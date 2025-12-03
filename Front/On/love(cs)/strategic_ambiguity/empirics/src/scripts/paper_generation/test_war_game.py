import unittest
import subprocess
import json
import os
from pathlib import Path

class TestWarGame(unittest.TestCase):
    def setUp(self):
        self.cwd = Path(__file__).parent
        self.output_dir = self.cwd / "output"
        self.report_file = self.cwd / "critique_report.json"
        self.dashboard_file = self.cwd / "battle_dashboard.html"

    def test_01_run_critique(self):
        """Run critique_spaceship.py and check exit code"""
        print("\n🚀 Running Critique Spaceship...")
        result = subprocess.run(["python3", "critique_spaceship.py"], cwd=self.cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stderr)
        self.assertEqual(result.returncode, 0, f"Critique script failed")
        self.assertTrue(self.report_file.exists(), "Critique report not generated")

    def test_02_verify_nuanced_critique(self):
        """Verify U and N get different critiques (Kim Agents)"""
        with open(self.report_file, 'r') as f:
            data = json.load(f)
        
        # Check U-Shaped Empirics (Should check for Entrepreneurship)
        u_file = "chap3_U_empirics.md"
        if u_file in data:
            critiques = str(data[u_file]["critiques"])
            # It might pass if content is good, but if it fails, it MUST be Kim U
            if "Missing" in critiques and "keywords" in critiques:
                self.assertIn("Kim U", critiques, "U-file should be critiqued by Kim U")
                self.assertNotIn("Kim N", critiques, "U-file should NOT be critiqued by Kim N")

        # Check Newsvendor Empirics (Should check for Operations)
        n_file = "chap3_N_empirics.md"
        if n_file in data:
            critiques = str(data[n_file]["critiques"])
            if "Missing" in critiques and "keywords" in critiques:
                self.assertIn("Kim N", critiques, "N-file should be critiqued by Kim N")
                self.assertNotIn("Kim U", critiques, "N-file should NOT be critiqued by Kim U")
        
        print("✅ Verified nuanced critique logic (Kim U vs Kim N)")

    def test_03_run_dashboard(self):
        """Run visualize_spaceship.py and check exit code"""
        print("🎨 Running Dashboard Generator...")
        result = subprocess.run(["python3.11", "visualize_spaceship.py"], cwd=self.cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stderr)
        self.assertEqual(result.returncode, 0, f"Dashboard script failed")
        self.assertTrue(self.dashboard_file.exists(), "Dashboard HTML not generated")

    def test_04_verify_dashboard_content(self):
        """Verify deputies, links, and responsiveness"""
        content = self.dashboard_file.read_text(encoding='utf-8')
        
        # 1. Verify Deputies (Jeong, Na, Kim)
        deputies = [
            "J-Intro", "J-Theory", "J-Empirics", "J-Discuss",
            "N-Intro", "N-Theory", "N-Empirics", "N-Discuss",
            "K-Ushape", "K-Commit", "K-News"
        ]
        for dep in deputies:
            self.assertIn(dep, content, f"Deputy {dep} missing from dashboard")
            
        # 2. Verify Command Links
        self.assertIn("onclick=\"openFile", content, "Command links (openFile) missing")
        
        # 3. Verify Mobile Responsiveness
        self.assertIn('<meta name="viewport"', content, "Viewport meta tag missing")
        self.assertIn('@media', content, "Media queries missing")
        
        # 4. Verify Risk Indicators from Critique
        self.assertTrue("risk-0" in content or "risk-1" in content or "risk-2" in content, "Risk indicators missing")
        
        # 5. Verify Tooltips (Solution #1)
        self.assertIn('title="', content, "Tooltips missing")
        # Check for at least one specific critique in a tooltip if possible, or just the structure
        if "risk-3" in content or "risk-2" in content:
            self.assertIn('❌', content, "Critique icons (❌) missing from tooltips")
        
        print("✅ Verified Dashboard Content (Deputies, Links, Mobile, Tooltips)")

if __name__ == '__main__':
    unittest.main(verbosity=2)
