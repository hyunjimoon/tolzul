#!/usr/bin/env python3
"""
전라좌수군 견리사의 군령 — 전체 테스트 파이프라인
Complete Test Pipeline Runner

핵심 정신: 일관성 검증의 자동화
Core Spirit: Automated Consistency Verification

실행 방법:
    python run_all_tests.py              # 전체 테스트 실행
    python run_all_tests.py --verbose    # 상세 출력
    python run_all_tests.py --quick      # 빠른 테스트만
    python run_all_tests.py --report     # HTML 리포트 생성

=============================================================================
통제사: ⚓ 이순신 문현지 (Moon)
=============================================================================
"""

import argparse
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Tuple, Optional
import json

# Base paths
TEST_ROOT = Path(__file__).resolve().parent
EMPIRICS_ROOT = TEST_ROOT.parent
UNIT_TEST_DIR = TEST_ROOT / "unit"


# ============================================================================
# FLEET CONFIGURATION
# ============================================================================

FLEET_CONFIG = {
    "통제사": "⚓ 이순신 문현지 (Moon)",
    "motto": "필사즉생 (必死卽生) — 죽으려 하면 살 것이요, 살려 하면 죽을 것이다",
    "test_philosophy": "見利思義 — 이익을 보면 의로움을 생각하라"
}

TEST_MODULES = {
    "hypothesis_consistency": {
        "name": "가설-구현 일관성",
        "file": "test_hypothesis_consistency.py",
        "commander": "김완 🐙",
        "priority": 1,
        "description": "V² → V(1-V) 수식 일관성 검증"
    },
    "vagueness_scorer": {
        "name": "Vagueness 스코어러",
        "file": "test_vagueness_scorer.py",
        "commander": "김완 🐙",
        "priority": 2,
        "description": "스코어링 알고리즘 정확성 검증"
    },
    "models_consistency": {
        "name": "회귀모형 일관성",
        "file": "test_models_consistency.py",
        "commander": "나대용 🐅",
        "priority": 1,
        "description": "회귀 수식과 가설 일치 검증"
    },
    "plotting_consistency": {
        "name": "시각화 일관성",
        "file": "test_plotting_consistency.py",
        "commander": "어영담 👾",
        "priority": 3,
        "description": "플롯이 가설을 정확히 반영하는지 검증"
    }
}


# ============================================================================
# BANNER
# ============================================================================

def print_banner():
    """Print fleet banner"""
    print("=" * 70)
    print("전라좌수군 견리사의 군령 — 테스트 파이프라인")
    print("Test Pipeline for PhD Thesis Paper Generation System")
    print("=" * 70)
    print(f"통제사: {FLEET_CONFIG['통제사']}")
    print(f"좌우명: {FLEET_CONFIG['motto']}")
    print(f"테스트 철학: {FLEET_CONFIG['test_philosophy']}")
    print("-" * 70)
    print(f"실행 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)


# ============================================================================
# TEST RUNNER
# ============================================================================

class TestRunner:
    """Test pipeline runner"""

    def __init__(self, verbose: bool = False, quick: bool = False):
        self.verbose = verbose
        self.quick = quick
        self.results: List[Tuple[str, bool, str]] = []

    def run_single_test(self, module_key: str) -> Tuple[bool, str]:
        """
        Run a single test module

        Returns:
            (success: bool, output: str)
        """
        if module_key not in TEST_MODULES:
            return False, f"Unknown test module: {module_key}"

        module = TEST_MODULES[module_key]
        test_file = UNIT_TEST_DIR / module["file"]

        if not test_file.exists():
            return False, f"Test file not found: {test_file}"

        print(f"\n{'='*60}")
        print(f"🧪 {module['name']} ({module['commander']})")
        print(f"   {module['description']}")
        print(f"{'='*60}")

        # Build pytest command
        cmd = [sys.executable, "-m", "pytest", str(test_file)]

        if self.verbose:
            cmd.extend(["-v", "--tb=short"])
        else:
            cmd.extend(["-q", "--tb=line"])

        if self.quick:
            cmd.extend(["-x"])  # Stop on first failure

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=str(EMPIRICS_ROOT),
                timeout=120
            )

            output = result.stdout + result.stderr
            success = result.returncode == 0

            if self.verbose:
                print(output)
            else:
                # Print summary
                if success:
                    print("✅ PASSED")
                else:
                    print("❌ FAILED")
                    # Print failure details
                    for line in output.split('\n'):
                        if 'FAILED' in line or 'Error' in line:
                            print(f"   {line}")

            return success, output

        except subprocess.TimeoutExpired:
            return False, "Test timed out after 120 seconds"
        except Exception as e:
            return False, f"Error running test: {e}"

    def run_all_tests(self) -> bool:
        """
        Run all tests in priority order

        Returns:
            True if all tests passed
        """
        print_banner()

        # Sort by priority
        sorted_modules = sorted(
            TEST_MODULES.items(),
            key=lambda x: x[1]["priority"]
        )

        all_passed = True

        for module_key, module in sorted_modules:
            success, output = self.run_single_test(module_key)
            self.results.append((module_key, success, output))

            if not success:
                all_passed = False

                if self.quick:
                    print("\n⚠️ Quick mode: Stopping on first failure")
                    break

        self.print_summary()
        return all_passed

    def print_summary(self):
        """Print test summary"""
        print("\n" + "=" * 70)
        print("📊 TEST SUMMARY")
        print("=" * 70)

        passed = sum(1 for _, success, _ in self.results if success)
        total = len(self.results)

        for module_key, success, _ in self.results:
            module = TEST_MODULES[module_key]
            status = "✅" if success else "❌"
            print(f"  {status} {module['name']} ({module['commander']})")

        print("-" * 70)
        print(f"  총 결과: {passed}/{total} passed")

        if passed == total:
            print("\n🎊 전라좌수군의 임무 완수!")
            print("   모든 테스트 통과 — 일관성 검증 완료")
        else:
            print(f"\n⚠️ {total - passed} 테스트 실패")
            print("   위 실패 항목을 확인하고 수정하세요")

        print("=" * 70)

    def generate_html_report(self, output_path: Optional[Path] = None) -> Path:
        """Generate HTML test report"""
        if output_path is None:
            output_path = TEST_ROOT / "reports" / f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

        output_path.parent.mkdir(parents=True, exist_ok=True)

        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>전라좌수군 견리사의 군령 — 테스트 리포트</title>
    <style>
        body {{ font-family: 'Noto Sans KR', sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #2c3e50; }}
        .passed {{ color: #27ae60; }}
        .failed {{ color: #e74c3c; }}
        .test-module {{ border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }}
        .summary {{ background: #f8f9fa; padding: 20px; border-radius: 5px; }}
        pre {{ background: #2d2d2d; color: #f8f8f2; padding: 15px; overflow-x: auto; }}
    </style>
</head>
<body>
    <h1>전라좌수군 견리사의 군령 — 테스트 리포트</h1>
    <p>생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

    <div class="summary">
        <h2>요약</h2>
        <p>통과: {sum(1 for _, s, _ in self.results if s)} / {len(self.results)}</p>
    </div>

    <h2>상세 결과</h2>
"""

        for module_key, success, output in self.results:
            module = TEST_MODULES[module_key]
            status_class = "passed" if success else "failed"
            status_icon = "✅" if success else "❌"

            html_content += f"""
    <div class="test-module">
        <h3 class="{status_class}">{status_icon} {module['name']} ({module['commander']})</h3>
        <p>{module['description']}</p>
        <details>
            <summary>상세 출력</summary>
            <pre>{output}</pre>
        </details>
    </div>
"""

        html_content += """
</body>
</html>
"""

        output_path.write_text(html_content, encoding='utf-8')
        print(f"\n📄 HTML 리포트 생성: {output_path}")

        return output_path

    def generate_json_report(self, output_path: Optional[Path] = None) -> Path:
        """Generate JSON test report for CI integration"""
        if output_path is None:
            output_path = TEST_ROOT / "reports" / f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        output_path.parent.mkdir(parents=True, exist_ok=True)

        report = {
            "timestamp": datetime.now().isoformat(),
            "fleet_config": FLEET_CONFIG,
            "summary": {
                "total": len(self.results),
                "passed": sum(1 for _, s, _ in self.results if s),
                "failed": sum(1 for _, s, _ in self.results if not s)
            },
            "tests": []
        }

        for module_key, success, output in self.results:
            module = TEST_MODULES[module_key]
            report["tests"].append({
                "key": module_key,
                "name": module["name"],
                "commander": module["commander"],
                "priority": module["priority"],
                "success": success,
                "output_length": len(output)
            })

        output_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"📄 JSON 리포트 생성: {output_path}")

        return output_path


# ============================================================================
# CONSISTENCY CHECK (Quick Pre-flight)
# ============================================================================

def run_consistency_check() -> bool:
    """
    Quick consistency check without full pytest

    Checks:
    1. V² vs V(1-V) formula alignment
    2. P1/P2/P3 domain consistency
    3. Emoji consistency
    """
    print("\n🔍 Quick Consistency Check")
    print("-" * 40)

    issues = []

    # Check chap2_theory.py for V(1-V)
    theory_file = EMPIRICS_ROOT / "src" / "scripts" / "paper_generation" / "chap2_theory.py"
    if theory_file.exists():
        content = theory_file.read_text()
        if "V(1-V)" in content:
            print("  ✅ H1 uses V(1-V) in theory")
        elif "V²" in content or "V**2" in content:
            issues.append("Theory still uses old V² formula")
            print("  ❌ Theory uses old V² formula")
    else:
        print("  ⚠️ chap2_theory.py not found")

    # Check models.py for U-shape term
    models_file = EMPIRICS_ROOT / "src" / "models.py"
    if models_file.exists():
        content = models_file.read_text()
        has_ushape = any(p in content for p in ["vagueness_ushape", "vagueness_squared", "**2"])
        if has_ushape:
            print("  ✅ models.py has U-shape term")
        else:
            issues.append("models.py missing U-shape term (vagueness_ushape or vagueness**2)")
            print("  ⚠️ models.py missing U-shape term")
    else:
        print("  ⚠️ models.py not found")

    # Check emoji consistency
    for chap_file in (EMPIRICS_ROOT / "src" / "scripts" / "paper_generation").glob("chap*.py"):
        content = chap_file.read_text()
        if "🕳️" in content or "🪾" in content or "🧩" in content:  # Old emojis
            issues.append(f"{chap_file.name} still has old emoji (should be 🦾 for P2, 🤹 for P3)")
            print(f"  ❌ {chap_file.name} has old emoji")

    print("-" * 40)
    if issues:
        print(f"Found {len(issues)} consistency issue(s)")
        return False
    else:
        print("✅ Quick consistency check passed")
        return True


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="전라좌수군 견리사의 군령 — 테스트 파이프라인",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python run_all_tests.py              # Run all tests
    python run_all_tests.py --verbose    # Verbose output
    python run_all_tests.py --quick      # Stop on first failure
    python run_all_tests.py --check      # Quick consistency check only
    python run_all_tests.py --report     # Generate HTML report
    python run_all_tests.py --module hypothesis_consistency  # Run single module
        """
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    parser.add_argument(
        '--quick', '-q',
        action='store_true',
        help='Stop on first failure'
    )
    parser.add_argument(
        '--check', '-c',
        action='store_true',
        help='Quick consistency check only (no pytest)'
    )
    parser.add_argument(
        '--report', '-r',
        action='store_true',
        help='Generate HTML report after tests'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Generate JSON report (for CI)'
    )
    parser.add_argument(
        '--module', '-m',
        type=str,
        choices=list(TEST_MODULES.keys()),
        help='Run specific test module'
    )
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List available test modules'
    )

    args = parser.parse_args()

    # List modules
    if args.list:
        print("\n📋 Available Test Modules:\n")
        for key, module in TEST_MODULES.items():
            print(f"  {key}")
            print(f"    Name: {module['name']}")
            print(f"    Commander: {module['commander']}")
            print(f"    Description: {module['description']}")
            print()
        return 0

    # Quick check only
    if args.check:
        success = run_consistency_check()
        return 0 if success else 1

    # Run tests
    runner = TestRunner(verbose=args.verbose, quick=args.quick)

    if args.module:
        # Run single module
        print_banner()
        success, _ = runner.run_single_test(args.module)
        runner.results.append((args.module, success, ""))
        runner.print_summary()
    else:
        # Run all tests
        success = runner.run_all_tests()

    # Generate reports
    if args.report:
        runner.generate_html_report()
    if args.json:
        runner.generate_json_report()

    return 0 if all(s for _, s, _ in runner.results) else 1


if __name__ == "__main__":
    sys.exit(main())
