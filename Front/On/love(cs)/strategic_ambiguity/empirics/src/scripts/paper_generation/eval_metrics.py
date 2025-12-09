#!/usr/bin/env python3
"""
Department별 Evaluation Metric — 김완 🐙 평가 도구
Evaluation Metrics for P1/P2/P3 across Journal Departments

=============================================================================
전라좌수군 견리사의 군령 — 나대용 🐅 설계, 김완 🐙 사용
=============================================================================

김완 확정 공식:
    MS_Fit_Score = (Rigor + Surprise) - Complexity
    - 각 1-5점
    - 총점 10점 만점
    - 7점 미만 = Reject Risk ⚠️

Department별 가중치:
    | Dept     | Rigor | Surprise | Complexity |
    |----------|-------|----------|------------|
    | E&I      | 1.0   | 1.2      | 1.0        |
    | Strategy | 1.2   | 1.0      | 0.8        |
    | OM       | 1.3   | 0.9      | 1.0        |

Background:
    P1, P2, P3를 각각 Management Science journal의 다른 Department에 병렬 투고:
    - P1 ✌️ U-Shape → E&I (Entrepreneurship & Innovation)
    - P2 🦾 Competency Trap → Business Strategy
    - P3 🤹 Execution Gap → Operations Management

Usage:
    python eval_metrics.py                          # Show all criteria
    python eval_metrics.py --score P1 4 5 3        # Score P1: rigor=4, surprise=5, complexity=3
    python eval_metrics.py --compare               # Side-by-side comparison
    python eval_metrics.py --checklist             # Generate empty checklist
    python eval_metrics.py --test                  # Run tests
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Union
from datetime import datetime
import json
import argparse

# ============================================================================
# CONFIGURATION
# ============================================================================

OUTPUT_DIR = Path(__file__).parent / "output"
REJECT_THRESHOLD = 7.0  # 7점 미만 = Reject Risk

# Paper Configuration
PAPERS = {
    "P1": {
        "emoji": "✌️",
        "title": "U-Shape: When Vagueness Pays",
        "target_dept": "E&I",
        "domain": "Technology"
    },
    "P2": {
        "emoji": "🦾",
        "title": "Competency Trap: When Success Kills Options",
        "target_dept": "Strategy",
        "domain": "Organization"
    },
    "P3": {
        "emoji": "🤹",
        "title": "Execution Gap: Optimal Number of Options",
        "target_dept": "OM",
        "domain": "Competition"
    }
}

# ============================================================================
# 김완 확정 공식: MS_Fit_Score = (Rigor + Surprise) - Complexity
# ============================================================================

@dataclass
class DeptWeights:
    """Department-specific weights for scoring"""
    rigor: float
    surprise: float
    complexity: float

    def weighted_score(self, rigor: float, surprise: float, complexity: float) -> float:
        """
        Calculate weighted MS_Fit_Score

        Formula: (Rigor * w_r + Surprise * w_s) - (Complexity * w_c)
        """
        weighted_rigor = rigor * self.rigor
        weighted_surprise = surprise * self.surprise
        weighted_complexity = complexity * self.complexity

        return (weighted_rigor + weighted_surprise) - weighted_complexity


# Department별 가중치
DEPT_WEIGHTS = {
    "E&I": DeptWeights(rigor=1.0, surprise=1.2, complexity=1.0),
    "Strategy": DeptWeights(rigor=1.2, surprise=1.0, complexity=0.8),
    "OM": DeptWeights(rigor=1.3, surprise=0.9, complexity=1.0),
}


# ============================================================================
# CORE SCORING FUNCTIONS
# ============================================================================

def score_paper(paper_id: str, dept: str, rigor: float, surprise: float,
                complexity: float) -> float:
    """
    Calculate MS_Fit_Score for a paper

    Args:
        paper_id: P1, P2, or P3
        dept: E&I, Strategy, or OM
        rigor: 1-5 score for methodological rigor
        surprise: 1-5 score for novel/surprising findings
        complexity: 1-5 score for unnecessary complexity

    Returns:
        Weighted MS_Fit_Score (max ~10, min ~-3)

    Raises:
        ValueError: If scores are out of range or dept unknown
    """
    # Validate inputs
    for name, val in [("rigor", rigor), ("surprise", surprise), ("complexity", complexity)]:
        if not 1 <= val <= 5:
            raise ValueError(f"{name} must be between 1 and 5, got {val}")

    if dept not in DEPT_WEIGHTS:
        raise ValueError(f"Unknown department: {dept}. Choose from {list(DEPT_WEIGHTS.keys())}")

    weights = DEPT_WEIGHTS[dept]
    return weights.weighted_score(rigor, surprise, complexity)


def alert_reject_risk(score: float) -> bool:
    """
    Check if score indicates reject risk

    Args:
        score: MS_Fit_Score

    Returns:
        True if score < 7 (reject risk), False otherwise
    """
    return score < REJECT_THRESHOLD


def get_score_interpretation(score: float) -> Tuple[str, str]:
    """
    Interpret score with emoji and description

    Returns:
        (emoji, description)
    """
    if score >= 9:
        return "🌟", "Excellent - Strong Accept"
    elif score >= 8:
        return "✅", "Good - Accept with Minor Revisions"
    elif score >= 7:
        return "🟡", "Borderline - Major Revisions Likely"
    elif score >= 5:
        return "⚠️", "REJECT RISK - Significant Issues"
    else:
        return "🔴", "HIGH REJECT RISK - Fundamental Problems"


# ============================================================================
# PAPER SCORE DATA STRUCTURE
# ============================================================================

@dataclass
class PaperScore:
    """Complete score for one paper"""
    paper_id: str
    dept: str
    rigor: float
    surprise: float
    complexity: float
    notes: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    @property
    def ms_fit_score(self) -> float:
        """Calculate MS_Fit_Score"""
        return score_paper(self.paper_id, self.dept, self.rigor,
                          self.surprise, self.complexity)

    @property
    def reject_risk(self) -> bool:
        """Check reject risk"""
        return alert_reject_risk(self.ms_fit_score)

    @property
    def interpretation(self) -> Tuple[str, str]:
        """Get score interpretation"""
        return get_score_interpretation(self.ms_fit_score)

    def to_dict(self) -> dict:
        emoji, desc = self.interpretation
        return {
            "paper_id": self.paper_id,
            "dept": self.dept,
            "rigor": self.rigor,
            "surprise": self.surprise,
            "complexity": self.complexity,
            "ms_fit_score": round(self.ms_fit_score, 2),
            "reject_risk": self.reject_risk,
            "interpretation": desc,
            "notes": self.notes,
            "timestamp": self.timestamp
        }


# ============================================================================
# COMPARISON FUNCTIONS
# ============================================================================

def compare_papers(scores: Dict[str, PaperScore]) -> str:
    """
    Generate side-by-side comparison of papers

    Args:
        scores: Dict mapping paper_id to PaperScore

    Returns:
        Formatted comparison table string
    """
    if not scores:
        return "No scores to compare"

    # Header
    lines = [
        "=" * 80,
        "📊 MS_Fit_Score 병렬 비교 — (Rigor + Surprise) - Complexity",
        "=" * 80,
        "",
        f"{'Metric':<20} {'P1 ✌️ (E&I)':<20} {'P2 🦾 (Strategy)':<20} {'P3 🤹 (OM)':<20}",
        "-" * 80,
    ]

    # Get scores for each paper
    def get_val(paper_id: str, attr: str) -> str:
        if paper_id in scores:
            val = getattr(scores[paper_id], attr)
            if isinstance(val, float):
                return f"{val:.1f}"
            return str(val)
        return "N/A"

    # Rows
    metrics = [
        ("Rigor (R)", "rigor"),
        ("Surprise (S)", "surprise"),
        ("Complexity (C)", "complexity"),
    ]

    for label, attr in metrics:
        p1 = get_val("P1", attr)
        p2 = get_val("P2", attr)
        p3 = get_val("P3", attr)
        lines.append(f"{label:<20} {p1:<20} {p2:<20} {p3:<20}")

    lines.append("-" * 80)

    # MS_Fit_Score row
    def get_score_str(paper_id: str) -> str:
        if paper_id in scores:
            score = scores[paper_id].ms_fit_score
            emoji, _ = get_score_interpretation(score)
            return f"{score:.2f} {emoji}"
        return "N/A"

    lines.append(f"{'MS_Fit_Score':<20} {get_score_str('P1'):<20} {get_score_str('P2'):<20} {get_score_str('P3'):<20}")

    # Reject Risk row
    def get_risk_str(paper_id: str) -> str:
        if paper_id in scores:
            risk = scores[paper_id].reject_risk
            return "⚠️ YES" if risk else "✅ NO"
        return "N/A"

    lines.append(f"{'Reject Risk (<7)':<20} {get_risk_str('P1'):<20} {get_risk_str('P2'):<20} {get_risk_str('P3'):<20}")

    lines.append("=" * 80)

    # Summary
    scored = [s for s in scores.values()]
    if scored:
        best = max(scored, key=lambda s: s.ms_fit_score)
        worst = min(scored, key=lambda s: s.ms_fit_score)
        lines.append(f"\n🏆 Best: {best.paper_id} ({best.ms_fit_score:.2f})")
        if worst.reject_risk:
            lines.append(f"⚠️ At Risk: {worst.paper_id} ({worst.ms_fit_score:.2f})")

    return "\n".join(lines)


def compare_papers_dataframe(scores: Dict[str, PaperScore]):
    """
    Generate DataFrame for comparison (if pandas available)

    Returns:
        pandas.DataFrame or dict if pandas not available
    """
    data = {
        "Paper": [],
        "Dept": [],
        "Rigor": [],
        "Surprise": [],
        "Complexity": [],
        "MS_Fit_Score": [],
        "Reject_Risk": [],
    }

    for paper_id in ["P1", "P2", "P3"]:
        if paper_id in scores:
            s = scores[paper_id]
            data["Paper"].append(f"{paper_id} {PAPERS[paper_id]['emoji']}")
            data["Dept"].append(s.dept)
            data["Rigor"].append(s.rigor)
            data["Surprise"].append(s.surprise)
            data["Complexity"].append(s.complexity)
            data["MS_Fit_Score"].append(round(s.ms_fit_score, 2))
            data["Reject_Risk"].append(s.reject_risk)

    try:
        import pandas as pd
        return pd.DataFrame(data)
    except ImportError:
        return data


# ============================================================================
# CHECKLIST GENERATION
# ============================================================================

def generate_checklist(paper_id: Optional[str] = None) -> str:
    """Generate scoring checklist for Kim-wan"""
    lines = [
        "=" * 70,
        "📝 김완 🐙 채점표 — MS_Fit_Score = (R + S) - C",
        "=" * 70,
        "",
        "공식: MS_Fit_Score = (Rigor × w_r + Surprise × w_s) - (Complexity × w_c)",
        "기준: 7점 미만 = Reject Risk ⚠️",
        "",
        "Department 가중치:",
        "| Dept     | Rigor (w_r) | Surprise (w_s) | Complexity (w_c) |",
        "|----------|-------------|----------------|------------------|",
        "| E&I      | 1.0         | 1.2            | 1.0              |",
        "| Strategy | 1.2         | 1.0            | 0.8              |",
        "| OM       | 1.3         | 0.9            | 1.0              |",
        "",
    ]

    papers_to_check = [paper_id] if paper_id else list(PAPERS.keys())

    for pid in papers_to_check:
        paper = PAPERS[pid]
        lines.extend([
            "-" * 70,
            f"### {pid} {paper['emoji']}: {paper['title']}",
            f"Target: {paper['target_dept']} | Domain: {paper['domain']}",
            "",
            "| Criterion   | Score (1-5) | Notes |",
            "|-------------|-------------|-------|",
            "| Rigor (R)   | [ ]         |       |",
            "| Surprise (S)| [ ]         |       |",
            "| Complexity (C)| [ ]       |       |",
            "",
            "MS_Fit_Score = (R + S) - C = ___",
            "Reject Risk: [ ] Yes  [ ] No",
            "",
        ])

    return "\n".join(lines)


# ============================================================================
# TESTS
# ============================================================================

def run_tests() -> bool:
    """
    Run unit tests for scoring functions

    Returns:
        True if all tests pass
    """
    print("=" * 60)
    print("🧪 eval_metrics.py 테스트 — 나대용 🐅")
    print("=" * 60)

    all_passed = True
    tests_run = 0
    tests_passed = 0

    def test(name: str, condition: bool, msg: str = ""):
        nonlocal all_passed, tests_run, tests_passed
        tests_run += 1
        if condition:
            tests_passed += 1
            print(f"  ✅ {name}")
        else:
            all_passed = False
            print(f"  ❌ {name}: {msg}")

    # Test 1: Basic scoring
    print("\n📋 Test 1: Basic Scoring")
    score = score_paper("P1", "E&I", rigor=4, surprise=5, complexity=3)
    # E&I weights: R=1.0, S=1.2, C=1.0
    # Expected: (4*1.0 + 5*1.2) - 3*1.0 = 4 + 6 - 3 = 7
    test("E&I basic score", abs(score - 7.0) < 0.01, f"Expected 7.0, got {score}")

    # Test 2: Strategy weights
    score2 = score_paper("P2", "Strategy", rigor=4, surprise=5, complexity=3)
    # Strategy weights: R=1.2, S=1.0, C=0.8
    # Expected: (4*1.2 + 5*1.0) - 3*0.8 = 4.8 + 5 - 2.4 = 7.4
    test("Strategy weighted score", abs(score2 - 7.4) < 0.01, f"Expected 7.4, got {score2}")

    # Test 3: OM weights
    score3 = score_paper("P3", "OM", rigor=4, surprise=5, complexity=3)
    # OM weights: R=1.3, S=0.9, C=1.0
    # Expected: (4*1.3 + 5*0.9) - 3*1.0 = 5.2 + 4.5 - 3 = 6.7
    test("OM weighted score", abs(score3 - 6.7) < 0.01, f"Expected 6.7, got {score3}")

    # Test 4: Reject risk threshold
    print("\n📋 Test 2: Reject Risk Detection")
    test("Score 6.9 = reject risk", alert_reject_risk(6.9) == True)
    test("Score 7.0 = no reject risk", alert_reject_risk(7.0) == False)
    test("Score 7.1 = no reject risk", alert_reject_risk(7.1) == False)

    # Test 5: Score interpretation
    print("\n📋 Test 3: Score Interpretation")
    emoji, _ = get_score_interpretation(9.5)
    test("Score 9.5 = 🌟", emoji == "🌟")
    emoji, _ = get_score_interpretation(8.0)
    test("Score 8.0 = ✅", emoji == "✅")
    emoji, _ = get_score_interpretation(6.0)
    test("Score 6.0 = ⚠️", emoji == "⚠️")

    # Test 6: Input validation
    print("\n📋 Test 4: Input Validation")
    try:
        score_paper("P1", "E&I", rigor=6, surprise=3, complexity=2)
        test("Rigor > 5 raises error", False, "Should have raised ValueError")
    except ValueError:
        test("Rigor > 5 raises error", True)

    try:
        score_paper("P1", "E&I", rigor=0, surprise=3, complexity=2)
        test("Rigor < 1 raises error", False, "Should have raised ValueError")
    except ValueError:
        test("Rigor < 1 raises error", True)

    try:
        score_paper("P1", "Unknown", rigor=3, surprise=3, complexity=2)
        test("Unknown dept raises error", False, "Should have raised ValueError")
    except ValueError:
        test("Unknown dept raises error", True)

    # Test 7: PaperScore dataclass
    print("\n📋 Test 5: PaperScore Dataclass")
    ps = PaperScore(paper_id="P1", dept="E&I", rigor=5, surprise=5, complexity=2)
    # Expected: (5*1.0 + 5*1.2) - 2*1.0 = 5 + 6 - 2 = 9
    test("PaperScore ms_fit_score", abs(ps.ms_fit_score - 9.0) < 0.01)
    test("PaperScore no reject risk at 9.0", ps.reject_risk == False)

    ps2 = PaperScore(paper_id="P2", dept="Strategy", rigor=2, surprise=3, complexity=4)
    # Expected: (2*1.2 + 3*1.0) - 4*0.8 = 2.4 + 3 - 3.2 = 2.2
    test("Low score = reject risk", ps2.reject_risk == True)

    # Test 8: Comparison
    print("\n📋 Test 6: Comparison Function")
    scores = {
        "P1": PaperScore("P1", "E&I", 4, 4, 2),
        "P2": PaperScore("P2", "Strategy", 3, 3, 3),
    }
    comparison = compare_papers(scores)
    test("Comparison contains P1", "P1" in comparison)
    test("Comparison contains header", "MS_Fit_Score" in comparison)

    # Summary
    print("\n" + "=" * 60)
    print(f"📊 Results: {tests_passed}/{tests_run} tests passed")
    if all_passed:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed")
    print("=" * 60)

    return all_passed


# ============================================================================
# CLI DISPLAY FUNCTIONS
# ============================================================================

def print_banner():
    """Print evaluation banner"""
    print("=" * 80)
    print("🇰🇷 전라좌수군 견리사의 군령 — MS_Fit_Score 평가 시스템")
    print("=" * 80)
    print("김완 🐙 | 義 (비판적 검증)")
    print("공식: MS_Fit_Score = (Rigor + Surprise) - Complexity")
    print("기준: 7점 미만 = Reject Risk ⚠️")
    print("-" * 80)


def display_single_score(paper_id: str, dept: str, rigor: float,
                        surprise: float, complexity: float):
    """Display score for a single paper"""
    print_banner()

    paper = PAPERS.get(paper_id, {})
    score = score_paper(paper_id, dept, rigor, surprise, complexity)
    emoji, desc = get_score_interpretation(score)
    risk = alert_reject_risk(score)

    weights = DEPT_WEIGHTS[dept]

    print(f"\n### {paper_id} {paper.get('emoji', '')} — {paper.get('title', '')}")
    print(f"Department: {dept}")
    print()
    print(f"Raw Scores:")
    print(f"  Rigor (R):      {rigor}/5  × {weights.rigor} = {rigor * weights.rigor:.1f}")
    print(f"  Surprise (S):   {surprise}/5  × {weights.surprise} = {surprise * weights.surprise:.1f}")
    print(f"  Complexity (C): {complexity}/5  × {weights.complexity} = {complexity * weights.complexity:.1f}")
    print()
    print(f"MS_Fit_Score = ({rigor * weights.rigor:.1f} + {surprise * weights.surprise:.1f}) - {complexity * weights.complexity:.1f}")
    print(f"             = {score:.2f}")
    print()
    print(f"{emoji} {desc}")
    if risk:
        print(f"⚠️ REJECT RISK: Score below 7.0 threshold")
    print()


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="🇰🇷 전라좌수군 MS_Fit_Score 평가 시스템",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
공식: MS_Fit_Score = (Rigor × w_r + Surprise × w_s) - (Complexity × w_c)
기준: 7점 미만 = Reject Risk ⚠️

Examples:
    python eval_metrics.py                          # Show formula & weights
    python eval_metrics.py --score P1 4 5 3        # Score P1: R=4, S=5, C=3
    python eval_metrics.py --compare               # Compare all papers
    python eval_metrics.py --checklist             # Generate blank checklist
    python eval_metrics.py --checklist P2          # Checklist for P2 only
    python eval_metrics.py --test                  # Run unit tests
        """
    )

    parser.add_argument(
        '--score', '-s',
        nargs=4,
        metavar=('PAPER', 'R', 'S', 'C'),
        help='Score a paper: paper_id rigor surprise complexity'
    )
    parser.add_argument(
        '--compare', '-c',
        action='store_true',
        help='Compare all papers (interactive)'
    )
    parser.add_argument(
        '--checklist', '-l',
        nargs='?',
        const='ALL',
        help='Generate checklist (optionally for specific paper)'
    )
    parser.add_argument(
        '--test', '-t',
        action='store_true',
        help='Run unit tests'
    )
    parser.add_argument(
        '--formula', '-f',
        action='store_true',
        help='Show formula and weights'
    )

    args = parser.parse_args()

    if args.test:
        success = run_tests()
        return 0 if success else 1

    elif args.score:
        paper_id = args.score[0].upper()
        if paper_id not in PAPERS:
            print(f"Unknown paper: {paper_id}. Choose from P1, P2, P3")
            return 1

        try:
            rigor = float(args.score[1])
            surprise = float(args.score[2])
            complexity = float(args.score[3])
        except ValueError:
            print("Scores must be numbers between 1-5")
            return 1

        dept = PAPERS[paper_id]["target_dept"]
        display_single_score(paper_id, dept, rigor, surprise, complexity)

    elif args.compare:
        print_banner()
        print("\n📊 Enter scores for each paper (1-5 for each):\n")

        scores = {}
        for paper_id in ["P1", "P2", "P3"]:
            paper = PAPERS[paper_id]
            dept = paper["target_dept"]
            print(f"\n{paper_id} {paper['emoji']} ({dept}):")
            try:
                r = float(input("  Rigor (1-5): ") or "0")
                s = float(input("  Surprise (1-5): ") or "0")
                c = float(input("  Complexity (1-5): ") or "0")
                if 1 <= r <= 5 and 1 <= s <= 5 and 1 <= c <= 5:
                    scores[paper_id] = PaperScore(paper_id, dept, r, s, c)
            except (ValueError, KeyboardInterrupt):
                pass

        print("\n" + compare_papers(scores))

    elif args.checklist:
        paper_id = args.checklist if args.checklist != 'ALL' else None
        print(generate_checklist(paper_id))

    else:
        # Default: show formula and weights
        print_banner()
        print("""
📐 김완 확정 공식:

    MS_Fit_Score = (Rigor × w_r + Surprise × w_s) - (Complexity × w_c)

📊 Department별 가중치:

    | Dept     | Rigor (w_r) | Surprise (w_s) | Complexity (w_c) |
    |----------|-------------|----------------|------------------|
    | E&I      | 1.0         | 1.2            | 1.0              |
    | Strategy | 1.2         | 1.0            | 0.8              |
    | OM       | 1.3         | 0.9            | 1.0              |

📏 해석 기준:

    Score ≥ 9.0  →  🌟 Excellent (Strong Accept)
    Score ≥ 8.0  →  ✅ Good (Accept with Minor Revisions)
    Score ≥ 7.0  →  🟡 Borderline (Major Revisions Likely)
    Score < 7.0  →  ⚠️ REJECT RISK

🎯 예시:

    P1 (E&I): Rigor=4, Surprise=5, Complexity=3
    → (4×1.0 + 5×1.2) - 3×1.0 = 4 + 6 - 3 = 7.0 🟡

    P2 (Strategy): Rigor=4, Surprise=5, Complexity=3
    → (4×1.2 + 5×1.0) - 3×0.8 = 4.8 + 5 - 2.4 = 7.4 ✅

    P3 (OM): Rigor=4, Surprise=5, Complexity=3
    → (4×1.3 + 5×0.9) - 3×1.0 = 5.2 + 4.5 - 3 = 6.7 ⚠️

─────────────────────────────────────────────────────────────
Usage:
    --score P1 4 5 3    # Score paper P1
    --compare           # Interactive comparison
    --checklist         # Generate blank checklist
    --test              # Run unit tests
""")

    return 0


if __name__ == "__main__":
    exit(main())
