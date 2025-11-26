# modules/cohorts.py
# -*- coding: utf-8 -*-
"""
Cohort tools for Era-of-Ferment analysis (AV & 3DP)
- Name matching (robust) across PitchBook snapshots
- Cohort windows (from research slides)
- Trace extractor + targeted H1/H2 analysis

Depends on your existing modules:
  - modules.features (engineer_features, preprocess_for_h2, create_survival_seriesb_progression)
  - modules.models (test_h1_early_funding, test_h2_main_survival)

Author: W1 cohort pipeline
"""

from __future__ import annotations
import re
import difflib
from dataclasses import dataclass
from typing import Dict, List, Tuple, Iterable, Optional

import numpy as np
import pandas as pd
from pathlib import Path

# --------------------------------------------------------------------------------------
# 0) Cohort definitions (names from 20startups list; windows from the cohort slides)
#     3DP (2013–2015), AV (2015–2018) – era-of-ferment cohorts
# --------------------------------------------------------------------------------------

COHORTS: Dict[str, Dict] = {
    "AV": {
        "window": (2015, 2018),  # founding-year window (inclusive)
        "names": [
            "Argo AI", "Ghost Autonomy", "Wayve", "Cruise", "Pony.ai",
            "Zoox", "Drive.ai", "May Mobility", "Nuro", "Aurora"
        ],
        "label": "AV (2015–2018)"
    },
    "3DP": {
        "window": (2013, 2015),  # founding-year window (inclusive)
        "names": [
            "Relativity Space", "Desktop Metal", "Markforged", "Carbon", "Arevo",
            "Velo3D", "Impossible Objects", "Continuous Composites", "Origin", "Essentium"
        ],
        "label": "3DP (2013–2015)"
    }
}

# --------------------------------------------------------------------------------------
# 1) Utility: company name normalization and fuzzy matching
# --------------------------------------------------------------------------------------

_PUNCT = re.compile(r"[^\w\s]")

def normalize_name(name: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace, drop suffixes."""
    if not isinstance(name, str):
        return ""
    n = name.lower().strip()
    n = _PUNCT.sub(" ", n)
    n = re.sub(r"\b(inc|co|corp|llc|ltd|gmbh|plc|incorporated|corporation)\b\.?", "", n)
    n = re.sub(r"\s+", " ", n).strip()
    return n

def build_name_index(df: pd.DataFrame, id_col: str, name_col: str) -> Dict[str, List[Tuple[str,int]]]:
    """Map normalized names to [(original_name, company_id), ...]."""
    index: Dict[str, List[Tuple[str,int]]] = {}
    if name_col not in df.columns or id_col not in df.columns:
        return index
    for _, r in df[[name_col, id_col]].dropna().iterrows():
        key = normalize_name(str(r[name_col]))
        if not key:
            continue
        item = (str(r[name_col]), int(r[id_col]))
        index.setdefault(key, []).append(item)
    return index

def best_match(name: str, all_keys: Iterable[str], cutoff: float = 0.82) -> Optional[str]:
    """Return best normalized-name key by difflib ratio above cutoff."""
    key = normalize_name(name)
    if not key:
        return None
    candidates = difflib.get_close_matches(key, list(all_keys), n=1, cutoff=cutoff)
    return candidates[0] if candidates else None

# --------------------------------------------------------------------------------------
# 2) Snapshot tools
# --------------------------------------------------------------------------------------

def detect_id_and_name_cols(df: pd.DataFrame) -> Tuple[str, str]:
    """Return (id_col, name_col) best guess."""
    id_col = "CompanyID" if "CompanyID" in df.columns else ("company_id" if "company_id" in df.columns else None)
    name_col = "CompanyName" if "CompanyName" in df.columns else ("company_name" if "company_name" in df.columns else None)
    if id_col is None or name_col is None:
        cols = ", ".join(df.columns[:15])
        raise ValueError(f"Could not detect ID/Name columns. Columns: {cols}")
    return id_col, name_col

def union_name_index(snapshots: Dict[str, pd.DataFrame]) -> Tuple[Dict[str, List[Tuple[str,int]]], str, str]:
    """
    Build a unified name → [(name, id)] index across multiple snapshots.
    Returns index and the detected (id_col, name_col).
    """
    assert snapshots, "snapshots dict empty"
    # Use the first frame to detect column names
    first = next(iter(snapshots.values()))
    id_col, name_col = detect_id_and_name_cols(first)
    idx: Dict[str, List[Tuple[str,int]]] = {}
    for df in snapshots.values():
        # be robust to different casings across files
        cand_id = "CompanyID" if "CompanyID" in df.columns else ("company_id" if "company_id" in df.columns else id_col)
        cand_name = "CompanyName" if "CompanyName" in df.columns else ("company_name" if "company_name" in df.columns else name_col)
        sub_idx = build_name_index(df, cand_id, cand_name)
        for k, vals in sub_idx.items():
            idx.setdefault(k, []).extend(vals)
    return idx, id_col, name_col

def resolve_cohort_ids(cohort_names: List[str], snapshots: Dict[str, pd.DataFrame], cutoff: float = 0.82) -> pd.DataFrame:
    """
    Resolve cohort company names to IDs using fuzzy matching across all snapshots.
    Returns a mapping table: [query_name, matched_name, company_id, match_score]
    """
    idx, id_col, name_col = union_name_index(snapshots)
    keys = list(idx.keys())

    rows = []
    for q in cohort_names:
        qn = normalize_name(q)
        match_key = best_match(q, keys, cutoff=cutoff)
        if match_key is None:
            rows.append({"query_name": q, "matched_name": None, "company_id": None, "match_score": 0.0})
            continue
        # compute similarity ratio for reporting
        score = difflib.SequenceMatcher(None, qn, match_key).ratio()
        # choose the modal (name, id) pair by frequency across snapshots
        candidates = idx[match_key]
        # if multiple IDs, choose the one appearing most; break ties by latest snapshot ‘t1’
        df_cand = pd.DataFrame(candidates, columns=["matched_name", "company_id"])
        pick = (df_cand["company_id"].value_counts().idxmax())
        # find at least one original name string for this id
        matched_name = df_cand[df_cand["company_id"] == pick]["matched_name"].iloc[0]
        rows.append({"query_name": q, "matched_name": matched_name, "company_id": int(pick), "match_score": float(score)})
    return pd.DataFrame(rows)

# --------------------------------------------------------------------------------------
# 3) Trace extractor (A-stage vs B+ / M&A across snapshots)
#     Lightweight "as-of" stage label for human-readable cohort traces
# --------------------------------------------------------------------------------------

_A_STAGE_PAT = re.compile(r"(?:\bSeries\s*A(?:[-\s]?\d+|[A-Z])?\b|\bEarly[-\s]*Stage\s*VC\b)", re.I)
_B_PLUS_PAT = re.compile(r"(?:\bLater[-\s]*Stage\s*VC\b|\bSeries\s*[B-G](?:[-\s]?\d+|[A-Z])?\b)", re.I)
_MA_PAT = re.compile(r"(Merger|Acquisition|Buyout|LBO)", re.I)

def _stage_label(deal_type: str, business_status: Optional[str] = None) -> str:
    s = str(deal_type or "")
    if business_status == "Out of Business":
        return "OOB"
    if _MA_PAT.search(s or ""):
        return "M&A"
    if _B_PLUS_PAT.search(s or ""):
        return "B+"
    if _A_STAGE_PAT.search(s or ""):
        return "A"
    return "Other/Unknown"

def extract_trace_for_ids(snapshots: Dict[str, pd.DataFrame], company_ids: Iterable[int]) -> pd.DataFrame:
    """
    For a set of company_ids, return a human-readable trace across snapshots:
    columns: [company_id, CompanyName, stage_t0, stage_tm1, stage_tm2, stage_t1]
    """
    # normalize column names per snapshot
    def col(df, name, fallback):
        return name if name in df.columns else fallback

    out = []
    for tag, df in snapshots.items():
        # robust column detection
        id_col, name_col = detect_id_and_name_cols(df)
        type_col = "LastFinancingDealType" if "LastFinancingDealType" in df.columns else "last_financing_deal_type"
        status_col = "BusinessStatus" if "BusinessStatus" in df.columns else ("business_status" if "business_status" in df.columns else None)

        sub = df[df[id_col].isin(company_ids)][[id_col, name_col, type_col] + ([status_col] if status_col else [])].copy()
        sub.rename(columns={id_col: "company_id", name_col: "CompanyName", type_col: "LastFinancingDealType"}, inplace=True)
        sub["stage_"+tag] = sub.apply(
            lambda r: _stage_label(r["LastFinancingDealType"], r[status_col] if status_col else None),
            axis=1
        )
        keep = ["company_id", "CompanyName", "stage_"+tag]
        out.append(sub[keep])

    # outer-merge across snapshots
    from functools import reduce
    trace = reduce(lambda l, r: pd.merge(l, r, on=["company_id", "CompanyName"], how="outer"), out)
    return trace

# --------------------------------------------------------------------------------------
# 4) Cohort analysis runner (engineer features → preprocess → survival DV → merge → filter → H1/H2)
# --------------------------------------------------------------------------------------

@dataclass
class CohortRunResult:
    cohort: str
    match_table_path: Path
    trace_path: Path
    h1_coef_path: Path
    h2_coef_path: Path
    h2_dataset_path: Path
    n_matched: int

def run_cohort_analysis(
    cohort_name: str,
    snapshots: Dict[str, pd.DataFrame],
    output_dir: Path,
    features_module,
    models_module,
    match_cutoff: float = 0.82
) -> CohortRunResult:
    """
    Execute the full H1/H2 pipeline restricted to a cohort (by names).

    Parameters
    ----------
    cohort_name : "AV" | "3DP"
    snapshots   : dict with keys {'t0','tm1','tm2','t1'} → company snapshots (as in run_analysis.py)
    output_dir  : base output directory; a subfolder outputs/cohorts/<cohort_name> will be created
    features_module : imported modules.features
    models_module   : imported modules.models
    match_cutoff    : float, fuzzy match threshold (0–1)

    Returns
    -------
    CohortRunResult with file paths.
    """
    assert cohort_name in COHORTS, f"Unknown cohort: {cohort_name}"
    cohort_info = COHORTS[cohort_name]
    names = cohort_info["names"]

    out_dir = Path(output_dir) / "cohorts" / cohort_name
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1) Resolve names → IDs (across all snapshots)
    print(f"\n[COHORT] {cohort_name}: resolving {len(names)} names with cutoff={match_cutoff}…")
    match_table = resolve_cohort_ids(names, snapshots, cutoff=match_cutoff)
    match_table.to_csv(out_dir / "cohort_match_table.csv", index=False)
    print(f"  ✓ Saved: {out_dir/'cohort_match_table.csv'}")

    matched_ids = [int(x) for x in match_table["company_id"].dropna().astype(int).tolist()]
    if len(matched_ids) == 0:
        raise RuntimeError(f"No cohort companies matched in snapshots for {cohort_name} (cutoff={match_cutoff}).")

    # 2) Human-readable traces across snapshots (A/B+/M&A/OOB)
    trace_df = extract_trace_for_ids(snapshots, matched_ids)
    trace_df.to_csv(out_dir / "cohort_trace.csv", index=False)
    print(f"  ✓ Saved: {out_dir/'cohort_trace.csv'}")

    # 3) Survival DV (Series B+ within 17m) using your canonical function
    surv_df = features_module.create_survival_seriesb_progression(
        df_baseline=snapshots['t0'],
        df_mid1=snapshots['tm1'],
        df_mid2=snapshots['tm2'],
        df_endpoint=snapshots['t1'],
        baseline_date="2021-12-01",
        mid1_date="2022-01-01",
        mid2_date="2022-05-01",
        endpoint_date="2023-05-01"
    )
    # returns company_id + Y_primary/Y_MA_upper/Y_MA_lower/at_risk

    # 4) Predictors from baseline; add founder_credibility and sector FE if present
    base = features_module.engineer_features(snapshots['t0'])
    # Keep both labels for your current stack:
    # - high_integration_cost (existing models)
    # - is_hardware (alias for readability; 1=hardware/integrated, 0=software/modular)
    if "high_integration_cost" in base.columns:
        base["is_hardware"] = base["high_integration_cost"].astype(int)
    else:
        # in case the features module changes names in future
        base["high_integration_cost"] = base.get("is_hardware", 0).astype(int)

    # founder credibility
    if hasattr(features_module, "compute_founder_credibility"):
        base["founder_credibility"] = features_module.compute_founder_credibility(base)
    else:
        base["founder_credibility"] = 0

    # sector FE if missing but keywords exist
    if "sector_fe" not in base.columns and "keywords" in base.columns and hasattr(features_module, "extract_sector_fe"):
        base["sector_fe"] = features_module.extract_sector_fe(base["keywords"])

    # 5) Preprocess for H2 (z-scores, cohorts, ic_within, etc.)
    base = features_module.preprocess_for_h2(base)

    # 6) Merge DV + predictors, then filter to matched cohort IDs only
    id_col = "CompanyID" if "CompanyID" in base.columns else "company_id"
    analysis = base.merge(surv_df.rename(columns={"company_id": id_col}), on=id_col, how="inner")
    analysis["survival"] = analysis["Y_primary"]
    analysis = analysis[analysis[id_col].isin(matched_ids)].copy()

    # Save the full cohort analysis dataset (required output)
    analysis_out = out_dir / "h2_analysis_dataset.csv"
    analysis.to_csv(analysis_out, index=False)
    print(f"  ✓ Saved: {analysis_out}")

    # 7) H1 (subset with early_funding) and H2 (subset with non‑censored survival)
    # H1
    df_h1 = analysis[analysis["early_funding_musd"].notna()].copy()
    h1_model = models_module.test_h1_early_funding(df_h1)
    h1_coef = pd.DataFrame({
        'variable': h1_model.params.index,
        'coefficient': h1_model.params.values,
        'std_err': h1_model.bse.values,
        't': h1_model.tvalues.values,
        'p_value': h1_model.pvalues.values,
        'ci_lower': h1_model.conf_int()[0].values,
        'ci_upper': h1_model.conf_int()[1].values
    })
    h1_out = out_dir / "h1_coefficients.csv"
    h1_coef.to_csv(h1_out, index=False)
    print(f"  ✓ Saved: {h1_out}")

    # H2 (primary spec; M&A censored)
    df_h2 = analysis[analysis["survival"].notna()].copy()
    h2_model = models_module.test_h2_main_survival(df_h2)
    h2_coef = pd.DataFrame({
        'variable': h2_model.params.index,
        'coefficient': h2_model.params.values,
        'std_err': h2_model.bse.values,
        'z': h2_model.tvalues.values,
        'p_value': h2_model.pvalues.values,
        'ci_lower': h2_model.conf_int()[0].values,
        'ci_upper': h2_model.conf_int()[1].values
    })
    h2_out = out_dir / "h2_main_coefficients.csv"
    h2_coef.to_csv(h2_out, index=False)
    print(f"  ✓ Saved: {h2_out}")

    return CohortRunResult(
        cohort=cohort_name,
        match_table_path=out_dir / "cohort_match_table.csv",
        trace_path=out_dir / "cohort_trace.csv",
        h1_coef_path=h1_out,
        h2_coef_path=h2_out,
        h2_dataset_path=analysis_out,
        n_matched=len(matched_ids)
    )
