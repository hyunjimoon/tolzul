#!/usr/bin/env python3
"""
Paper Magnet — 논문 자석 검색 시스템
Searches relevant papers from the paper database based on theoretical resonance

The "magnet" metaphor: Given our theory (P1/P2/P3), find papers with the
strongest attraction — measured by how much their pairing resonates with
Scott (commitment) and Charlie (flexibility).

=============================================================================
전라좌수군 견리사의 군령 — 문헌 탐색 시스템
=============================================================================

Usage:
    python paper_magnet.py                    # Show all resonant papers
    python paper_magnet.py --paper P1         # Papers for P1 (U-Shape)
    python paper_magnet.py --paper P2         # Papers for P2 (Competency Trap)
    python paper_magnet.py --paper P3         # Papers for P3 (Execution Gap)
    python paper_magnet.py --keyword "option" # Search by keyword
    python paper_magnet.py --top 10           # Show top 10 most resonant
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional
import re
import argparse

# ============================================================================
# CONFIGURATION
# ============================================================================

PAPER_DATABASE = Path("/Users/hyunjimoon/tolzul/Space/Library/1논문용")

# Scott's commitment keywords (Stern — "Just Choose!")
SCOTT_KEYWORDS = [
    "commitment", "lock-in", "sunk cost", "irreversible", "specificity",
    "focus", "exploitation", "efficiency", "optimization", "scale",
    "concrete", "decision", "choice", "bet", "all-in", "concentration",
    "specialization", "dedication", "investment", "resource allocation"
]

# Charlie's flexibility keywords (Fine — "Is it feasible?")
CHARLIE_KEYWORDS = [
    "flexibility", "option", "pivot", "adapt", "experiment", "explore",
    "uncertainty", "ambiguity", "vagueness", "modularity", "real option",
    "learning", "iteration", "agile", "dynamic", "reversible", "hedge",
    "portfolio", "diversification", "optionality", "discovery"
]

# Paper-specific keyword sets
PAPER_KEYWORDS = {
    "P1": {
        "primary": ["vagueness", "ambiguity", "signal", "communication", "modularity",
                   "u-shape", "convex", "non-linear", "curvilinear"],
        "secondary": ["survival", "funding", "venture", "startup", "entrepreneur",
                     "information asymmetry", "adverse selection", "cheap talk"]
    },
    "P2": {
        "primary": ["competency trap", "core rigidity", "success trap", "commitment trap",
                   "path dependence", "lock-in", "exploitation", "replacement effect"],
        "secondary": ["capability", "learning", "bayesian", "belief", "pivot",
                     "paradigm shift", "disruption", "incumbent"]
    },
    "P3": {
        "primary": ["newsvendor", "portfolio", "option count", "coordination",
                   "clockspeed", "dependency", "execution gap"],
        "secondary": ["commitment cost", "flexibility cost", "trade-off", "operations",
                     "capacity", "inventory", "timing", "entry"]
    }
}


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class PaperResonance:
    """Resonance score for a paper"""
    filename: str
    title: str
    scott_score: float = 0.0  # Commitment resonance
    charlie_score: float = 0.0  # Flexibility resonance
    p1_score: float = 0.0
    p2_score: float = 0.0
    p3_score: float = 0.0
    keywords_found: List[str] = field(default_factory=list)

    @property
    def total_resonance(self) -> float:
        """Total theoretical resonance"""
        return self.scott_score + self.charlie_score

    @property
    def balance(self) -> str:
        """Scott-Charlie balance indicator"""
        if self.scott_score > self.charlie_score * 1.5:
            return "⚡ Scott-heavy (Commitment)"
        elif self.charlie_score > self.scott_score * 1.5:
            return "🌊 Charlie-heavy (Flexibility)"
        else:
            return "⚖️ Balanced (Tension)"

    @property
    def best_paper_fit(self) -> str:
        """Which paper (P1/P2/P3) this resonates with most"""
        scores = {"P1": self.p1_score, "P2": self.p2_score, "P3": self.p3_score}
        best = max(scores, key=scores.get)
        if scores[best] == 0:
            return "General"
        return best


# ============================================================================
# PAPER SCANNING
# ============================================================================

def extract_title_from_filename(filename: str) -> str:
    """Extract readable title from filename"""
    # Remove emoji prefix and .md extension
    title = re.sub(r'^📜|^📝', '', filename)
    title = title.replace('.md', '')
    # Replace underscores with spaces
    title = title.replace('_', ' ')
    return title


def scan_paper_content(filepath: Path) -> str:
    """Read paper content for keyword analysis"""
    try:
        content = filepath.read_text(encoding='utf-8')
        return content.lower()
    except Exception as e:
        return ""


def calculate_keyword_score(content: str, keywords: List[str]) -> Tuple[float, List[str]]:
    """Calculate keyword presence score and return found keywords"""
    found = []
    score = 0.0

    for keyword in keywords:
        # Count occurrences (case insensitive)
        count = content.count(keyword.lower())
        if count > 0:
            found.append(keyword)
            # Diminishing returns for repeated keywords
            score += min(count, 5) * (1 / len(keyword.split()))  # Longer phrases worth more

    return score, found


def analyze_paper(filepath: Path) -> PaperResonance:
    """Analyze a single paper for theoretical resonance"""
    filename = filepath.name
    title = extract_title_from_filename(filename)
    content = scan_paper_content(filepath)

    # Calculate Scott (commitment) and Charlie (flexibility) scores
    scott_score, scott_found = calculate_keyword_score(content, SCOTT_KEYWORDS)
    charlie_score, charlie_found = calculate_keyword_score(content, CHARLIE_KEYWORDS)

    # Calculate paper-specific scores
    p1_primary, p1_found = calculate_keyword_score(content, PAPER_KEYWORDS["P1"]["primary"])
    p1_secondary, _ = calculate_keyword_score(content, PAPER_KEYWORDS["P1"]["secondary"])
    p1_score = p1_primary * 2 + p1_secondary

    p2_primary, p2_found = calculate_keyword_score(content, PAPER_KEYWORDS["P2"]["primary"])
    p2_secondary, _ = calculate_keyword_score(content, PAPER_KEYWORDS["P2"]["secondary"])
    p2_score = p2_primary * 2 + p2_secondary

    p3_primary, p3_found = calculate_keyword_score(content, PAPER_KEYWORDS["P3"]["primary"])
    p3_secondary, _ = calculate_keyword_score(content, PAPER_KEYWORDS["P3"]["secondary"])
    p3_score = p3_primary * 2 + p3_secondary

    all_found = list(set(scott_found + charlie_found + p1_found + p2_found + p3_found))

    return PaperResonance(
        filename=filename,
        title=title,
        scott_score=scott_score,
        charlie_score=charlie_score,
        p1_score=p1_score,
        p2_score=p2_score,
        p3_score=p3_score,
        keywords_found=all_found
    )


def scan_all_papers() -> List[PaperResonance]:
    """Scan all papers in the database"""
    papers = []

    for filepath in PAPER_DATABASE.glob("*.md"):
        if filepath.name.startswith("TEMPLATE"):
            continue
        resonance = analyze_paper(filepath)
        if resonance.total_resonance > 0:
            papers.append(resonance)

    return papers


# ============================================================================
# FILTERING AND SORTING
# ============================================================================

def filter_by_paper(papers: List[PaperResonance], paper_id: str) -> List[PaperResonance]:
    """Filter papers most relevant to P1, P2, or P3"""
    score_attr = f"{paper_id.lower()}_score"
    filtered = [p for p in papers if getattr(p, score_attr) > 0]
    return sorted(filtered, key=lambda p: getattr(p, score_attr), reverse=True)


def filter_by_keyword(papers: List[PaperResonance], keyword: str) -> List[PaperResonance]:
    """Filter papers containing specific keyword"""
    return [p for p in papers if keyword.lower() in ' '.join(p.keywords_found).lower()]


def get_top_resonant(papers: List[PaperResonance], n: int = 20) -> List[PaperResonance]:
    """Get top N most theoretically resonant papers"""
    return sorted(papers, key=lambda p: p.total_resonance, reverse=True)[:n]


# ============================================================================
# DISPLAY
# ============================================================================

def display_paper(paper: PaperResonance, rank: int = 0):
    """Display a single paper's resonance"""
    rank_str = f"#{rank} " if rank > 0 else ""
    print(f"\n{rank_str}📄 {paper.title}")
    print(f"   File: {paper.filename}")
    print(f"   Resonance: {paper.total_resonance:.1f} | {paper.balance}")
    print(f"   Scott/Charlie: {paper.scott_score:.1f} / {paper.charlie_score:.1f}")
    print(f"   Paper fit: P1={paper.p1_score:.1f}, P2={paper.p2_score:.1f}, P3={paper.p3_score:.1f} → Best: {paper.best_paper_fit}")
    if paper.keywords_found:
        keywords_display = ', '.join(paper.keywords_found[:8])
        if len(paper.keywords_found) > 8:
            keywords_display += f" (+{len(paper.keywords_found)-8} more)"
        print(f"   Keywords: {keywords_display}")


def display_papers_table(papers: List[PaperResonance], title: str = "Paper Resonance"):
    """Display papers in table format"""
    print("\n" + "=" * 80)
    print(f"🧲 {title}")
    print("=" * 80)

    # Header
    print(f"\n{'Rank':<5} {'Title':<40} {'Total':<8} {'Balance':<25} {'Best':<6}")
    print("-" * 80)

    for i, paper in enumerate(papers, 1):
        title_short = paper.title[:38] + ".." if len(paper.title) > 40 else paper.title
        print(f"{i:<5} {title_short:<40} {paper.total_resonance:<8.1f} {paper.balance:<25} {paper.best_paper_fit:<6}")


def display_paper_recommendations(paper_id: str, papers: List[PaperResonance]):
    """Display recommendations for a specific paper (P1/P2/P3)"""
    paper_names = {
        "P1": "✌️ U-Shape: When Vagueness Pays",
        "P2": "🦾 Competency Trap: When Success Kills Options",
        "P3": "🤹 Execution Gap: Optimal Number of Options"
    }

    filtered = filter_by_paper(papers, paper_id)[:15]

    print("\n" + "=" * 80)
    print(f"🧲 MAGNET RESULTS for {paper_id}: {paper_names.get(paper_id, '')}")
    print("=" * 80)
    print(f"\nTop {len(filtered)} papers with strongest attraction to {paper_id}:\n")

    for i, paper in enumerate(filtered, 1):
        score = getattr(paper, f"{paper_id.lower()}_score")
        print(f"  {i:2}. [{score:.1f}] {paper.title}")
        if paper.keywords_found:
            relevant = [k for k in paper.keywords_found
                       if k in PAPER_KEYWORDS[paper_id]["primary"] + PAPER_KEYWORDS[paper_id]["secondary"]]
            if relevant:
                print(f"      → Keywords: {', '.join(relevant[:5])}")


# ============================================================================
# SPECIAL ANALYSIS: SCOTT-CHARLIE TENSION
# ============================================================================

def analyze_tension_papers(papers: List[PaperResonance]) -> List[PaperResonance]:
    """Find papers that show tension between Scott and Charlie perspectives"""
    # Papers with both high Scott AND high Charlie scores
    tension_papers = [
        p for p in papers
        if p.scott_score > 2 and p.charlie_score > 2
    ]
    return sorted(tension_papers,
                  key=lambda p: min(p.scott_score, p.charlie_score),
                  reverse=True)


def display_tension_analysis(papers: List[PaperResonance]):
    """Display papers that embody the Scott-Charlie tension"""
    tension = analyze_tension_papers(papers)[:10]

    print("\n" + "=" * 80)
    print("⚖️ SCOTT-CHARLIE TENSION PAPERS")
    print("Papers that embody the commitment-flexibility trade-off")
    print("=" * 80)

    for i, paper in enumerate(tension[:10], 1):
        print(f"\n{i}. {paper.title}")
        print(f"   ⚡ Scott (Commitment): {paper.scott_score:.1f}")
        print(f"   🌊 Charlie (Flexibility): {paper.charlie_score:.1f}")
        print(f"   Tension Strength: {min(paper.scott_score, paper.charlie_score):.1f}")


# ============================================================================
# CITATION HELPER
# ============================================================================

def generate_citation_block(papers: List[PaperResonance], paper_id: str) -> str:
    """Generate a citation block for use in paper sections"""
    filtered = filter_by_paper(papers, paper_id)[:10]

    lines = [f"## Recommended Citations for {paper_id}\n"]
    lines.append("```markdown")
    for paper in filtered:
        # Extract author and year from filename
        match = re.search(r'([A-Za-z]+)(\d{2,4})', paper.filename)
        if match:
            author = match.group(1)
            year = match.group(2)
            if len(year) == 2:
                year = "20" + year if int(year) < 50 else "19" + year
            lines.append(f"- {author} ({year}): {paper.title}")
    lines.append("```")

    return "\n".join(lines)


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Paper Magnet — Find theoretically resonant papers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python paper_magnet.py              # Show top resonant papers
    python paper_magnet.py --paper P1   # Papers for U-Shape theory
    python paper_magnet.py --paper P2   # Papers for Competency Trap
    python paper_magnet.py --paper P3   # Papers for Execution Gap
    python paper_magnet.py --tension    # Scott-Charlie tension papers
    python paper_magnet.py --keyword "real option"
        """
    )
    parser.add_argument('--paper', '-p', choices=['P1', 'P2', 'P3'],
                        help='Filter for specific paper')
    parser.add_argument('--keyword', '-k', type=str,
                        help='Search by keyword')
    parser.add_argument('--top', '-t', type=int, default=20,
                        help='Number of top results to show')
    parser.add_argument('--tension', action='store_true',
                        help='Show Scott-Charlie tension papers')
    parser.add_argument('--cite', action='store_true',
                        help='Generate citation blocks')

    args = parser.parse_args()

    print("🧲 Scanning paper database...")
    papers = scan_all_papers()
    print(f"   Found {len(papers)} relevant papers\n")

    if args.tension:
        display_tension_analysis(papers)
    elif args.paper:
        display_paper_recommendations(args.paper, papers)
        if args.cite:
            print("\n" + generate_citation_block(papers, args.paper))
    elif args.keyword:
        filtered = filter_by_keyword(papers, args.keyword)
        display_papers_table(filtered[:args.top], f"Papers containing '{args.keyword}'")
    else:
        # Default: show top resonant papers
        top = get_top_resonant(papers, args.top)
        display_papers_table(top, f"Top {args.top} Most Theoretically Resonant Papers")

        print("\n" + "-" * 80)
        print("Quick Stats:")
        print(f"  Total papers scanned: {len(papers)}")
        print(f"  P1 (U-Shape) relevant: {len([p for p in papers if p.p1_score > 0])}")
        print(f"  P2 (Comp Trap) relevant: {len([p for p in papers if p.p2_score > 0])}")
        print(f"  P3 (Exec Gap) relevant: {len([p for p in papers if p.p3_score > 0])}")
        print(f"  Tension papers (Scott+Charlie): {len(analyze_tension_papers(papers))}")


if __name__ == "__main__":
    main()
