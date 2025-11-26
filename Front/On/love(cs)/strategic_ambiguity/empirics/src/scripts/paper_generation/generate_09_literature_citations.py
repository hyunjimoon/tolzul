#!/usr/bin/env python3
"""
PHASE 9: 총 (Literature Citations for Thesis) — 문현지 📚
"문헌을 종합하는 사람" — The Literature Synthesizer

Consolidated single-file implementation aligned with Thesis Chapter 2 structure:
- 2.1 Literature Scanning (scan_literature_library)
- 2.2 Relevance Ranking (rank_by_relevance)
- 2.3 Citation Generation (generate_citations)

Commander: 문현지 (Moon Hyunji)
Narrative Role: 총 (Synthesis/Integration)
Color: Indigo (#4B0082)

Output: 09_Literature_Citations.md
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import sys
import argparse
import yaml
import re

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from src.scripts.paper_generation import OUTPUT_DIR

# ============================================================================
# PHASE METADATA
# ============================================================================

PHASE_ID: int = 9
PHASE_NAME: str = "Literature Citations for Thesis"
COMMANDER: str = "문현지"
NARRATIVE_ROLE: str = "총"
OUTPUT_FILENAME: str = "09_Literature_Citations.md"

# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class PaperMetadata:
    """Structured metadata for a paper"""
    filename: str
    authors: List[str] = field(default_factory=list)
    year: Optional[int] = None
    title: str = ""
    core_argument: str = ""
    key_concepts: List[str] = field(default_factory=list)
    field_tags: List[str] = field(default_factory=list)
    research_tags: List[str] = field(default_factory=list)
    connections: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class ScoredPaper:
    """Paper with relevance scores"""
    paper: PaperMetadata
    total_score: float
    concept_score: float
    method_score: float
    network_score: float


# Key papers for citation network
KEY_PAPERS = {
    'pontikes', 'Abdallah2014', 'Padgett1993', 'Eisenberg1984',
    'gans23', 'gans22', 'gans20', 'Ferraro2015'
}


# ============================================================================
# 2.1 LITERATURE SCANNING
# ============================================================================

def scan_literature_library(library_path: Path) -> List[PaperMetadata]:
    """
    2.1 Literature Scanning: Parse all papers in library
    
    Extracts metadata from markdown files:
    - YAML frontmatter (author, year, field, tags)
    - Core argument from content
    - Key concepts
    """
    papers = []
    
    if not library_path.exists():
        print(f"Error: Library path does not exist: {library_path}")
        return papers
    
    md_files = [f for f in library_path.glob("*.md") 
                if not ('TEMPLATE' in f.name or f.name.startswith('_'))]
    
    print(f"Found {len(md_files)} markdown files in library")
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            paper = _parse_paper(md_file.name, content)
            if paper:
                papers.append(paper)
        except Exception as e:
            print(f"Warning: Failed to parse {md_file.name}: {e}")
    
    print(f"Successfully parsed {len(papers)} papers")
    return papers


def _parse_paper(filename: str, content: str) -> Optional[PaperMetadata]:
    """Parse single paper file"""
    # Extract YAML frontmatter
    frontmatter = {}
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            frontmatter = yaml.safe_load(match.group(1)) or {}
        except:
            pass
    
    # Extract metadata
    paper = PaperMetadata(filename=filename)
    
    # Authors
    if 'author_ids' in frontmatter:
        authors = frontmatter['author_ids']
        if isinstance(authors, list):
            paper.authors = [str(a).strip() for a in authors if a]
        elif isinstance(authors, str):
            paper.authors = [authors.strip()]
    
    # Year
    if 'year' in frontmatter:
        try:
            paper.year = int(frontmatter['year'])
        except:
            pass
    
    # Title from first heading
    heading = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if heading:
        paper.title = re.sub(r'📜|🗄️|\[.*?\]', '', heading.group(1)).strip()
    else:
        paper.title = filename.replace('📜', '').replace('.md', '').replace('_', ' ')
    
    # Core argument
    for pattern in [r'##\s*핵심 논점.*?\n(.*?)(?=\n##|\Z)',
                    r'##\s*Core Argument.*?\n(.*?)(?=\n##|\Z)',
                    r'##\s*Summary.*?\n(.*?)(?=\n##|\Z)']:
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            arg = re.split(r'\n\n|\n###', match.group(1).strip())[0]
            paper.core_argument = re.sub(r'\*\*|\*|`|\n', ' ', arg)[:500]
            break
    
    # Key concepts from ### headers
    concepts_match = re.search(r'##\s*Key Concepts.*?\n(.*?)(?=\n##|\Z)', 
                               content, re.DOTALL | re.IGNORECASE)
    if concepts_match:
        paper.key_concepts = re.findall(r'###\s*(.+)$', concepts_match.group(1), re.MULTILINE)[:10]
    
    # Field tags
    if 'field' in frontmatter:
        fields = frontmatter['field']
        paper.field_tags = [str(f).strip() for f in (fields if isinstance(fields, list) else [fields])]
    
    # Research tags
    if 'tags' in frontmatter:
        tags = frontmatter['tags']
        paper.research_tags = [str(t).strip() for t in (tags if isinstance(tags, list) else [])]
    
    # Connections
    if 'connections' in frontmatter:
        paper.connections = frontmatter['connections']
    
    return paper


# ============================================================================
# 2.2 RELEVANCE RANKING
# ============================================================================

def rank_by_relevance(
    papers: List[PaperMetadata],
    thesis_keywords: List[str],
    top_n: int = 10,
    weights: Dict[str, float] = None
) -> List[ScoredPaper]:
    """
    2.2 Relevance Ranking: Score and rank papers by thesis relevance
    
    Weighted scoring (0-10 scale):
    - Concept overlap (50%): Keyword matching
    - Methodological fit (30%): Theory/empirical alignment
    - Citation network (20%): Connections to key papers
    """
    if weights is None:
        weights = {'concept': 0.5, 'method': 0.3, 'network': 0.2}
    
    scored = []
    for paper in papers:
        concept = _score_concepts(paper, thesis_keywords)
        method = _score_methodology(paper)
        network = _score_network(paper)
        
        total = (weights['concept'] * concept + 
                weights['method'] * method + 
                weights['network'] * network)
        
        scored.append(ScoredPaper(paper, total, concept, method, network))
    
    scored.sort(key=lambda x: x.total_score, reverse=True)
    return scored[:top_n]


def _score_concepts(paper: PaperMetadata, keywords: List[str]) -> float:
    """Score concept overlap with thesis keywords"""
    text = f"{paper.title} {paper.core_argument} {' '.join(paper.key_concepts)} {' '.join(paper.research_tags)}"
    text = re.sub(r'[^a-z0-9\s]', '', text.lower())
    
    matches = sum(1.5 if kw.lower() in text else 0 for kw in keywords)
    return min(matches / len(keywords) * 10, 10.0) if keywords else 0.0


def _score_methodology(paper: PaperMetadata) -> float:
    """Score methodological relevance"""
    score = 5.0
    
    # Preferred fields
    preferred = {'strategy', 'org', 'innovation', 'causality', 'bayesian'}
    field_matches = sum(1 for tag in paper.field_tags 
                       if any(p in tag.lower() for p in preferred))
    score += min(field_matches * 1.5, 3.0)
    
    # Method keywords
    methods = ['bayesian', 'formal', 'model', 'theory', 'mechanism', 'causal']
    text = (paper.core_argument + ' '.join(paper.key_concepts)).lower()
    method_matches = sum(1 for m in methods if m in text)
    score += min(method_matches * 0.5, 2.0)
    
    return min(score, 10.0)


def _score_network(paper: PaperMetadata) -> float:
    """Score citation network proximity"""
    score = 0.0
    
    # Check filename
    if any(key in paper.filename.lower() for key in KEY_PAPERS):
        score += 5.0
    
    # Check connections
    if paper.connections:
        all_conns = []
        for conn_type in ['extends', 'applied_in', 'related_to']:
            all_conns.extend(paper.connections.get(conn_type, []))
        
        for conn in all_conns:
            if any(key in str(conn).lower() for key in KEY_PAPERS):
                score += 2.0
                break
    
    return min(score, 10.0)


# ============================================================================
# 2.3 CITATION GENERATION
# ============================================================================

def generate_citations(scored_papers: List[ScoredPaper]) -> str:
    """
    2.3 Citation Generation: Create thesis-ready citation sentences
    
    For each paper:
    - Format authors (single, dual, et al.)
    - Extract core claim
    - Generate linkage to thesis
    - Produce insertable sentence
    """
    content = f"""# 9. Literature Citations for Thesis

**Thesis**: "Flexibility and Commitment in Entrepreneurship"  
**Generated**: 2025-11-24  
**Total Papers Scanned**: {len(scored_papers)}  
**Top Papers Selected**: {len(scored_papers)}

## 9.1 Overview

This section synthesizes theoretical foundations supporting our empirical findings on strategic vagueness.

**Key Empirical Findings**:
- **H1 (Early Funding)**: Vagueness reduces early-stage funding (β=-8.5×10⁻⁷, p<0.001)
- **H2 (Growth)**: Hardware ventures experience 3× stronger vagueness penalty (β=-0.030, p=0.046)
- **Core Mechanism**: Technology modularity moderates the vagueness-performance relationship

## 9.2 Top {len(scored_papers)} Ranked Papers

"""
    
    for i, scored in enumerate(scored_papers, 1):
        paper = scored.paper
        
        # Format citation
        citation = _format_citation(paper.authors, paper.year)
        
        # Core claim
        claim = paper.core_argument[:200] if paper.core_argument else f"Examines {paper.title.lower()}."
        if not claim.endswith('.'):
            claim += '.'
        
        # Linkage
        linkage = "Directly supports thesis concepts." if scored.concept_score > 7 else "Contributes to theoretical understanding."
        if paper.connections:
            if 'extends' in paper.connections:
                linkage = "Extends foundational theory; " + linkage
        
        # Thesis sentence
        thesis_sentence = f"{claim.rstrip('.')} {citation}."
        
        # Build entry
        authors_str = ', '.join(paper.authors) if paper.authors else "Unknown"
        year_str = str(paper.year) if paper.year else "n.d."
        
        content += f"""### {i}. {paper.title} — Score: {scored.total_score:.1f}/10

**Paper**: [{paper.filename}](file:///Users/hyunjimoon/tolzul/Space/Library/1논문용/{paper.filename})  
**Authors**: {authors_str} ({year_str})  
**Core Claim**: {claim}

**Linkage to Thesis**: {linkage}

**Citation-Ready Sentence**:
> {thesis_sentence}

**Relevance Breakdown**:
- Concept Overlap: {scored.concept_score:.1f}/10
- Methodological Fit: {scored.method_score:.1f}/10
- Citation Network: {scored.network_score:.1f}/10

---

"""
    
    content += f"""
## 9.3 Integration with Empirical Findings

These {len(scored_papers)} papers provide theoretical scaffolding for our empirical analysis, connecting information economics (H1), real options theory (H2), and modularity perspectives.

---

**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})  
**Commander:** {COMMANDER} 📚  
**Generated from:** `{Path(__file__).name}`
"""
    
    return content


def _format_citation(authors: List[str], year: int = None) -> str:
    """Format author citation"""
    if not authors:
        return "(Unknown)"
    
    last_names = [a.replace(',', '').split()[-1] for a in authors if a]
    
    if len(last_names) == 1:
        citation = last_names[0]
    elif len(last_names) == 2:
        citation = f"{last_names[0]} & {last_names[1]}"
    else:
        citation = f"{last_names[0]} et al."
    
    if year:
        citation = f"{citation} {year}"
    
    return f"({citation})"


# ============================================================================
# CONFIGURATION & MAIN
# ============================================================================

def load_config() -> dict:
    """Load configuration from YAML file"""
    config_path = Path(__file__).parent / "config" / "citation_config.yaml"
    
    if config_path.exists():
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    return {
        'thesis': {
            'title': 'Flexibility and Commitment in Entrepreneurship',
            'keywords': ['ambiguity', 'flexibility', 'commitment', 'stakeholder']
        },
        'scoring': {'concept_weight': 0.5, 'methodology_weight': 0.3, 'network_weight': 0.2},
        'output': {
            'top_n': 10,
            'paper_library_path': '/Users/hyunjimoon/tolzul/Space/Library/1논문용'
        }
    }


def main() -> None:
    """Main execution"""
    parser = argparse.ArgumentParser(description='Generate literature citations for thesis')
    parser.add_argument('--keywords', type=str, help='Comma-separated thesis keywords')
    parser.add_argument('--top-n', type=int, default=10, help='Number of top papers')
    parser.add_argument('--library-path', type=str, help='Path to paper library')
    args = parser.parse_args()
    
    config = load_config()
    
    # Get parameters
    keywords = [k.strip() for k in args.keywords.split(',')] if args.keywords else config['thesis']['keywords']
    library_path = Path(args.library_path) if args.library_path else Path(config['output']['paper_library_path'])
    top_n = args.top_n
    weights = {
        'concept': config['scoring']['concept_weight'],
        'method': config['scoring']['methodology_weight'],
        'network': config['scoring']['network_weight']
    }
    
    # Print header
    print("=" * 70)
    print(f"PHASE {PHASE_ID}: {NARRATIVE_ROLE} — {PHASE_NAME}")
    print(f"Commander: {COMMANDER} 📚 (The Literature Synthesizer)")
    print("=" * 70)
    print()
    
    # Execute pipeline
    print(f"📚 2.1 Literature Scanning: {library_path}")
    papers = scan_literature_library(library_path)
    
    print(f"🔍 2.2 Relevance Ranking ({len(papers)} papers)...")
    print(f"   Keywords: {', '.join(keywords)}")
    scored = rank_by_relevance(papers, keywords, top_n, weights)
    
    print(f"✍️  2.3 Citation Generation (top {len(scored)} papers)...")
    content = generate_citations(scored)
    
    # Write output
    output_path = OUTPUT_DIR / OUTPUT_FILENAME
    output_path.write_text(content)
    
    print()
    print(f"✅ Generated: {output_path}")
    print(f"📊 Statistics:")
    print(f"   - Papers scanned: {len(papers)}")
    print(f"   - Top papers selected: {len(scored)}")
    print(f"   - Keywords: {', '.join(keywords)}")
    print()
    print(f"📚 문현지 says: 'The synthesis is complete!'")


if __name__ == "__main__":
    main()
