# Parallel Agent Testing Guide

## Running 8 Agents in Parallel (Claude Code)

### Method 1: Using Claude Code Task Tool (Recommended)

You can launch 8 parallel agents, one for each section, in a single Claude Code message:

```
Launch 8 parallel agents to test paper generation pipeline:

Agent 1: Test Section 1 (Introduction) - run generate_01_intro.py and verify output
Agent 2: Test Section 2 (Literature) - run generate_02_litreview.py and verify output
Agent 3: Test Section 3 (Conceptual) - run generate_03_conceptual.py and verify output
Agent 4: Test Section 4 (Methodology) - run generate_04_method.py and verify output
Agent 5: Test Section 5 (Results) - run generate_05_results.py and verify output
Agent 6: Test Section 6 (Discussion) - run generate_06_discussion.py and verify output
Agent 7: Test Section 7 (Poster) - run generate_07_poster.py and verify SVG output
Agent 8: Test Section 8 (Industry) - run generate_08_industry_comparison.py and verify output

Each agent should:
1. Navigate to src/scripts/paper_generation
2. Run their assigned script
3. Verify the output file exists and has non-zero size
4. Extract and report key statistics/content
5. Report success/failure status
```

### Method 2: Using Bash Background Jobs

```bash
cd src/scripts/paper_generation

# Launch all 8 sections in parallel
python generate_01_intro.py > logs/01.log 2>&1 &
python generate_02_litreview.py > logs/02.log 2>&1 &
python generate_03_conceptual.py > logs/03.log 2>&1 &
python generate_04_method.py > logs/04.log 2>&1 &
python generate_05_results.py > logs/05.log 2>&1 &
python generate_06_discussion.py > logs/06.log 2>&1 &
python generate_07_poster.py > logs/07.log 2>&1 &
python generate_08_industry_comparison.py > logs/08.log 2>&1 &

# Wait for all to complete
wait

# Check results
echo "All sections completed!"
ls -lh output/
```

### Method 3: Using GNU Parallel

```bash
cd src/scripts/paper_generation

# Create job list
cat > jobs.txt <<EOF
python generate_01_intro.py
python generate_02_litreview.py
python generate_03_conceptual.py
python generate_04_method.py
python generate_05_results.py
python generate_06_discussion.py
python generate_07_poster.py
python generate_08_industry_comparison.py
EOF

# Run in parallel (8 jobs at once)
parallel -j 8 < jobs.txt

# Verify outputs
ls -lh output/
```

### Method 4: Using Python multiprocessing

```python
#!/usr/bin/env python3
"""
parallel_generator.py - Run all 8 sections in parallel
"""

import multiprocessing
import subprocess
import sys
from pathlib import Path

def run_section(section_num):
    """Run a single section generator"""
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

    script = scripts[section_num]
    print(f"[Agent {section_num}] Starting {script}...")

    try:
        result = subprocess.run(
            ["python", script],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            print(f"[Agent {section_num}] ✅ Completed {script}")
            return (section_num, True, result.stdout)
        else:
            print(f"[Agent {section_num}] ❌ Failed {script}")
            return (section_num, False, result.stderr)
    except Exception as e:
        print(f"[Agent {section_num}] ❌ Error: {e}")
        return (section_num, False, str(e))

def main():
    print("=" * 60)
    print("PARALLEL PAPER GENERATION - 8 AGENTS")
    print("=" * 60)

    # Create process pool with 8 workers
    with multiprocessing.Pool(processes=8) as pool:
        # Launch all 8 sections in parallel
        results = pool.map(run_section, range(1, 9))

    # Summarize results
    print("\n" + "=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)

    success_count = sum(1 for _, success, _ in results if success)

    for section_num, success, output in results:
        status = "✅" if success else "❌"
        print(f"{status} Section {section_num}: {'SUCCESS' if success else 'FAILED'}")

    print(f"\n✅ Successfully generated: {success_count}/8 sections")

    # Verify output files
    output_dir = Path("output")
    if output_dir.exists():
        files = list(output_dir.glob("*.md")) + list(output_dir.glob("*.svg"))
        print(f"\n📂 Generated {len(files)} files in output/")

    return 0 if success_count == 8 else 1

if __name__ == "__main__":
    sys.exit(main())
```

Usage:
```bash
cd src/scripts/paper_generation
chmod +x parallel_generator.py
python parallel_generator.py
```

### Method 5: Using Make (Parallel Build)

Create a `Makefile`:

```makefile
# Makefile for parallel paper generation

.PHONY: all clean test

OUTPUT_DIR = output
SECTIONS = 01 02 03 04 05 06 07 08

# Target files
TARGETS = \
	$(OUTPUT_DIR)/01_Introduction.md \
	$(OUTPUT_DIR)/02_LiteratureReview.md \
	$(OUTPUT_DIR)/03_Conceptual_Model.md \
	$(OUTPUT_DIR)/04_Method.md \
	$(OUTPUT_DIR)/05_Results.md \
	$(OUTPUT_DIR)/06_Discussion.md \
	$(OUTPUT_DIR)/07_Poster.svg \
	$(OUTPUT_DIR)/08_IndustryComparison.md

# Build all sections in parallel
all: $(TARGETS)
	@echo "✅ All 8 sections generated!"

# Section 1: Introduction
$(OUTPUT_DIR)/01_Introduction.md: generate_01_intro.py
	@echo "[Agent 1] Generating Introduction..."
	python generate_01_intro.py

# Section 2: Literature Review
$(OUTPUT_DIR)/02_LiteratureReview.md: generate_02_litreview.py
	@echo "[Agent 2] Generating Literature Review..."
	python generate_02_litreview.py

# Section 3: Conceptual Model
$(OUTPUT_DIR)/03_Conceptual_Model.md: generate_03_conceptual.py
	@echo "[Agent 3] Generating Conceptual Model..."
	python generate_03_conceptual.py

# Section 4: Methodology
$(OUTPUT_DIR)/04_Method.md: generate_04_method.py
	@echo "[Agent 4] Generating Methodology..."
	python generate_04_method.py

# Section 5: Results
$(OUTPUT_DIR)/05_Results.md: generate_05_results.py
	@echo "[Agent 5] Generating Results..."
	python generate_05_results.py

# Section 6: Discussion
$(OUTPUT_DIR)/06_Discussion.md: generate_06_discussion.py
	@echo "[Agent 6] Generating Discussion..."
	python generate_06_discussion.py

# Section 7: Poster
$(OUTPUT_DIR)/07_Poster.svg: generate_07_poster.py
	@echo "[Agent 7] Generating Poster..."
	python generate_07_poster.py

# Section 8: Industry Comparison
$(OUTPUT_DIR)/08_IndustryComparison.md: generate_08_industry_comparison.py
	@echo "[Agent 8] Generating Industry Comparison..."
	python generate_08_industry_comparison.py

# Clean output directory
clean:
	@echo "Cleaning output directory..."
	rm -rf $(OUTPUT_DIR)/*.md $(OUTPUT_DIR)/*.svg $(OUTPUT_DIR)/*.png
	@echo "✅ Cleaned!"

# Test all sections
test: all
	@echo "Testing outputs..."
	@ls -lh $(OUTPUT_DIR)/
	@echo "✅ Test complete!"
```

Usage:
```bash
cd src/scripts/paper_generation

# Run with 8 parallel jobs
make -j 8

# Clean and regenerate
make clean && make -j 8

# Test
make test
```

## Performance Comparison

| Method | Setup Time | Execution Time | Complexity |
|--------|------------|----------------|------------|
| Claude Code (Task tool) | Instant | ~5s total | Very Easy |
| Bash background jobs | Minimal | ~3s total | Easy |
| GNU Parallel | 1 min (install) | ~3s total | Easy |
| Python multiprocessing | 5 min (write script) | ~3s total | Medium |
| Make parallel | 10 min (write Makefile) | ~2s total | Medium |

## Recommendation

**For quick testing**: Use Method 1 (Claude Code) or Method 2 (Bash)

**For production/automation**: Use Method 5 (Make) - integrates well with existing pipelines

**For programmatic control**: Use Method 4 (Python multiprocessing)

## Agent Assignment Strategy

Each agent handles one section independently:

| Agent | Section | Script | Output | Dependencies |
|-------|---------|--------|--------|--------------|
| 🤖 Agent 1 | Introduction | `generate_01_intro.py` | `01_Introduction.md` | h1, h2 CSVs |
| 🤖 Agent 2 | Literature | `generate_02_litreview.py` | `02_LiteratureReview.md` | None |
| 🤖 Agent 3 | Conceptual | `generate_03_conceptual.py` | `03_Conceptual_Model.md` | analysis_panel.csv |
| 🤖 Agent 4 | Methodology | `generate_04_method.py` | `04_Method.md` | None |
| 🤖 Agent 5 | Results | `generate_05_results.py` | `05_Results.md` + PNG | h1, h2 CSVs, matplotlib |
| 🤖 Agent 6 | Discussion | `generate_06_discussion.py` | `06_Discussion.md` | None |
| 🤖 Agent 7 | Poster | `generate_07_poster.py` | `07_Poster.svg` + MD | h1, h2 CSVs |
| 🤖 Agent 8 | Industry | `generate_08_industry_comparison.py` | `08_IndustryComparison.md` | Industry CSVs |

## Resource Requirements

- **CPU**: 8 cores ideal (1 per agent), minimum 4 cores
- **Memory**: ~2GB total (250MB per agent)
- **Disk I/O**: Minimal (read CSVs, write MD files)
- **Time**: ~3-5 seconds with true parallelism

## Monitoring Parallel Execution

```bash
# Watch output directory in real-time
watch -n 0.5 'ls -lh output/ | tail -10'

# Monitor CPU usage
htop

# Check process count
ps aux | grep "generate_" | wc -l
```
