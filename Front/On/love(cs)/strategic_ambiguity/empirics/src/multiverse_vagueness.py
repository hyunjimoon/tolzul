# src/multiverse_vagueness.py
"""
Multi-Metric Vagueness Analysis Framework

Supports multiple vagueness metrics with full metadata tracking via xarray/NetCDF.
Each metric is stored with attributes documenting:
  - scorer_class: Which scorer class was used
  - scorer_version: Version identifier
  - components: List of component scores
  - references: Academic citations
  - computed_at: Timestamp

Usage:
    from multiverse_vagueness import VaguenessMultiverse

    mv = VaguenessMultiverse()
    ds = mv.compute_all_metrics(df)  # Returns xarray.Dataset with all metrics
    mv.save(ds, 'outputs/vagueness_multiverse.nc')
"""

from datetime import datetime
from typing import Dict, List, Optional
import pandas as pd
import numpy as np
import xarray as xr

from .vagueness_v2 import StrategicVaguenessScorerV2, HybridVaguenessScorerV2
from .vagueness_v3 import StrategicVaguenessScorerV3


# =============================================================================
# Metric Registry: All available vagueness metrics
# =============================================================================
VAGUENESS_METRICS = {
    "v2_categorical": {
        "name": "Categorical Vagueness (V2)",
        "description": "Density of abstract marketing keywords weighted by IDF",
        "components": ["S_cat"],
        "references": ["Zuckerman 1999", "Hannan et al. 2007", "Pontikes 2012"],
        "scorer_class": "StrategicVaguenessScorerV2",
        "output_key": "S_cat",
    },
    "v2_concreteness_deficit": {
        "name": "Concreteness Deficit (V2)",
        "description": "Absence of specific signals (numbers, dates, versions, units)",
        "components": ["S_concdef"],
        "references": ["Pan et al. 2018", "Chen et al. 2015"],
        "scorer_class": "StrategicVaguenessScorerV2",
        "output_key": "S_concdef",
    },
    "v2_raw": {
        "name": "V2 Raw Composite",
        "description": "0.5*max(S_cat, S_concdef) + 0.5*mean(S_cat, S_concdef)",
        "components": ["S_cat", "S_concdef"],
        "references": ["Zuckerman 1999", "Pan et al. 2018"],
        "scorer_class": "StrategicVaguenessScorerV2",
        "output_key": "V_raw",
    },
    "v2_hybrid": {
        "name": "V2 Hybrid (Current Default)",
        "description": "50% V2 linguistic + 50% inverse concrete feature count",
        "components": ["S_cat", "S_concdef", "concrete_count"],
        "references": ["Zuckerman 1999", "Pan et al. 2018", "Chen et al. 2015"],
        "scorer_class": "HybridVaguenessScorerV2",
        "output_key": "V_minmax",
    },
    "v3_market_entropy": {
        "name": "Market Entropy (V3)",
        "description": "Shannon entropy over market keyword categories - measures optionality",
        "components": ["V_market_entropy"],
        "references": ["Shannon 1948", "Thesis §3-4"],
        "scorer_class": "StrategicVaguenessScorerV3",
        "output_key": "V_market_entropy",
    },
    "v3_tech_abstractness": {
        "name": "Tech Abstractness (V3)",
        "description": "Inverse of technical specificity density",
        "components": ["V_tech_abstractness"],
        "references": ["Thesis §3-4"],
        "scorer_class": "StrategicVaguenessScorerV3",
        "output_key": "V_tech_abstractness",
    },
    "v3_composite": {
        "name": "V3 Composite",
        "description": "100 * (0.5*(1-entropy) + 0.5*(abstractness/100))",
        "components": ["V_market_entropy", "V_tech_abstractness"],
        "references": ["Thesis §3-4"],
        "scorer_class": "StrategicVaguenessScorerV3",
        "output_key": "V_composite",
    },
}


class VaguenessMultiverse:
    """
    Compute and store multiple vagueness metrics with full metadata.

    Each metric is stored in an xarray Dataset with:
    - Variable-level attributes (scorer, components, references)
    - Global attributes (dataset info, computation timestamp)
    """

    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self._scorers: Dict[str, object] = {}

    def _get_scorer(self, scorer_class: str):
        """Lazy initialization of scorers."""
        if scorer_class not in self._scorers:
            if scorer_class == "StrategicVaguenessScorerV2":
                self._scorers[scorer_class] = StrategicVaguenessScorerV2(
                    use_idf=True, random_state=self.random_state
                )
            elif scorer_class == "HybridVaguenessScorerV2":
                self._scorers[scorer_class] = HybridVaguenessScorerV2(
                    use_idf=True, random_state=self.random_state
                )
            elif scorer_class == "StrategicVaguenessScorerV3":
                self._scorers[scorer_class] = StrategicVaguenessScorerV3()
            else:
                raise ValueError(f"Unknown scorer class: {scorer_class}")
        return self._scorers[scorer_class]

    def compute_all_metrics(
        self,
        df: pd.DataFrame,
        description_col: str = "description",
        keywords_col: str = "keywords",
        company_id_col: str = "CompanyID",
        metrics: Optional[List[str]] = None
    ) -> xr.Dataset:
        """
        Compute all (or selected) vagueness metrics and return as xarray Dataset.

        Parameters
        ----------
        df : pd.DataFrame
            Input DataFrame with text columns
        description_col : str
            Column name for company descriptions
        keywords_col : str
            Column name for keywords
        company_id_col : str
            Column name for company identifiers
        metrics : list[str], optional
            List of metric keys to compute. If None, computes all.

        Returns
        -------
        xr.Dataset
            Dataset with each metric as a data variable, including metadata
        """
        if metrics is None:
            metrics = list(VAGUENESS_METRICS.keys())

        # Prepare text data
        texts = (
            df[description_col].fillna('') + ' ' +
            df.get(keywords_col, pd.Series([''] * len(df))).fillna('')
        ).tolist()

        # Company IDs as coordinates
        company_ids = df[company_id_col].values if company_id_col in df.columns else np.arange(len(df))

        # Compute each metric
        data_vars = {}

        # V2 scores (compute once, extract components)
        if any(m.startswith("v2_") for m in metrics):
            print("Computing V2 metrics...")
            scorer_v2 = self._get_scorer("StrategicVaguenessScorerV2")
            scorer_v2.fit(texts)
            v2_df = scorer_v2.transform(texts)

            for metric_key in metrics:
                if not metric_key.startswith("v2_") or metric_key == "v2_hybrid":
                    continue
                meta = VAGUENESS_METRICS[metric_key]
                output_key = meta["output_key"]

                data_vars[metric_key] = xr.DataArray(
                    data=v2_df[output_key].values,
                    dims=["company"],
                    attrs={
                        "long_name": meta["name"],
                        "description": meta["description"],
                        "scorer_class": meta["scorer_class"],
                        "scorer_version": "V2",
                        "components": ", ".join(meta["components"]),
                        "references": ", ".join(meta["references"]),
                        "units": "0-100 scale" if output_key != "V_market_entropy" else "0-1 scale",
                    }
                )

        # V2 Hybrid
        if "v2_hybrid" in metrics:
            print("Computing V2-Hybrid metric...")
            scorer_hybrid = self._get_scorer("HybridVaguenessScorerV2")
            scorer_hybrid.fit(texts)
            hybrid_scores = scorer_hybrid.transform(texts)

            meta = VAGUENESS_METRICS["v2_hybrid"]
            data_vars["v2_hybrid"] = xr.DataArray(
                data=hybrid_scores[:, 4],  # V_minmax column
                dims=["company"],
                attrs={
                    "long_name": meta["name"],
                    "description": meta["description"],
                    "scorer_class": meta["scorer_class"],
                    "scorer_version": "V2-Hybrid",
                    "components": ", ".join(meta["components"]),
                    "references": ", ".join(meta["references"]),
                    "units": "0-100 scale",
                    "note": "This is the current default metric in h2_analysis_dataset.csv",
                }
            )

        # V3 scores
        if any(m.startswith("v3_") for m in metrics):
            print("Computing V3 metrics...")
            scorer_v3 = self._get_scorer("StrategicVaguenessScorerV3")
            scorer_v3.fit(texts)
            v3_df = scorer_v3.score_series(texts)

            for metric_key in metrics:
                if not metric_key.startswith("v3_"):
                    continue
                meta = VAGUENESS_METRICS[metric_key]
                output_key = meta["output_key"]

                data_vars[metric_key] = xr.DataArray(
                    data=v3_df[output_key].values,
                    dims=["company"],
                    attrs={
                        "long_name": meta["name"],
                        "description": meta["description"],
                        "scorer_class": meta["scorer_class"],
                        "scorer_version": "V3",
                        "components": ", ".join(meta["components"]),
                        "references": ", ".join(meta["references"]),
                        "units": "0-1 scale" if "entropy" in output_key else "0-100 scale",
                    }
                )

        # Create Dataset
        ds = xr.Dataset(
            data_vars=data_vars,
            coords={"company": company_ids},
            attrs={
                "title": "Vagueness Multiverse Dataset",
                "description": "Multiple vagueness metrics for robustness analysis",
                "created_at": datetime.now().isoformat(),
                "source_file": "multiverse_vagueness.py",
                "n_companies": len(df),
                "metrics_computed": ", ".join(metrics),
            }
        )

        return ds

    def save(self, ds: xr.Dataset, path: str) -> None:
        """Save Dataset to NetCDF with full metadata."""
        ds.to_netcdf(path, mode='w')
        print(f"Saved to {path}")
        print(f"  Metrics: {list(ds.data_vars)}")
        print(f"  N: {len(ds.company)}")

    def load(self, path: str) -> xr.Dataset:
        """Load Dataset from NetCDF with metadata."""
        return xr.open_dataset(path)


def run_multiverse_analysis(
    df: pd.DataFrame,
    output_path: str = "outputs/vagueness_multiverse.nc",
    metrics: Optional[List[str]] = None
) -> xr.Dataset:
    """
    Convenience function to compute all metrics and save.

    Parameters
    ----------
    df : pd.DataFrame
        Input data with description and keywords columns
    output_path : str
        Where to save the NetCDF file
    metrics : list[str], optional
        Which metrics to compute (default: all)

    Returns
    -------
    xr.Dataset
        Dataset with all computed metrics
    """
    mv = VaguenessMultiverse()
    ds = mv.compute_all_metrics(df, metrics=metrics)
    mv.save(ds, output_path)
    return ds


# For CLI usage
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python multiverse_vagueness.py <input_csv> [output_nc]")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_nc = sys.argv[2] if len(sys.argv) > 2 else "outputs/vagueness_multiverse.nc"

    print(f"Loading {input_csv}...")
    df = pd.read_csv(input_csv, low_memory=False)

    print("Computing all vagueness metrics...")
    ds = run_multiverse_analysis(df, output_nc)

    print("\nMetric Summary:")
    for var in ds.data_vars:
        arr = ds[var]
        print(f"\n{var}:")
        print(f"  Name: {arr.attrs.get('long_name', 'N/A')}")
        print(f"  Mean: {float(arr.mean()):.2f}")
        print(f"  Std: {float(arr.std()):.2f}")
        print(f"  Scorer: {arr.attrs.get('scorer_class', 'N/A')}")
