"""
Strategic Vagueness Scorer V2
==============================

Computes vagueness using TWO components only:
  1. Categorical Vagueness (S_cat): abstract keyword use
  2. Concreteness Deficit (S_concdef): absence of specific references

Removed: lexical-uncertainty component (per research spec p.25-26)

Returns:
  - S_cat, S_concdef, V_raw (0-100 scale)
  - V_pct (percentile, global or within-group)
  - V_minmax (min-max normalized)

Author: 권준/나대용 (中軍)
Date: 2025-11-16
"""

import re
import warnings
from typing import Optional, List, Dict
import pandas as pd
import numpy as np
from collections import Counter


class StrategicVaguenessScorerV2:
    """
    Strategic Vagueness Scorer V2 - Two-component vagueness measure.

    Parameters
    ----------
    abstract_terms : list[str], optional
        Custom list of abstract/categorical terms. If None, uses default lexicon.
    unit_terms : list[str], optional
        Custom list of unit/spec terms for specificity detection. If None, uses defaults.
    use_idf : bool, default=True
        Weight abstract terms by inverse document frequency to reduce false positives.
    groupby_cols : list[str], optional
        Column names for group-wise percentile computation.
    random_state : int, default=0
        Random seed for reproducibility (currently unused but reserved).
    """

    # Default abstract terms lexicon
    DEFAULT_ABSTRACT_TERMS = [
        "platform", "solution", "ecosystem", "innovation", "AI-powered",
        "end-to-end", "digital transformation", "next-generation", "seamless",
        "synergy", "leverage", "framework", "infrastructure", "service layer",
        "suite", "experience", "future-proof", "cutting-edge", "revolutionary",
        "transformative", "strategic", "holistic", "integrated", "comprehensive",
        "robust", "scalable", "flexible", "agile", "dynamic", "optimize",
        "streamline", "enhance", "enable", "empower", "deliver", "drive",
        "value-added", "best-in-class", "world-class", "industry-leading",
        "state-of-the-art", "advanced", "sophisticated", "intelligent",
        "smart", "automated", "cloud-based", "enterprise-grade"
    ]

    # Default stopwords (generic English - do NOT remove domain terms)
    STOPWORDS = set([
        "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
        "has", "he", "in", "is", "it", "its", "of", "on", "that", "the",
        "to", "was", "will", "with", "we", "our", "this", "these", "those"
    ])

    def __init__(
        self,
        abstract_terms: Optional[List[str]] = None,
        unit_terms: Optional[List[str]] = None,
        use_idf: bool = True,
        groupby_cols: Optional[List[str]] = None,
        random_state: int = 0
    ):
        self.abstract_terms = abstract_terms or self.DEFAULT_ABSTRACT_TERMS
        self.unit_terms = unit_terms
        self.use_idf = use_idf
        self.groupby_cols = groupby_cols
        self.random_state = random_state

        # Build regex patterns
        self._abstract_pattern = self._build_abstract_pattern()
        self._idf_weights = {}
        self._fitted = False

    def _build_abstract_pattern(self) -> re.Pattern:
        """Build regex pattern for abstract terms (case-insensitive)."""
        # Escape special regex chars and handle multi-word terms
        escaped_terms = [re.escape(term) for term in self.abstract_terms]
        pattern = r'\b(' + '|'.join(escaped_terms) + r')\b'
        return re.compile(pattern, re.IGNORECASE)

    def _preprocess(self, text: str) -> str:
        """
        Preprocessing: lowercase, strip HTML, collapse whitespace.

        Parameters
        ----------
        text : str
            Raw input text

        Returns
        -------
        str
            Cleaned text
        """
        if not isinstance(text, str):
            return ""

        # Strip HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)

        # Lowercase
        text = text.lower()

        # Collapse whitespace
        text = re.sub(r'\s+', ' ', text).strip()

        return text

    def _tokenize(self, text: str) -> List[str]:
        """
        Tokenize on word boundaries; keep hyphenated terms.

        Parameters
        ----------
        text : str
            Preprocessed text

        Returns
        -------
        list[str]
            Tokens
        """
        # Match words including hyphenated terms
        pattern = r'\b[\w][\w\-]*\b'
        tokens = re.findall(pattern, text)
        return tokens

    def _compute_idf(self, texts: List[str]) -> Dict[str, float]:
        """
        Compute inverse document frequency for abstract terms.

        Parameters
        ----------
        texts : list[str]
            Corpus of preprocessed texts

        Returns
        -------
        dict
            IDF weights for each abstract term
        """
        n_docs = len(texts)
        doc_freq = Counter()

        for text in texts:
            # Find unique abstract terms in this document
            matches = set(self._abstract_pattern.findall(text))
            for term in matches:
                doc_freq[term.lower()] += 1

        # Compute IDF: log(N / df)
        idf = {}
        for term in self.abstract_terms:
            df = doc_freq.get(term.lower(), 0)
            if df > 0:
                idf[term.lower()] = np.log(n_docs / df)
            else:
                idf[term.lower()] = 0.0

        return idf

    def _score_categorical_vagueness(self, text: str, tokens: List[str]) -> float:
        """
        Component (1): Categorical Vagueness → S_cat ∈ [0, 100]

        Measures reliance on abstract category terms.

        Parameters
        ----------
        text : str
            Preprocessed text
        tokens : list[str]
            Tokenized text

        Returns
        -------
        float
            S_cat score in [0, 100]
        """
        token_count = len(tokens)
        if token_count == 0:
            return 0.0

        # Find all abstract term matches
        matches = self._abstract_pattern.findall(text)

        if not matches:
            return 0.0

        # Count abstract terms
        if self.use_idf and self._fitted:
            # Weight by IDF
            weighted_count = sum(
                self._idf_weights.get(match.lower(), 1.0)
                for match in matches
            )
            # Normalize by mean IDF to keep scale consistent
            mean_idf = np.mean(list(self._idf_weights.values())) if self._idf_weights else 1.0
            if mean_idf > 0:
                count_abstract = weighted_count / mean_idf
            else:
                count_abstract = len(matches)
        else:
            count_abstract = len(matches)

        # Score with scaling factor α
        # Tuned so marketing-heavy → 60-80, technical → 20-40
        # For marketing with ~40% abstract terms: 100 * 0.4 * α = 70 → α ≈ 1.75
        alpha = 2.3  # Scaling constant

        score = 100 * (count_abstract / max(1, token_count)) * alpha

        # Clip to [0, 100]
        return min(100.0, max(0.0, score))

    def _score_concreteness_deficit(self, text: str, tokens: List[str]) -> float:
        """
        Component (2): Concreteness Deficit → S_concdef ∈ [0, 100]

        Penalizes absence of specifics (numbers, dates, versions, units, benchmarks).

        Parameters
        ----------
        text : str
            Preprocessed text
        tokens : list[str]
            Tokenized text

        Returns
        -------
        float
            S_concdef score in [0, 100]
        """
        token_count = max(1, len(tokens))

        # Feature 1: Numbers or percentages
        has_number = bool(re.search(r'\d+(\.\d+)?%?', text))
        number_density = len(re.findall(r'\d+(\.\d+)?%?', text)) / (token_count / 100)

        # Feature 2: Dates, quarters, years
        has_date = bool(re.search(
            r'\b(20\d{2}|q[1-4]\s*20\d{2}|january|february|march|april|may|june|'
            r'july|august|september|october|november|december)\b',
            text, re.IGNORECASE
        ))
        date_density = len(re.findall(
            r'\b(20\d{2}|q[1-4]\s*20\d{2}|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\b',
            text, re.IGNORECASE
        )) / (token_count / 100)

        # Feature 3: Versions or releases
        has_version = bool(re.search(
            r'\bv\d+(\.\d+){0,3}\b|version\s+\d+|release\s+\d+|sdk\s+v?\d+|api\s+v?\d+',
            text, re.IGNORECASE
        ))

        # Feature 4: Units and specs
        unit_pattern = (
            r'\b\d+\s*(nm|ghz|mhz|kw|mw|w|ms|μs|ns|gb|tb|mb|kb|kwh|mwh|'
            r'tops|flops|gflops|tflops|μm|mm|cm|m|km|mpa|gpa|kpa|pa|'
            r'hz|v|a|ma|μa|°c|°f|k|mol|cd|lm|lx|db|dbi|ppm|ppb|%|'
            r'cri|coherence|qubit|qubits|error\s+rate|fidelity)\b'
        )
        has_units = bool(re.search(unit_pattern, text, re.IGNORECASE))
        unit_density = len(re.findall(unit_pattern, text, re.IGNORECASE)) / (token_count / 100)

        # Feature 5: Benchmarks, publications, named clients
        benchmark_pattern = (
            r'\b(benchmark|published|nature|science|ieee|arxiv|acm|'
            r'customer|client|partner|pilot|deployment|production)\b'
        )
        has_benchmark = bool(re.search(benchmark_pattern, text, re.IGNORECASE))

        # Named entities (capitalized bigrams as proxy for companies/products)
        named_entities = re.findall(r'\b[A-Z][a-z]+\s+[A-Z][a-z]+\b', text)
        has_named = len(named_entities) > 0

        # Weighted combination of features
        # Use density-based squashing: 1 - exp(-density)
        w1, w2, w3, w4, w5 = 0.25, 0.20, 0.15, 0.25, 0.15

        evidence_1 = 1 - np.exp(-number_density * 0.5) if number_density > 0 else 0
        evidence_2 = 1 - np.exp(-date_density * 0.8) if date_density > 0 else 0
        evidence_3 = float(has_version)
        evidence_4 = 1 - np.exp(-unit_density * 0.6) if unit_density > 0 else 0
        evidence_5 = float(has_benchmark or has_named)

        specificity_evidence = (
            w1 * evidence_1 +
            w2 * evidence_2 +
            w3 * evidence_3 +
            w4 * evidence_4 +
            w5 * evidence_5
        )

        # Concreteness deficit is inverse of specificity
        s_concdef = 100 * (1 - specificity_evidence)

        # Clip to [0, 100]
        return min(100.0, max(0.0, s_concdef))

    def _aggregate_v_raw(self, s_cat: float, s_concdef: float) -> float:
        """
        Aggregate S_cat and S_concdef into V_raw using max-mean hybrid.

        V_raw = 0.5 * max(S_cat, S_concdef) + 0.5 * mean(S_cat, S_concdef)

        Rationale: Preserves extreme signals when either component is very high.

        Parameters
        ----------
        s_cat : float
            Categorical vagueness score
        s_concdef : float
            Concreteness deficit score

        Returns
        -------
        float
            V_raw score in [0, 100]
        """
        mean_val = 0.5 * (s_cat + s_concdef)
        max_val = max(s_cat, s_concdef)
        v_raw = 0.5 * max_val + 0.5 * mean_val
        return v_raw

    def fit(
        self,
        texts: List[str],
        y: Optional[pd.Series] = None,
        group_cols: Optional[pd.DataFrame] = None
    ):
        """
        Fit the scorer on a corpus (compute IDF weights if enabled).

        Parameters
        ----------
        texts : list[str]
            Input texts
        y : pd.Series, optional
            Ignored (for sklearn compatibility)
        group_cols : pd.DataFrame, optional
            Group columns for within-group percentile computation

        Returns
        -------
        self
        """
        # Preprocess all texts
        preprocessed = [self._preprocess(text) for text in texts]

        # Compute IDF weights if enabled
        if self.use_idf:
            self._idf_weights = self._compute_idf(preprocessed)

        self._fitted = True
        return self

    def transform(
        self,
        texts: List[str],
        group_cols: Optional[pd.DataFrame] = None
    ) -> pd.DataFrame:
        """
        Transform texts into vagueness scores.

        Parameters
        ----------
        texts : list[str]
            Input texts
        group_cols : pd.DataFrame, optional
            Group columns for within-group percentile computation

        Returns
        -------
        pd.DataFrame
            Columns: S_cat, S_concdef, V_raw, V_pct, V_minmax
        """
        results = []

        for text in texts:
            # Preprocess and tokenize
            preprocessed = self._preprocess(text)
            tokens = self._tokenize(preprocessed)

            # Compute components
            s_cat = self._score_categorical_vagueness(preprocessed, tokens)
            s_concdef = self._score_concreteness_deficit(preprocessed, tokens)

            # Aggregate
            v_raw = self._aggregate_v_raw(s_cat, s_concdef)

            results.append({
                'S_cat': s_cat,
                'S_concdef': s_concdef,
                'V_raw': v_raw
            })

        df = pd.DataFrame(results)

        # Compute percentiles
        if group_cols is not None and self.groupby_cols:
            # Within-group percentiles
            combined = pd.concat([group_cols.reset_index(drop=True), df], axis=1)
            combined['V_pct'] = combined.groupby(self.groupby_cols)['V_raw'].rank(pct=True) * 100
            df['V_pct'] = combined['V_pct']
        else:
            # Global percentiles
            df['V_pct'] = df['V_raw'].rank(pct=True) * 100

        # Compute min-max normalization
        v_min = df['V_raw'].min()
        v_max = df['V_raw'].max()
        if v_max > v_min:
            df['V_minmax'] = 100 * (df['V_raw'] - v_min) / (v_max - v_min)
        else:
            df['V_minmax'] = 50.0  # All same value

        return df

    def fit_transform(
        self,
        texts: List[str],
        y: Optional[pd.Series] = None,
        group_cols: Optional[pd.DataFrame] = None
    ) -> pd.DataFrame:
        """
        Fit and transform in one step.

        Parameters
        ----------
        texts : list[str]
            Input texts
        y : pd.Series, optional
            Ignored (for sklearn compatibility)
        group_cols : pd.DataFrame, optional
            Group columns for within-group percentile computation

        Returns
        -------
        pd.DataFrame
            Columns: S_cat, S_concdef, V_raw, V_pct, V_minmax
        """
        self.fit(texts, y, group_cols)
        return self.transform(texts, group_cols)


# Backward compatibility shim
class StrategicVaguenessScorer(StrategicVaguenessScorerV2):
    """
    Deprecated: Use StrategicVaguenessScorerV2 instead.

    This is a compatibility shim. The lexical-uncertainty component has been
    removed per research spec p.25-26. Vagueness is now computed using only
    two components: Categorical Vagueness and Concreteness Deficit.
    """

    def __init__(self, *args, **kwargs):
        warnings.warn(
            "StrategicVaguenessScorer is deprecated. "
            "Lexical uncertainty component has been removed; "
            "using two-component V (Categorical Vagueness + Concreteness Deficit). "
            "Please use StrategicVaguenessScorerV2 directly.",
            DeprecationWarning,
            stacklevel=2
        )
        super().__init__(*args, **kwargs)


# Convenience function for backward compatibility with features.py
def compute_vagueness_vectorized_v2(descriptions: pd.Series, keywords: pd.Series) -> pd.Series:
    """
    Vectorized wrapper for StrategicVaguenessScorerV2.

    Returns V_raw scores (0-100 scale) compatible with V1 interface.

    Parameters
    ----------
    descriptions : pd.Series
        Company descriptions
    keywords : pd.Series
        Company keywords

    Returns
    -------
    pd.Series
        V_raw vagueness scores (0-100)
    """
    # Combine description and keywords
    texts = (descriptions.fillna('') + ' ' + keywords.fillna('')).tolist()

    # Initialize scorer
    scorer = StrategicVaguenessScorerV2(use_idf=True)

    # Fit and transform
    scorer.fit(texts)
    results = scorer.transform(texts)

    # Return V_raw as Series with original index
    return pd.Series(results['V_raw'].values, index=descriptions.index)
