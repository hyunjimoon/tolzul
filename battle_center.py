#!/usr/bin/env python3
"""
Battle Control Center (전투 지휘소)
=================================

Visualizes the Battle Logs (전투일지) as a real-time command center.
Reports to the 4 Generals:
1. Kwon Jun (Strategy): Plans & Status
2. Jeong Un (Execution): Work Log & Actions
3. Kim Wan (Validation): Blockers & Learnings
4. Eo Young-dam (Navigation): Next Steps & Roadmap
"""

import re
import sys
from pathlib import Path
from datetime import datetime

# --- Configuration ---
BASE_DIR = Path("/Users/hyunjimoon/tolzul")
LOG_FILE_MAIN = BASE_DIR / "Front/On/love(cs)/strategic_ambiguity/전투일지🩸.md"
LOG_FILE_APPEND = BASE_DIR / "Front/On/love(cs)/strategic_ambiguity/전투일지🩸_week4_append.md"
OUTPUT_FILE = BASE_DIR / "battle_dashboard.html"

# --- Persona Mapping ---
PERSONAS = {
    "Kwon Jun": {
        "role": "Strategy (중군장)",
        "icon": "🐅",
        "color": "#ffcc00", # Gold
        "sections": ["아침 계획", "전체 진행상황", "Week", "목표"]
    },
    "Jeong Un": {
        "role": "Execution (좌수사)",
        "icon": "🐙",
        "color": "#ff3333", # Red
        "sections": ["작업 로그", "완료한 것", "완료", "실행"]
    },
    "Kim Wan": {
        "role": "Validation (우수사)",
        "icon": "🐢",
        "color": "#33cc33", # Green
        "sections": ["막혔던 것", "배운 것", "이슈", "검증"]
    },
    "Eo Young-dam": {
        "role": "Navigation (항해장)",
        "icon": "🌊",
        "color": "#3399ff", # Blue
        "sections": ["내일", "다음 주", "Week 5", "인계"]
    }
}

def parse_latest_log(file_paths):
    """
    Parses the latest daily log from the given files.
    Returns a dictionary mapped to personas.
    """
    all_content = ""
    for fp in file_paths:
        if fp.exists():
            with open(fp, 'r', encoding='utf-8') as f:
                all_content += "\n" + f.read()
    
    # Find all "Day X" headers
    # Format: ## 🗓️ Day 26 - 2025.11.24 (일)
    day_pattern = r"## 🗓️ Day (\d+) - (\d{4}\.\d{2}\.\d{2})"
    matches = list(re.finditer(day_pattern, all_content))
    
    if not matches:
        return None, "No daily logs found."
    
    # Get the last match (latest day)
    last_match = matches[-1]
    day_num = last_match.group(1)
    date_str = last_match.group(2)
    start_idx = last_match.start()
    
    # Extract content until next header or end
    content_after = all_content[start_idx:]
    # Find next "## " to cut off
    next_header = re.search(r"\n## ", content_after[5:]) # Skip the current header
    
    if next_header:
        daily_content = content_after[:next_header.start() + 5]
    else:
        daily_content = content_after
        
    print(f"⚔️  Parsing Log for Day {day_num} ({date_str})...")
    
    # Map content to personas
    report = {name: [] for name in PERSONAS}
    
    # Split by sub-headers (### )
    sections = re.split(r"\n### ", daily_content)
    
    for section in sections:
        lines = section.strip().split('\n')
        header = lines[0].strip()
        body = '\n'.join(lines[1:]).strip()
        
        if not body: continue
        
        # Assign to persona based on keywords
        assigned = False
        for name, info in PERSONAS.items():
            for keyword in info['sections']:
                if keyword in header:
                    report[name].append(f"<h4>{header}</h4>\n<div class='content-block'>{markdown_to_html(body)}</div>")
                    assigned = True
                    break
            if assigned: break
        
        # Default fallback (if not matched) -> Jeong Un (Execution)
        if not assigned and header and "Day" not in header:
             report["Jeong Un"].append(f"<h4>{header}</h4>\n<div class='content-block'>{markdown_to_html(body)}</div>")

    return f"Day {day_num} ({date_str})", report

def markdown_to_html(text):
    """Simple markdown to HTML converter."""
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Code blocks
    text = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', text, flags=re.DOTALL)
    # Lists
    text = re.sub(r'^\s*-\s+(.*)', r'<li>\1</li>', text, flags=re.MULTILINE)
    # Wrap lists (simple heuristic)
    text = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', text, flags=re.DOTALL) # This is too greedy, but okay for simple view
    # Fix greedy ul - actually let's just leave lis, browser handles them okay-ish or we style them
    # Better: just replace - with • for visual
    return text.replace('\n', '<br>')

def generate_dashboard(title, report):
    """Generates the HTML dashboard."""
    
    html = f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Battle Control Center: {title}</title>
        <style>
            body {{
                background-color: #0a0a0a;
                color: #e0e0e0;
                font-family: 'Courier New', monospace;
                margin: 0;
                padding: 20px;
                background-image: linear-gradient(rgba(0, 20, 0, 0.2) 1px, transparent 1px),
                                  linear-gradient(90deg, rgba(0, 20, 0, 0.2) 1px, transparent 1px);
                background-size: 20px 20px;
            }}
            h1 {{
                text-align: center;
                color: #ff3333;
                text-shadow: 0 0 10px #ff0000;
                border-bottom: 2px solid #ff3333;
                padding-bottom: 10px;
                margin-bottom: 30px;
                text-transform: uppercase;
                letter-spacing: 5px;
            }}
            .grid-container {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                grid-template-rows: 1fr 1fr;
                gap: 20px;
                height: 85vh;
            }}
            .panel {{
                background-color: rgba(20, 20, 20, 0.8);
                border: 1px solid #444;
                padding: 20px;
                overflow-y: auto;
                box-shadow: 0 0 15px rgba(0,0,0,0.5);
                position: relative;
            }}
            .panel::before {{
                content: '';
                position: absolute;
                top: 0; left: 0; right: 0; bottom: 0;
                border: 1px solid transparent;
                
            }}
            .panel-header {{
                display: flex;
                align-items: center;
                border-bottom: 1px solid #555;
                padding-bottom: 10px;
                margin-bottom: 15px;
            }}
            .icon {{
                font-size: 2em;
                margin-right: 15px;
            }}
            .role {{
                font-size: 0.8em;
                opacity: 0.7;
                text-transform: uppercase;
            }}
            .name {{
                font-size: 1.5em;
                font-weight: bold;
            }}
            .content-block {{
                margin-bottom: 15px;
                line-height: 1.6;
            }}
            h4 {{
                color: #aaa;
                margin-bottom: 5px;
                border-left: 3px solid #555;
                padding-left: 10px;
            }}
            ul {{ padding-left: 20px; }}
            li {{ margin-bottom: 5px; }}
            pre {{
                background: #111;
                padding: 10px;
                border: 1px solid #333;
                white-space: pre-wrap;
            }}
            
            /* Specific Panel Colors */
            .panel-kwon {{ border-color: {PERSONAS['Kwon Jun']['color']}; }}
            .panel-kwon h4 {{ border-left-color: {PERSONAS['Kwon Jun']['color']}; }}
            
            .panel-jeong {{ border-color: {PERSONAS['Jeong Un']['color']}; }}
            .panel-jeong h4 {{ border-left-color: {PERSONAS['Jeong Un']['color']}; }}
            
            .panel-kim {{ border-color: {PERSONAS['Kim Wan']['color']}; }}
            .panel-kim h4 {{ border-left-color: {PERSONAS['Kim Wan']['color']}; }}
            
            .panel-eo {{ border-color: {PERSONAS['Eo Young-dam']['color']}; }}
            .panel-eo h4 {{ border-left-color: {PERSONAS['Eo Young-dam']['color']}; }}

            .music-player {{
                position: fixed;
                bottom: 20px;
                right: 20px;
                opacity: 0.5;
            }}
            .music-player:hover {{ opacity: 1; }}
        </style>
    </head>
    <body>
        <h1>⚔️ Battle Control Center: {title}</h1>
        
        <div class="grid-container">
            <!-- Kwon Jun (Strategy) -->
            <div class="panel panel-kwon">
                <div class="panel-header" style="color: {PERSONAS['Kwon Jun']['color']}">
                    <span class="icon">{PERSONAS['Kwon Jun']['icon']}</span>
                    <div>
                        <div class="role">{PERSONAS['Kwon Jun']['role']}</div>
                        <div class="name">Kwon Jun</div>
                    </div>
                </div>
                {''.join(report['Kwon Jun']) if report['Kwon Jun'] else "<em>No strategic updates.</em>"}
            </div>

            <!-- Jeong Un (Execution) -->
            <div class="panel panel-jeong">
                <div class="panel-header" style="color: {PERSONAS['Jeong Un']['color']}">
                    <span class="icon">{PERSONAS['Jeong Un']['icon']}</span>
                    <div>
                        <div class="role">{PERSONAS['Jeong Un']['role']}</div>
                        <div class="name">Jeong Un</div>
                    </div>
                </div>
                {''.join(report['Jeong Un']) if report['Jeong Un'] else "<em>No execution logs.</em>"}
            </div>

            <!-- Kim Wan (Validation) -->
            <div class="panel panel-kim">
                <div class="panel-header" style="color: {PERSONAS['Kim Wan']['color']}">
                    <span class="icon">{PERSONAS['Kim Wan']['icon']}</span>
                    <div>
                        <div class="role">{PERSONAS['Kim Wan']['role']}</div>
                        <div class="name">Kim Wan</div>
                    </div>
                </div>
                {''.join(report['Kim Wan']) if report['Kim Wan'] else "<em>No validation issues.</em>"}
            </div>

            <!-- Eo Young-dam (Navigation) -->
            <div class="panel panel-eo">
                <div class="panel-header" style="color: {PERSONAS['Eo Young-dam']['color']}">
                    <span class="icon">{PERSONAS['Eo Young-dam']['icon']}</span>
                    <div>
                        <div class="role">{PERSONAS['Eo Young-dam']['role']}</div>
                        <div class="name">Eo Young-dam</div>
                    </div>
                </div>
                {''.join(report['Eo Young-dam']) if report['Eo Young-dam'] else "<em>No navigation data.</em>"}
            </div>
        </div>

        <!-- Audio: Epic War Drums -->
        <div class="music-player">
            <iframe width="300" height="80" src="https://www.youtube.com/embed/1Dq057C0xJ0?autoplay=1&loop=1&playlist=1Dq057C0xJ0" 
            title="War Drums" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
    </body>
    </html>
    """
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Battle Dashboard generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    title, report = parse_latest_log([LOG_FILE_MAIN, LOG_FILE_APPEND])
    if title:
        generate_dashboard(title, report)
    else:
        print("Failed to generate dashboard.")
