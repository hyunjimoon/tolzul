# src/vagueness_v3.py
# =============================================================================
# StrategicVaguenessScorerV3
# -----------------------------------------------------------------------------
# Two orthogonal dimensions of vagueness:
#   (1) V_market_entropy     — market optionality via Shannon entropy
#   (2) V_tech_abstractness  — lack of concrete technical detail
#
# Implementation notes:
#   - Entropy uses category-hit counts from definitions.MARKET_KEYWORDS.
#     H_norm = H / log(K), K = #categories. This situates optionality in [0,1].
#     Intuition: broader category incidence => higher optionality. (Shannon 1948)
#   - Abstractness = 100 * (1 - normalize(density)), where density is
#     matches_per_word for metrics/units, timelines, and standards.
#     We learn robust min/max from the corpus (1–99% winsorized range).
#
# Theory anchors:
#   - Optionality (entropy) aligns with strategic flexibility and pivot potential;
#     abstractness proxies feasibility opacity. See thesis §3–4 for the staged
#     information vs. options narrative and the exercisability moderator.  # noqa
#   - For a legacy single score, we expose V_composite = 100 * (0.5*(1-H_norm)
#     + 0.5*(abstractness/100)), i.e., “low optionality + high abstractness”.
# =============================================================================

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np
import pandas as pd

from .definitions import MARKET_KEYWORDS, TECH_SPEC_PATTERNS, CONSTANTS


def _compile_or_pattern(keywords: List[str]) -> re.Pattern:
    """Compile a word-boundary OR-regex for keywords (case-insensitive)."""
    # Escape keywords and allow spaces/hyphens variants
    parts = []
    for kw in keywords:
        kw = kw.strip()
        if not kw:
            continue
        # Replace spaces with \s+ to catch hyphen/space variants
        safe = re.escape(kw).replace(r"\ ", r"\s+")
        parts.append(rf"(?:{safe})")
    if not parts:
        # Match nothing, never triggers
        return re.compile(r"(?!.).*")
    pattern = r"(?i)\b(?:%s)\b" % "|".join(parts)
    return re.compile(pattern, flags=re.IGNORECASE)


def _compile_multiline(pattern_str: str) -> re.Pattern:
    """Compile multi-line, case-insensitive regex from a verbose pattern string."""
    return re.compile(pattern_str, flags=re.IGNORECASE | re.VERBOSE)


@dataclass
class V3Calibration:
    """Holds dataset-calibrated bounds for density normalization."""
    dens_lo: float  # robust lower bound (e.g., 1st pct)
    dens_hi: float  # robust upper bound (e.g., 99th pct)


class StrategicVaguenessScorerV3:
    """Computes (V_market_entropy, V_tech_abstractness, V_composite) per text.

    Usage:
        scorer = StrategicVaguenessScorerV3()
        scorer.fit(text_series)    # learns density normalization
        out = scorer.score(text)   # dict with V_* fields
        df_scores = scorer.score_series(text_series)
    """

    def __init__(
        self,
        market_keywords: Optional[Dict[str, List[str]]] = None,
        tech_spec_patterns: Optional[Dict[str, str]] = None,
        calibration: Optional[V3Calibration] = None,
    ):
        self.market_keywords = market_keywords or MARKET_KEYWORDS
        self.tech_spec_patterns = tech_spec_patterns or TECH_SPEC_PATTERNS

        # Compile category patterns
        self._cat_patterns: Dict[str, re.Pattern] = {
            cat: _compile_or_pattern(words)
            for cat, words in self.market_keywords.items()
        }

        # Compile technical specificity patterns
        self._spec_patterns: List[re.Pattern] = [
            _compile_multiline(pat) for pat in self.tech_spec_patterns.values()
        ]

        self._K = len(self._cat_patterns)  # number of categories
        self._logK = math.log(max(self._K, 2))
        self.calibration = calibration or V3Calibration(dens_lo=0.0, dens_hi=0.1)

    # -----------------------
    # Public fitting routine
    # -----------------------
    def fit(self, texts: Iterable[str]) -> "StrategicVaguenessScorerV3":
        """Estimate robust bounds for density normalization from corpus.

        We compute matches-per-word density for each text, then set
        dens_lo = 1st percentile, dens_hi = 99th percentile.
        """
        densities = []
        for t in texts:
            d = self._density(t or "")
            densities.append(d)
        if not densities:
            self.calibration = V3Calibration(dens_lo=0.0, dens_hi=0.1)
            return self

        arr = np.asarray(densities, dtype=float)
        lo = float(np.nanpercentile(arr, 1))
        hi = float(np.nanpercentile(arr, 99))
        if not np.isfinite(lo):
            lo = 0.0
        if not np.isfinite(hi) or hi <= lo:
            # Fallback if degenerate
            hi = max(lo + 1e-6, 0.1)

        self.calibration = V3Calibration(dens_lo=lo, dens_hi=hi)
        return self

    # -----------------------
    # Core computations
    # -----------------------
    def _count_category_hits(self, text: str) -> Dict[str, int]:
        counts = {}
        for cat, pat in self._cat_patterns.items():
            matches = pat.findall(text)
            counts[cat] = len(matches)
        return counts

    def _compute_market_entropy(self, text: str) -> float:
        """Normalized Shannon entropy over category-hit distribution.

        H_norm in [0,1]; 0 when all mass is concentrated in a single category;
        max when hits are spread uniformly across categories.

        If no category is hit, returns 0 by convention.
        """
        counts = self._count_category_hits(text or "")
        total = sum(counts.values())
        if total == 0:
            return 0.0

        probs = np.array([c / total for c in counts.values()], dtype=float)
        # Numerical safety: remove zeros
        probs = probs[probs > 0]
        H = -np.sum(probs * np.log(probs + CONSTANTS["ENTROPY_EPS"]))
        H_norm = float(H / self._logK)
        # Bound to [0,1]
        return float(max(0.0, min(1.0, H_norm)))

    def _density(self, text: str) -> float:
        """Matches-per-word density for technical specificity signals."""
        if not text:
            return 0.0
        # Word count
        words = re.findall(r"\b\w+\b", text.lower())
        n_words = max(len(words), 1)
        # Combined matches from all patterns (allow overlaps across families)
        m = 0
        for pat in self._spec_patterns:
            m += len(pat.findall(text))
        return float(m) / float(n_words)

    def _compute_tech_abstractness(self, text: str) -> Tuple[float, float]:
        """Return (density, abstractness_score).

        abstractness_score = 100 * (1 - normalize(density; dens_lo, dens_hi))
        with clipping to [0, 100].
        """
        d = self._density(text or "")
        lo, hi = self.calibration.dens_lo, self.calibration.dens_hi
        # Normalize
        if hi <= lo:
            z = 0.0
        else:
            z = (d - lo) / (hi - lo)
        z = max(0.0, min(1.0, z))
        score = 100.0 * (1.0 - z)
        return d, float(score)

    # -----------------------
    # Public scoring methods
    # -----------------------
    def score(self, text: str) -> Dict[str, float]:
        """Score a single text."""
        H_norm = self._compute_market_entropy(text or "")
        _, abs_score = self._compute_tech_abstractness(text or "")

        # Legacy composite (scaled to 0-100):
        #   Higher when OPTIONALITY is low AND ABSTRACTNESS is high.
        composite = 100.0 * (0.5 * (1.0 - H_norm) + 0.5 * (abs_score / 100.0))

        return {
            "V_market_entropy": float(H_norm),        # [0,1]
            "V_tech_abstractness": float(abs_score),  # [0,100]
            "V_composite": float(composite),          # [0,100]
        }

    def score_series(self, texts: Iterable[str]) -> pd.DataFrame:
        """Vectorized scoring over an iterable/Series of texts."""
        # If texts is a Series, we can iterate directly
        out = {
            "V_market_entropy": [],
            "V_tech_abstractness": [],
            "V_composite": [],
        }
        for t in texts:
            s = self.score(t or "")
            out["V_market_entropy"].append(s["V_market_entropy"])
            out["V_tech_abstractness"].append(s["V_tech_abstractness"])
            out["V_composite"].append(s["V_composite"])
        return pd.DataFrame(out)
