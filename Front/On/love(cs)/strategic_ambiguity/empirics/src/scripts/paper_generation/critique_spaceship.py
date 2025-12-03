#!/usr/bin/env python3
"""
CRITIQUE SPACESHIP: The Automated "Reviewer #2" 👹
==================================================
"This paper is promising, but..." — Reviewer #2

This script acts as the "Red Team" for the Jeolla Left Navy.
It ruthlessly critiques the generated markdown files for:
1. Structure (Missing sections?)
2. Vagueness (Too many weasel words?)
3. Citations (Are you just making things up?)
4. Length (Is it substantial?)

Output: `critique_report.json`
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any

# Configuration
CURRENT_DIR = Path(__file__).parent
OUTPUT_DIR = CURRENT_DIR / "output"
REPORT_FILE = CURRENT_DIR / "critique_report.json"

# "Weasel Words" that suggest weakness/vagueness
WEASEL_WORDS = [
    "maybe", "perhaps", "possibly", "might", "could", "believe", "hope", 
    "seem", "appear", "suggests", "arguably", "conceivably"
]

# "They Say / I Say" Patterns (Graff & Birkenstein)
THEY_SAY_PATTERNS = [
    "argue", "claim", "contend", "suggest", "assert", "believe", "emphasize", 
    "according to", "in the view of", "as x puts it"
]

I_SAY_PATTERNS = [
    "however", "in contrast", "on the other hand", "we propose", "we argue", 
    "my view", "our data", "this paper", "in this study"
]

NAYSAYER_PATTERNS = [
    "skeptics", "critics", "objection", "may object", "might argue", 
    "of course", "admittedly", "to be sure"
]

SO_WHAT_PATTERNS = [
    "consequently", "therefore", "as a result", "implication", "matter", 
    "significant", "crucial", "important"
]

# Posen-Cachon "Contribution" Patterns
# "What was thought to be X is really Y" (Surprise/Null-Breaking)
NULL_BREAKING_PATTERNS = [
    "contrary to", "unlike", "traditionally", "assumed that", "challenge", 
    "surprising", "unexpected", "in fact", "actually", "turns out",
    "common belief", "conventional wisdom", "prevailing view"
]

# Kim Agents (Department-Specific Patterns)
# Kim U (Entrepreneurship & Innovation)
KIM_U_PATTERNS = [
    "innovation", "entrepreneur", "venture", "value creation", "scaling", 
    "business model", "disruption", "opportunity", "founder"
]

# Kim C (Business Strategy)
KIM_C_PATTERNS = [
    "competitive advantage", "performance", "strategic choice", "heterogeneity", 
    "capabilities", "resource", "positioning", "rivalry", "industry"
]

# Kim N (Operations Management)
KIM_N_PATTERNS = [
    "efficiency", "process", "supply chain", "optimization", "inventory", 
    "coordination", "throughput", "bottleneck", "operational"
]

def analyze_file(file_path: Path) -> Dict[str, Any]:
    """Analyze a single markdown file and return metrics."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return {"error": str(e), "risk_score": 100}

    # 1. Length Check
    words = len(content.split())
    content_lower = content.lower()
    
    # 2. Structure Check (Headers)
    headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
    has_structure = len(headers) >= 3  # At least Title + 2 sections
    
    # 3. Vagueness Check
    weasel_count = sum(content_lower.count(w) for w in WEASEL_WORDS)
    vagueness_ratio = (weasel_count / max(1, words)) * 1000  # Per 1000 words
    
    # 4. Citation Check (Simple heuristic for (Name, Year))
    citations = re.findall(r'\([A-Z][a-z]+,\s?\d{4}\)', content)
    citation_count = len(citations)
    
    # 5. "They Say / I Say" Check (Especially for Chap 1 & 2)
    is_intro_theory = "chap1" in file_path.name or "chap2" in file_path.name
    
    has_they_say = any(p in content_lower for p in THEY_SAY_PATTERNS)
    has_i_say = any(p in content_lower for p in I_SAY_PATTERNS)
    has_naysayer = any(p in content_lower for p in NAYSAYER_PATTERNS)
    has_so_what = any(p in content_lower for p in SO_WHAT_PATTERNS)
    
    # 6. Posen-Cachon "Contribution" Check (Surprise)
    has_null_breaking = any(p in content_lower for p in NULL_BREAKING_PATTERNS)
    
    # 7. Kim Agents (Department Check)
    fname = file_path.name
    is_U = "_U_" in fname
    is_C = "_C_" in fname
    is_N = "_N_" in fname
    
    has_kim_u = any(p in content_lower for p in KIM_U_PATTERNS)
    has_kim_c = any(p in content_lower for p in KIM_C_PATTERNS)
    has_kim_n = any(p in content_lower for p in KIM_N_PATTERNS)

    # Load Config
    CONFIG_FILE = CURRENT_DIR / "critique_config.json"
    config = {
        "weights": {
            "length_short": 50, "length_shallow": 20, "structure_missing": 30,
            "vagueness": 20, "citation_missing": 20,
            "rhetoric_context": 15, "rhetoric_voice": 15, "rhetoric_naysayer": 10, "rhetoric_sowhat": 10,
            "surprise_null_breaking": 15, "department_fit": 20
        },
        "toggles": {
            "enable_length_check": True, "enable_structure_check": True, "enable_vagueness_check": True,
            "enable_citation_check": True, "enable_rhetoric_check": True, "enable_surprise_check": True,
            "enable_department_check": True
        }
    }
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                loaded_config = json.load(f)
                config["weights"].update(loaded_config.get("weights", {}))
                config["toggles"].update(loaded_config.get("toggles", {}))
        except Exception as e:
            print(f"⚠️ Error loading config: {e}")

    w = config["weights"]
    t = config["toggles"]

    # --- SCORING LOGIC (The "Reviewer #2" Brain) ---
    risk_score = 0
    critiques = []
    
    # Length Penalty
    if t["enable_length_check"]:
        if words < 100:
            risk_score += w["length_short"]
            critiques.append("Too short (stub?)")
        elif words < 500:
            risk_score += w["length_shallow"]
            critiques.append("Lacks depth")
        
    # Structure Penalty
    if t["enable_structure_check"] and not has_structure:
        risk_score += w["structure_missing"]
        critiques.append("Poor structure (missing headers)")
        
    # Vagueness Penalty
    if t["enable_vagueness_check"] and vagueness_ratio > 5:
        risk_score += w["vagueness"]
        critiques.append(f"Vague language ({int(vagueness_ratio)}/1k)")
        
    # Citation Penalty
    if t["enable_citation_check"] and citation_count == 0 and words > 300:
        risk_score += w["citation_missing"]
        critiques.append("Missing citations")

    # "They Say / I Say" Penalty (Targeted)
    if t["enable_rhetoric_check"] and is_intro_theory:
        if not has_they_say:
            risk_score += w["rhetoric_context"]
            critiques.append("Missing 'They Say' (Context)")
        if not has_i_say:
            risk_score += w["rhetoric_voice"]
            critiques.append("Missing 'I Say' (Voice)")
        if not has_naysayer and words > 500:
            risk_score += w["rhetoric_naysayer"]
            critiques.append("Missing 'Naysayer' (Counter-arg)")
        if not has_so_what:
            risk_score += w["rhetoric_sowhat"]
            critiques.append("Missing 'So What?' (Significance)")
            
    # Posen-Cachon Penalty
    if t["enable_surprise_check"] and is_intro_theory:
        if not has_null_breaking:
            risk_score += w["surprise_null_breaking"]
            critiques.append("Missing 'Surprise' (Null-Breaking)")
            
    # Kim Agent Penalties (Department Fit)
    if t["enable_department_check"]:
        if is_U and not has_kim_u:
            risk_score += w["department_fit"]
            critiques.append("Missing 'Entrepreneurship' keywords (Kim U)")
        if is_C and not has_kim_c:
            risk_score += w["department_fit"]
            critiques.append("Missing 'Strategy' keywords (Kim C)")
        if is_N and not has_kim_n:
            risk_score += w["department_fit"]
            critiques.append("Missing 'Operations' keywords (Kim N)")
        
    # Cap score
    risk_score = min(100, risk_score)
    
    # Determine Risk Level (0-3) for Dashboard
    # 0: Low Risk (Green), 1: Medium (Yellow), 2: High (Orange), 3: Critical (Red)
    if risk_score < 20: risk_level = 0
    elif risk_score < 50: risk_level = 1
    elif risk_score < 80: risk_level = 2
    else: risk_level = 3
    
    return {
        "file": file_path.name,
        "words": words,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "critiques": critiques,
        "citation_count": citation_count
    }

def main():
    print("👹 Reviewer #2 is entering the room...")
    
    if not OUTPUT_DIR.exists():
        print("❌ Output directory not found!")
        return

    report = {}
    files = list(OUTPUT_DIR.glob("*.md"))
    
    if not files:
        print("❌ No papers found to critique!")
        return

    print(f"🔍 Scanning {len(files)} papers...")
    
    for f in files:
        # Skip non-paper files if any
        if not f.name.startswith("chap"):
            continue
            
        result = analyze_file(f)
        report[f.name] = result
        
        # Print summary
        icon = "🟢" if result["risk_level"] == 0 else "🟡" if result["risk_level"] == 1 else "🟠" if result["risk_level"] == 2 else "🔴"
        print(f"{icon} {f.name}: Score {result['risk_score']} | {', '.join(result['critiques'])}")

    # Save Report
    with open(REPORT_FILE, 'w') as f:
        json.dump(report, f, indent=2)
        
    print(f"\n📝 Critique Report saved to: {REPORT_FILE}")
    print("👹 Reviewer #2 says: 'Address these comments immediately.'")

if __name__ == "__main__":
    main()
