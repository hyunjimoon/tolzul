#!/usr/bin/env python3
"""
parallel_generator.py - Run all 8 sections in parallel using 8 agents

Each agent is responsible for one section, running independently.
Agents execute concurrently using Python's multiprocessing pool.

Usage:
    python parallel_generator.py
    python parallel_generator.py --verbose
"""

import multiprocessing
import subprocess
import sys
import time
from pathlib import Path
import argparse


def run_section(section_num):
    """
    Run a single section generator (Agent worker function)

    Each agent:
    1. Executes its assigned script
    2. Captures output
    3. Reports success/failure
    4. Returns verification data
    """
    scripts = {
        1: "generate_01_intro.py",
        2: "generate_02_litreview.py",
        3: "generate_03_conceptual.py",
        4: "generate_04_method.py",
        5: "generate_05_results.py",
        6: "generate_06_discussion.py",
        7: "generate_07_poster.py",
        8: "generate_08_industry_comparison.py"
    }

    agent_names = {
        1: "📝 Introduction Agent",
        2: "📚 Literature Agent",
        3: "🧠 Conceptual Agent",
        4: "🔬 Methodology Agent",
        5: "📊 Results Agent",
        6: "💭 Discussion Agent",
        7: "🎨 Poster Agent",
        8: "🏭 Industry Agent"
    }

    script = scripts[section_num]
    agent_name = agent_names[section_num]

    print(f"[{agent_name}] Starting {script}...")
    start_time = time.time()

    try:
        result = subprocess.run(
            ["python", script],
            capture_output=True,
            text=True,
            timeout=60  # 60 second timeout per section
        )

        elapsed = time.time() - start_time

        if result.returncode == 0:
            print(f"[{agent_name}] ✅ Completed in {elapsed:.1f}s")
            return {
                "section": section_num,
                "agent": agent_name,
                "success": True,
                "time": elapsed,
                "output": result.stdout,
                "error": None
            }
        else:
            print(f"[{agent_name}] ❌ Failed after {elapsed:.1f}s")
            return {
                "section": section_num,
                "agent": agent_name,
                "success": False,
                "time": elapsed,
                "output": result.stdout,
                "error": result.stderr
            }

    except subprocess.TimeoutExpired:
        print(f"[{agent_name}] ⏱️ Timeout (>60s)")
        return {
            "section": section_num,
            "agent": agent_name,
            "success": False,
            "time": 60.0,
            "output": None,
            "error": "Timeout after 60 seconds"
        }

    except Exception as e:
        print(f"[{agent_name}] ❌ Error: {e}")
        return {
            "section": section_num,
            "agent": agent_name,
            "success": False,
            "time": 0.0,
            "output": None,
            "error": str(e)
        }


def verify_outputs():
    """Verify all expected output files exist"""
    output_dir = Path("output")

    expected_files = {
        1: "01_Introduction.md",
        2: "02_LiteratureReview.md",
        3: "03_Conceptual_Model.md",
        4: "04_Method.md",
        5: "05_Results.md",
        6: "06_Discussion.md",
        7: "07_Poster.svg",
        8: "08_IndustryComparison.md"
    }

    results = {}
    total_size = 0

    for section, filename in expected_files.items():
        filepath = output_dir / filename
        if filepath.exists():
            size = filepath.stat().st_size
            results[section] = {
                "exists": True,
                "size": size,
                "size_kb": size / 1024
            }
            total_size += size
        else:
            results[section] = {
                "exists": False,
                "size": 0,
                "size_kb": 0
            }

    # Check for additional files (poster MD, spec curve PNG)
    poster_md = output_dir / "07_Poster.md"
    spec_curve = output_dir / "spec_curve_analysis.png"

    if poster_md.exists():
        total_size += poster_md.stat().st_size
    if spec_curve.exists():
        total_size += spec_curve.stat().st_size

    results["total_size"] = total_size
    results["total_size_kb"] = total_size / 1024

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Run 8 parallel agents for paper generation"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed output from each agent"
    )
    args = parser.parse_args()

    print("=" * 70)
    print("PARALLEL PAPER GENERATION - 8 AGENTS")
    print("=" * 70)
    print(f"Strategy: 8 independent agents, 1 per section")
    print(f"Execution: Concurrent multiprocessing pool")
    print(f"Expected time: ~5 seconds")
    print("=" * 70)
    print()

    start_time = time.time()

    # Create process pool with 8 workers (1 per section)
    print("🚀 Launching 8 agents in parallel...")
    print()

    with multiprocessing.Pool(processes=8) as pool:
        # Launch all 8 sections concurrently
        results = pool.map(run_section, range(1, 9))

    total_time = time.time() - start_time

    print()
    print("=" * 70)
    print("EXECUTION SUMMARY")
    print("=" * 70)

    # Count successes
    success_count = sum(1 for r in results if r["success"])

    # Sort by section number for display
    results_sorted = sorted(results, key=lambda x: x["section"])

    for r in results_sorted:
        status = "✅" if r["success"] else "❌"
        print(f"{status} Section {r['section']}: {r['agent']} ({r['time']:.1f}s)")

        if args.verbose and not r["success"]:
            print(f"   Error: {r['error']}")

    print()
    print(f"✅ Successfully generated: {success_count}/8 sections")
    print(f"⏱️  Total execution time: {total_time:.1f}s")

    # Calculate speedup vs sequential
    total_agent_time = sum(r["time"] for r in results)
    speedup = total_agent_time / total_time if total_time > 0 else 1
    print(f"⚡ Speedup: {speedup:.1f}x (parallel efficiency: {speedup/8*100:.0f}%)")

    print()
    print("=" * 70)
    print("OUTPUT VERIFICATION")
    print("=" * 70)

    verification = verify_outputs()

    for section in range(1, 9):
        if section in verification:
            v = verification[section]
            status = "✅" if v["exists"] else "❌"
            size_str = f"{v['size_kb']:.1f}KB" if v["exists"] else "missing"
            print(f"{status} Section {section}: {size_str}")

    print()
    print(f"📂 Total output size: {verification['total_size_kb']:.1f}KB")

    # List all files in output directory
    output_dir = Path("output")
    if output_dir.exists():
        all_files = list(output_dir.glob("*"))
        print(f"📄 Total files generated: {len(all_files)}")

    print()
    print("=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print("1. Review generated markdown files in: output/")
    print("2. Open 07_Poster.svg in browser for visual summary")
    print("3. Expand sections using LLM with META_PROMPT")
    print("4. Integrate into LaTeX template")
    print()

    # Return exit code
    if success_count == 8:
        print("🎉 All agents completed successfully!")
        return 0
    else:
        print(f"⚠️  {8 - success_count} agent(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
