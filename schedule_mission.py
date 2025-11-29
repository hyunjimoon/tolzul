import os
import sys
from pathlib import Path
import subprocess

# Configuration
LABEL = "com.hyunjimoon.tolzul.mission"
BASE_DIR = Path("/Users/hyunjimoon/tolzul")
SCRIPT_PATH = BASE_DIR / "run_daily_mission.sh"
PLIST_DIR = Path.home() / "Library/LaunchAgents"
PLIST_PATH = PLIST_DIR / f"{LABEL}.plist"

def create_plist():
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{LABEL}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{SCRIPT_PATH}</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>{BASE_DIR}/launchd_stdout.log</string>
    <key>StandardErrorPath</key>
    <string>{BASE_DIR}/launchd_stderr.log</string>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
"""
    
    # Ensure directory exists
    PLIST_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(PLIST_PATH, 'w') as f:
        f.write(plist_content)
    
    print(f"📝 Created plist at: {PLIST_PATH}")

def load_job():
    # Unload if exists
    try:
        subprocess.run(["launchctl", "unload", str(PLIST_PATH)], check=False, capture_output=True)
    except Exception:
        pass

    # Load
    try:
        subprocess.run(["launchctl", "load", str(PLIST_PATH)], check=True)
        print(f"🚀 Job '{LABEL}' loaded successfully!")
        print("   - Scheduled for: Daily at 09:00 AM")
        print("   - RunAtLoad: True (Will run immediately for testing)")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to load job: {e}")

if __name__ == "__main__":
    print("🕒 Setting up Daily Mission Schedule...")
    create_plist()
    load_job()
