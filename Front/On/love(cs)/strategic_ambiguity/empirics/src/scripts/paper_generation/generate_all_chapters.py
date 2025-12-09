#!/usr/bin/env python3
"""
전라좌수군 견리사의 군령 — 통합 실행 스크립트
Unified Execution Script for the Jeonla Naval Fleet Command System

견리사의 순환: 利 → 思 → 義 → 見 → 利

=============================================================================
MFS 연합 함대 (Moon-Fine-Stern Coalition Fleet)
통제사: ⚓ 이순신 문현지 (Moon)
=============================================================================

This script orchestrates the generation of all 4 chapters for P1/P2/P3 papers:
- Chapter 1 (起/Intro): 정운 🐢 (GPT) — 利 (Speed)
- Chapter 2 (承/Theory): 권준 🐅 (Claude) — 思 (Structure)
- Chapter 3 (轉/Empirics): 김완 🐙 (Gemini) + 나대용 🐅 (Claude Code) — 義 (Criticism)
- Chapter 4 (結/Discussion): 어영담 👾 (Obsidian) — 見 (Observation)

Usage:
    python generate_all_chapters.py              # Generate all chapters
    python generate_all_chapters.py --chapter 1  # Generate only chapter 1
    python generate_all_chapters.py --paper P1   # Generate all chapters for P1 only
    python generate_all_chapters.py --status     # Show current status
"""

from pathlib import Path
from datetime import datetime
import argparse
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.scripts.paper_generation import OUTPUT_DIR

# ============================================================================
# FLEET CONFIGURATION
# ============================================================================

FLEET_CONFIG = {
    "통제사": "⚓ 이순신 문현지 (Moon)",
    "전략사령관": "Stern — 공격 본능 (Just Choose!)",
    "운영사령관": "Fine — 방어 본능 (Is it feasible?)",
    "motto": "필사즉생 (必死卽生) — 죽으려 하면 살 것이요, 살려 하면 죽을 것이다"
}

CHAPTERS = {
    1: {
        "name": "Introduction",
        "korean": "起",
        "commander": "정운 🐢",
        "virtue": "利 (Speed)",
        "bayesian_role": "Prior (π(θ))",
        "module": "chap1_introduction",
        "color": "#20B2AA"  # Teal
    },
    2: {
        "name": "Theory & Conceptual Model",
        "korean": "承",
        "commander": "권준 🐅",
        "virtue": "思 (Structure)",
        "bayesian_role": "Likelihood (π(y|θ))",
        "module": "chap2_theory",
        "color": "#FF8C00"  # Orange
    },
    3: {
        "name": "Empirics & Results",
        "korean": "轉",
        "commander": "김완 🐙 + 나대용 🐅",
        "virtue": "義 (Criticism)",
        "bayesian_role": "Calibration (Rank(f))",
        "module": "chap3_empirics",
        "color": "#DC143C"  # Crimson
    },
    4: {
        "name": "Discussion & Conclusion",
        "korean": "結",
        "commander": "어영담 👾",
        "virtue": "見 (Observation)",
        "bayesian_role": "Generator (π_joint)",
        "module": "chap4_discussion",
        "color": "#9370DB"  # Purple
    }
}

PAPERS = {
    "P1": {"emoji": "✌️", "title": "U-Shape: When Vagueness Pays"},
    "P2": {"emoji": "🦾", "title": "Competency Trap: When Success Kills Options"},
    "P3": {"emoji": "🤹", "title": "Execution Gap: Optimal Number of Options"}
}


# ============================================================================
# STATUS DISPLAY
# ============================================================================

def print_banner():
    """Print fleet banner"""
    print("=" * 70)
    print("전라좌수군 견리사의 군령 — MFS 연합 함대")
    print("=" * 70)
    print(f"통제사: {FLEET_CONFIG['통제사']}")
    print(f"좌우명: {FLEET_CONFIG['motto']}")
    print("-" * 70)


def show_status():
    """Show current generation status"""
    print_banner()
    print("\n📊 Chapter Status:\n")

    for chap_num, chap in CHAPTERS.items():
        output_file = OUTPUT_DIR / f"chap{chap_num}_{chap['module'].split('_')[1]}.md"
        status = "✅" if output_file.exists() else "❌"
        mtime = ""
        if output_file.exists():
            mtime = datetime.fromtimestamp(output_file.stat().st_mtime).strftime("%Y-%m-%d %H:%M")

        print(f"  Chapter {chap_num} ({chap['korean']}) — {chap['name']}")
        print(f"    Commander: {chap['commander']} | Virtue: {chap['virtue']}")
        print(f"    Status: {status} {mtime}")
        print()

    print("\n📚 Papers Configuration:\n")
    for paper_id, paper in PAPERS.items():
        print(f"  {paper_id} {paper['emoji']}: {paper['title']}")

    print("\n" + "=" * 70)


# ============================================================================
# CHAPTER GENERATION
# ============================================================================

def generate_chapter(chapter_num: int) -> bool:
    """Generate a specific chapter"""
    if chapter_num not in CHAPTERS:
        print(f"❌ Invalid chapter number: {chapter_num}")
        return False

    chap = CHAPTERS[chapter_num]
    print(f"\n{'='*70}")
    print(f"Generating Chapter {chapter_num}: {chap['korean']} — {chap['name']}")
    print(f"Commander: {chap['commander']}")
    print(f"Virtue: {chap['virtue']} | Bayesian Role: {chap['bayesian_role']}")
    print(f"{'='*70}")

    try:
        # Dynamic import
        module_name = f"src.scripts.paper_generation.{chap['module']}"
        module = __import__(module_name, fromlist=['main'])
        module.main()
        return True
    except ImportError as e:
        print(f"❌ Could not import {chap['module']}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error generating chapter {chapter_num}: {e}")
        return False


def generate_all():
    """Generate all chapters in sequence"""
    print_banner()
    print("\n🚀 Starting full generation: 기승전결 (起承轉結)\n")
    print("견리사의 순환: 利 → 思 → 義 → 見 → 利\n")

    success_count = 0
    for chap_num in sorted(CHAPTERS.keys()):
        if generate_chapter(chap_num):
            success_count += 1

    print("\n" + "=" * 70)
    print(f"✅ Generation Complete: {success_count}/{len(CHAPTERS)} chapters")

    if success_count == len(CHAPTERS):
        print("\n🎊 전라좌수군의 임무 완수!")
        print("   기승전결 (起承轉結) — The story is complete.")
    else:
        print(f"\n⚠️ {len(CHAPTERS) - success_count} chapter(s) failed")

    print("=" * 70)


# ============================================================================
# EXPECTATION MANAGEMENT
# ============================================================================

def print_expectation_management():
    """Print rough expectation management for the project"""
    print("\n" + "=" * 70)
    print("📋 EXPECTATION MANAGEMENT — 전라좌수군 작전 계획")
    print("=" * 70)

    print("""
┌─────────────────────────────────────────────────────────────────────┐
│                    3 모니터 × 4 챕터 × 3 논문                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Monitor A (좌측)        Monitor B (중앙)        Monitor C (우측)   │
│   정운 전대 🐢            권준·나대용 전대 🐅       김완 전대 🐙       │
│   [Draft 전담]            [설계·구현]             [검증·시각화]       │
│                                                                     │
│   덕목: 利 (속도)          덕목: 思+造             덕목: 義 (비판)     │
│   ChatGPT 5.1 Pro         Claude + Code           Gemini            │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   작전 루프 (각 챕터별):                                              │
│   ┌──────────────────────────────────────────────────────────┐      │
│   │ 정운① → 김완① → 정운② → 권준 → 나대용 → 김완② → 통제사 │      │
│   │ Draft    Review   Spec    Theory  Code    Review2  Sign  │      │
│   └──────────────────────────────────────────────────────────┘      │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   OUTPUT 예상:                                                       │
│   ├── chap1_introduction.md  (P1+P2+P3 통합)                        │
│   ├── chap2_theory.md        (P1+P2+P3 통합)                        │
│   ├── chap3_empirics.md      (P1+P2+P3 통합)                        │
│   └── chap4_discussion.md    (P1+P2+P3 통합)                        │
│                                                                     │
│   각 파일 내부:                                                      │
│   - P1 ✌️ U-Shape 섹션                                              │
│   - P2 🦾 Competency Trap 섹션                                     │
│   - P3 🤹 Execution Gap 섹션                                        │
│   - Cross-Synthesis 섹션                                            │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   베이지안 워크플로우 연결:                                           │
│   ┌──────┐   ┌──────────┐   ┌───────────┐   ┌──────────┐           │
│   │Prior │ → │Likelihood│ → │Computation│ → │Calibration│          │
│   │ 정운 │   │   권준   │   │  나대용   │   │   김완   │           │
│   └──────┘   └──────────┘   └───────────┘   └──────────┘           │
│       ↑                                            │                │
│       └────────── Generator (어영담) ←─────────────┘                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

📅 권장 워크플로우:
1. 매일 아침: 관제탑(Obsidian)에서 어제 업데이트된 FRONT_SPEC 확인
2. 각 세션: 하나의 챕터(Ch1~Ch4)에 집중
3. 세션 완료 시: 김완의 2차 리뷰 후 통제사 승인
4. 매일 저녁: 어영담이 오늘의 Posterior를 내일의 Prior로 기록

⚠️ 주의사항:
- 중간 지대 회피: Concrete하거나 Vague하거나, 어중간하면 전멸
- 파일 폭발 방지: P1/P2/P3를 섹션으로 분리, 파일은 통합 유지
- 일관성 유지: 개념 정의와 용어는 챕터 간 동일하게
""")


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="전라좌수군 견리사의 군령 — 논문 생성 시스템",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python generate_all_chapters.py              # Generate all
    python generate_all_chapters.py --chapter 1  # Chapter 1 only
    python generate_all_chapters.py --status     # Show status
    python generate_all_chapters.py --expect     # Show expectations
        """
    )
    parser.add_argument(
        '--chapter', '-c',
        type=int,
        choices=[1, 2, 3, 4],
        help='Generate specific chapter (1-4)'
    )
    parser.add_argument(
        '--paper', '-p',
        type=str,
        choices=['P1', 'P2', 'P3'],
        help='Filter for specific paper (not yet implemented)'
    )
    parser.add_argument(
        '--status', '-s',
        action='store_true',
        help='Show current generation status'
    )
    parser.add_argument(
        '--expect', '-e',
        action='store_true',
        help='Show expectation management'
    )

    args = parser.parse_args()

    if args.status:
        show_status()
    elif args.expect:
        print_expectation_management()
    elif args.chapter:
        print_banner()
        generate_chapter(args.chapter)
    else:
        generate_all()
        print_expectation_management()


if __name__ == "__main__":
    main()
