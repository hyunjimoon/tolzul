# modules/cohorts.py
from __future__ import annotations
import re
from pathlib import Path
from typing import Dict, Iterable, List, Tuple, Optional

import pandas as pd
import numpy as np

# Optional: use RapidFuzz if available (faster/better than difflib)
try:
    from rapidfuzz import fuzz
    _USE_RAPIDFUZZ = True
except Exception:
    from difflib import SequenceMatcher
    _USE_RAPIDFUZZ = False


# --------------------------------------------------------------------------------------
# Cohort definitions (Era-of-Ferment cohorts: AV and 3DP)
# Source: 20startups.pdf (AV and 3DP exemplars)
# --------------------------------------------------------------------------------------

COHORTS: Dict[str, List[str]] = {
    "AV": [
        "Argo AI", "Ghost Autonomy", "Cruise", "Pony.ai", "Zoox",
        "Drive.ai", "May Mobility", "Nuro", "Aurora", "Wayve"
    ],
    "3DP": [
        "Relativity Space", "Desktop Metal", "Markforged", "Carbon", "Arevo",
        "Velo3D", "Impossible Objects", "Continuous Composites", "Origin", "Essentium"
    ]
}
COHORTS["ALL"] = COHORTS["AV"] + COHORTS["3DP"]


# --------------------------------------------------------------------------------------
# Utilities: normalization, reading, and indexing
# --------------------------------------------------------------------------------------

_AFFIXES = [
    r"\binc\b", r"\bincorporated\b", r"\bcorp\b", r"\bcorporation\b",
    r"\bltd\b", r"\bllc\b", r"\bco\b", r"\bcompany\b", r"\blabs\b",
    r"\btechnologies\b", r"\btechnology\b", r"\bsystems\b"
]
_AFFIX_RE = re.compile("|".join(_AFFIXES))

def normalize_text(s: str) -> str:
    """Lowercase, strip punctuation/affixes; keep alphanumerics/spaces."""
    if not isinstance(s, str):
        return ""
    s = s.lower()
    s = re.sub(r"[^\w\s]", " ", s)          # remove punctuation (keep letters/numbers/space)
    s = _AFFIX_RE.sub("", s)                # drop common company suffixes
    s = re.sub(r"\s+", " ", s).strip()
    return s

def normalize_id(x) -> str:
    """Always treat company ids as strings; do not cast to int."""
    if pd.isna(x):
        return ""
    return str(x).strip()

def pick_id_and_name_columns(df: pd.DataFrame) -> Tuple[str, str]:
    cand_ids = ["CompanyID", "company_id", "firm_id", "id"]
    cand_names = ["CompanyName", "company_name", "Name", "name"]
    id_col = next((c for c in cand_ids if c in df.columns), None)
    nm_col = next((c for c in cand_names if c in df.columns), None)
    if not id_col or not nm_col:
        raise ValueError("Could not find CompanyID/company_id and CompanyName/company_name columns.")
    return id_col, nm_col

def build_name_index(df: pd.DataFrame) -> Dict[str, List[Tuple[str, str]]]:
    """
    Map normalized company name -> list of (company_id_str, original_name).
    Multiple IDs per name are allowed (ambiguity handled later).
    """
    id_col, nm_col = pick_id_and_name_columns(df)
    idx: Dict[str, List[Tuple[str, str]]] = {}
    for _, r in df[[id_col, nm_col]].dropna().iterrows():
        cid = normalize_id(r[id_col])
        nm = str(r[nm_col]).strip()
        key = normalize_text(nm)
        idx.setdefault(key, []).append((cid, nm))
    return idx

def union_name_index(snapshots: Dict[str, pd.DataFrame]) -> Dict[str, List[Tuple[str, str, str]]]:
    """
    Union index across snapshots: name_key -> list of (company_id, orig_name, snapshot_key).
    """
    out: Dict[str, List[Tuple[str, str, str]]] = {}
    for snap_key, df in snapshots.items():
        sub = build_name_index(df)
        for key, pairs in sub.items():
            out.setdefault(key, [])
            out[key].extend([(cid, orig, snap_key) for cid, orig in pairs])
    return out


# --------------------------------------------------------------------------------------
# Name resolution (fuzzy)
# --------------------------------------------------------------------------------------

def _score(a: str, b: str) -> float:
    if _USE_RAPIDFUZZ:
        return fuzz.ratio(a, b) / 100.0
    return SequenceMatcher(None, a, b).ratio()

def resolve_cohort_ids(
    input_names: Iterable[str],
    snapshots: Dict[str, pd.DataFrame],
    cutoff: float = 0.82
) -> pd.DataFrame:
    """
    Resolve canonical cohort names to PitchBook CompanyIDs (string) via fuzzy matching.

    Returns a DataFrame:
        ['input_name','matched_name','company_id','snapshot','score']
    """
    name_index = union_name_index(snapshots)
    index_keys = list(name_index.keys())

    rows = []
    for raw in input_names:
        qkey = normalize_text(raw)
        # exact match first
        if qkey in name_index:
            # if multiple ids for same key, keep all (dedupe later)
            for cid, onm, snap in name_index[qkey]:
                rows.append((raw, onm, cid, snap, 1.0))
            continue

        # fuzzy best
        best_key, best_score = None, -1.0
        for k in index_keys:
            sc = _score(qkey, k)
            if sc > best_score:
                best_key, best_score = k, sc

        if best_key is not None and best_score >= cutoff:
            for cid, onm, snap in name_index[best_key]:
                rows.append((raw, onm, cid, snap, float(best_score)))
        else:
            rows.append((raw, "", "", "", float(best_score)))

    mt = pd.DataFrame(rows, columns=["input_name","matched_name","company_id","snapshot","score"])
    # Deduplicate: keep best row per input_name
    mt = mt.sort_values(["input_name","score"], ascending=[True, False]).drop_duplicates(["input_name"], keep="first")
    return mt


# --------------------------------------------------------------------------------------
# Trace extraction across snapshots
# --------------------------------------------------------------------------------------

_TRACE_COLS = [
    "CompanyID","CompanyName","LastFinancingDate","LastFinancingDealType",
    "CompanyFinancingStatus","BusinessStatus","Description","Keywords","YearFounded"
]

def extract_traces(
    cohort_ids: Iterable[str],
    snapshots: Dict[str, pd.DataFrame]
) -> pd.DataFrame:
    """
    Long panel for a set of company_ids across snapshots.
    """
    traces = []
    for snap_key, df in snapshots.items():
        id_col, nm_col = pick_id_and_name_columns(df)
        use_cols = [c for c in _TRACE_COLS if c in df.columns]
        sub = df[df[id_col].astype(str).isin([normalize_id(x) for x in cohort_ids])][use_cols].copy()
        sub["snapshot"] = snap_key
        # normalize column names
        if "CompanyID" in sub.columns:
            sub.rename(columns={"CompanyID": "company_id"}, inplace=True)
        if "CompanyName" in sub.columns:
            sub.rename(columns={"CompanyName": "company_name"}, inplace=True)
        traces.append(sub)
    if not traces:
        return pd.DataFrame(columns=["company_id","company_name","snapshot"])
    out = pd.concat(traces, axis=0, ignore_index=True)
    return out


# --------------------------------------------------------------------------------------
# Cohort-restricted hypothesis testing
# --------------------------------------------------------------------------------------

def run_cohort_analysis(
    cohort_names: List[str],
    snapshots: Dict[str, pd.DataFrame],
    match_cutoff: float = 0.82
) -> Dict[str, pd.DataFrame]:
    """
    Resolve IDs, extract traces, and run H1/H2 on cohort only.
    Uses the same functions as your main pipeline for comparability.

    Returns dict with:
      - match_table
      - traces
      - h1_coeffs
      - h2_main_coeffs
      - analysis_df (merged features + DV for cohort)
    """
    # 1) Name → ID
    mt = resolve_cohort_ids(cohort_names, snapshots, cutoff=match_cutoff)

    resolved = mt[mt["company_id"].astype(str).str.len() > 0]
    cohort_ids = sorted(resolved["company_id"].astype(str).unique().tolist())

    # 2) Traces
    traces = extract_traces(cohort_ids, snapshots)

    # 3) Create DV + features → restrict to cohort
    # Reuse existing pipeline functions to keep identical specs
    from modules.features import (
        engineer_features, compute_founder_credibility, extract_sector_fe,
        create_survival_seriesb_progression, preprocess_for_h2
    )
    from modules.models import (
        test_h1_early_funding, test_h2_main_survival
    )

    # DV within 17‑month window, exactly as in main pipeline
    dv = create_survival_seriesb_progression(
        df_baseline=snapshots["t0"],
        df_mid1=snapshots["tm1"],
        df_mid2=snapshots["tm2"],
        df_endpoint=snapshots["t1"],
        baseline_date="2021-12-01",
        mid1_date="2022-01-01",
        mid2_date="2022-05-01",
        endpoint_date="2023-05-01"
    )
    dv = dv[dv["company_id"].astype(str).isin(cohort_ids)].copy()

    # Features from baseline
    df0 = snapshots["t0"].copy()
    # Keep only cohort ids before engineering (saves time/mem)
    id_col, _ = pick_id_and_name_columns(df0)
    df0 = df0[df0[id_col].astype(str).isin(cohort_ids)].copy()

    feats = engineer_features(df0)
    # founder credibility
    feats["founder_credibility"] = compute_founder_credibility(feats)
    # sector FE (defensive)
    if "sector_fe" not in feats.columns and "keywords" in feats.columns:
        feats["sector_fe"] = extract_sector_fe(feats["keywords"])

    # H2 preprocess (creates z_vagueness, ic_within, founding_cohort, etc.)
    feats = preprocess_for_h2(feats)

    # Merge DV + predictors using string id
    # Harmonize id column name
    if "CompanyID" in feats.columns:
        feats.rename(columns={"CompanyID": "company_id"}, inplace=True)
    analysis_df = feats.merge(dv, on="company_id", how="inner")
    # Standardize DV column name for the model
    analysis_df["survival"] = analysis_df["Y_primary"]

    # H1: only firms with early_funding info
    df_h1 = feats[feats["early_funding_musd"].notna()].copy()
    h1_res = test_h1_early_funding(df_h1)

    # H2: cohort, non‑censored
    df_h2 = analysis_df[analysis_df["survival"].notna()].copy()
    h2_res = test_h2_main_survival(df_h2)

    # Packaging outputs
    h1_coeffs = pd.DataFrame({
        "variable": h1_res.params.index,
        "coefficient": h1_res.params.values,
        "std_err": h1_res.bse.values,
        "t": h1_res.tvalues.values,
        "p_value": h1_res.pvalues.values,
        "ci_lower": h1_res.conf_int()[0].values,
        "ci_upper": h1_res.conf_int()[1].values
    })
    h2_main_coeffs = pd.DataFrame({
        "variable": h2_res.params.index,
        "coefficient": h2_res.params.values,
        "std_err": h2_res.bse.values,
        "z": h2_res.tvalues.values,
        "p_value": h2_res.pvalues.values,
        "ci_lower": h2_res.conf_int()[0].values,
        "ci_upper": h2_res.conf_int()[1].values
    })

    return {
        "match_table": mt,
        "traces": traces,
        "h1_coeffs": h1_coeffs,
        "h2_main_coeffs": h2_main_coeffs,
        "analysis_df": analysis_df
    }
