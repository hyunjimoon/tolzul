from typing import Protocol, Dict, Any, Tuple
import pandas as pd

class EmpiricsEngine(Protocol):
    """
    The Protocol (Job Description) for all Specialist Ships (P1, P2, P3).
    Any module acting as an 'Empirics Engine' must implement these methods.
    """
    
    def generate_dummy_data(self) -> pd.DataFrame:
        """Generate or load the dataset."""
        ...

    def run_h1_ols(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Run Hypothesis 1 analysis (Linear)."""
        ...

    def run_h2_logit(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Run Hypothesis 2 analysis (Logit/Interaction)."""
        ...
        
    def main(self) -> Tuple[pd.DataFrame, Dict, Dict, Dict, pd.DataFrame]:
        """
        Execute the full pipeline.
        Returns: (df, h1_results, h2_results, robustness, coef_table)
        """
        ...
