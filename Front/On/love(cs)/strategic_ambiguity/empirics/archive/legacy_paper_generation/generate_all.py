#!/usr/bin/env python3
"""
Master Script: Generate All Paper Sections

Executes all paper generation scripts in sequence:
1. Introduction
2. Literature Review
3. Conceptual Model
4. Methodology
5. Results
6. Discussion
7. Poster (현지의 포스터 공방)
8. Industry Comparison (PR #13 integration)

Usage:
    python generate_all.py
    python generate_all.py --sections 1 2 3  # Generate only specific sections
    python generate_all.py --sections 7      # Generate poster only
    python generate_all.py --sections 8      # Generate industry comparison only
"""

import sys
import argparse
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.scripts.paper_generation import OUTPUT_DIR


def run_section(section_num, section_name, module_name):
    """Run a single section generation script"""
    print(f"\n{'='*60}")
    print(f"Section {section_num}: {section_name}")
    print(f"{'='*60}")

    try:
        module = __import__(f"src.scripts.paper_generation.{module_name}", fromlist=[module_name])
        module.main()
        return True
    except Exception as e:
        print(f"❌ Error generating section {section_num}: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description="Generate academic paper sections")
    parser.add_argument(
        "--sections",
        nargs="+",
        type=int,
        choices=range(1, 9),
        help="Specific sections to generate (1-8). Default: all sections"
    )
    args = parser.parse_args()

    sections = [
        (1, "Introduction", "generate_01_intro"),
        (2, "Literature Review", "generate_02_litreview"),
        (3, "Conceptual Model", "generate_03_conceptual"),
        (4, "Methodology", "generate_04_method"),
        (5, "Results", "generate_05_results"),
        (6, "Discussion", "generate_06_discussion"),
        (7, "Poster", "generate_07_poster"),
        (8, "Industry Comparison", "generate_08_industry_comparison")
    ]

    # Filter sections if specified
    if args.sections:
        sections = [s for s in sections if s[0] in args.sections]

    print("="*60)
    print("PAPER GENERATION PIPELINE")
    print("="*60)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Sections to generate: {[s[0] for s in sections]}")
    print("="*60)

    success_count = 0
    failed_sections = []

    for section_num, section_name, module_name in sections:
        if run_section(section_num, section_name, module_name):
            success_count += 1
        else:
            failed_sections.append(section_num)

    # Summary
    print("\n" + "="*60)
    print("GENERATION COMPLETE")
    print("="*60)
    print(f"✅ Successfully generated: {success_count}/{len(sections)} sections")

    if failed_sections:
        print(f"❌ Failed sections: {failed_sections}")
        return 1

    print(f"\n📂 Output location: {OUTPUT_DIR}")
    print("\nGenerated files:")
    for section_num, section_name, _ in sections:
        # Special handling for poster (SVG + MD)
        if section_num == 7:
            svg_path = OUTPUT_DIR / "07_Poster.svg"
            md_path = OUTPUT_DIR / "07_Poster.md"
            if svg_path.exists() and md_path.exists():
                print(f"   ✓ 07_Poster.svg + 07_Poster.md")
            else:
                print(f"   ✗ 07_Poster files (not found)")
        else:
            filename = f"0{section_num}_" + section_name.replace(" ", "") + ".md"
            filepath = OUTPUT_DIR / filename
            if filepath.exists():
                print(f"   ✓ {filename}")
            else:
                print(f"   ✗ {filename} (not found)")

    print("\n" + "="*60)
    print("NEXT STEPS")
    print("="*60)
    print("1. Review generated Markdown files in:", OUTPUT_DIR)
    print("2. Expand each section using LLM with META_PROMPT from source code")
    print("3. Open 07_Poster.svg in browser for visual poster")
    print("4. Integrate into LaTeX template")
    print("5. Add citations and references")
    print("6. Generate figures and tables")
    print("\n💡 Pro tip: Use Claude or GPT-4 to expand sections based on META_PROMPT")
    print("   Each script contains detailed META_PROMPT in source code")
    print("\n🎨 Poster tip: 07_Poster.svg is 30-second visual summary")
    print("   현지의 포스터 공방: 복잡한 것을 단순하게, 단순한 것을 아름답게")

    return 0


if __name__ == "__main__":
    sys.exit(main())
