#!/usr/bin/env python3
"""
Scale Dashboard Generator
=========================
Generates the 'Scale Control Tower' dashboard based on the architecture defined in ARCHITECTURE.md.
Reads data from json files in ./data/ and outputs scale_dashboard.html.
"""

import json
import os
from pathlib import Path
import datetime

# Configuration
CURRENT_DIR = Path(__file__).parent.resolve()
DATA_DIR = CURRENT_DIR / "data"
OUTPUT_FILE = CURRENT_DIR / "scale_dashboard.html"

def load_json(filename):
    path = DATA_DIR / filename
    if not path.exists():
        print(f"Warning: {filename} not found at {path}")
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return {}


def get_obsidian_url(path_suffix):
    """Generates an Obsidian URL for a given relative path."""
    # Base path relative to vault root
    # Vault: tolzul
    # Root: /Users/hyunjimoon/tolzul
    base_path = "Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output"
    full_path = f"{base_path}/{path_suffix}"
    
    # URL Encode
    import urllib.parse
    encoded_path = urllib.parse.quote(full_path)
    
    return f"obsidian://open?vault=tolzul&file={encoded_path}"

def generate_production_matrix(paragraphs_data):
    html = """
    <div class="panel production-matrix">
        <div class="panel-header">📊 PRODUCTION MATRIX</div>
        <div class="matrix-grid">
            <div class="matrix-header">
                <div class="col-group">GROUP</div>
                <div class="col-sect">I</div>
                <div class="col-sect">T</div>
                <div class="col-sect">E</div>
                <div class="col-sect">D</div>
                <div class="col-verify">✓</div>
                <div class="col-progress">Progress</div>
            </div>
    """
    
    for group in paragraphs_data.get("groups", []):
        # Determine file paths based on group ID
        paths = {"I": "", "T": "", "E": "", "D": ""}
        
        if group["id"] == "intro":
            paths["I"] = "_🩸I/_🩸I.md"
            paths["D"] = "_🐣D/🐣D.md" # Using D folder for Intro group's D section as per request logic? Or maybe Intro has its own D? 
            # Re-reading request: 
            # /.../output/_🐣D/🐣D.md
            # /.../output/_🩸I/_🩸I.md
            # So Intro group likely maps to _🩸I and _🐣D for I and D respectively?
            # Let's assume Intro row I -> _🩸I/_🩸I.md, D -> _🐣D/🐣D.md (since Discussion group is separate)
            # Actually, looking at the groups: Intro, U, C, N, Discussion.
            # The user listed:
            # _🐣D/🐣D.md -> Likely for Discussion group
            # _🩸I/_🩸I.md -> Likely for Intro group
            pass
        elif group["id"] == "u":
            paths["I"] = "✌️U/📝product/chap1_intro.md"
            paths["T"] = "✌️U/📝product/chap2_theory.md"
            paths["E"] = "✌️U/📝product/chap3_empirics.md"
            paths["D"] = "✌️U/📝product/chap4_discussion.md"
        elif group["id"] == "c":
            paths["I"] = "🦾C/📝product/chap1_intro.md"
            paths["T"] = "🦾C/📝product/chap2_theory.md"
            paths["E"] = "🦾C/📝product/chap3_empirics.md"
            paths["D"] = "🦾C/📝product/chap4_discussion.md"
        elif group["id"] == "n":
            paths["I"] = "🤹N/📝product/chap1_intro.md"
            paths["T"] = "🤹N/📝product/chap2_theory.md"
            paths["E"] = "🤹N/📝product/chap3_empirics.md"
            paths["D"] = "🤹N/📝product/chap4_discussion.md"
        elif group["id"] == "disc":
             # Discussion group might map to _🐣D/🐣D.md
             paths["D"] = "_🐣D/🐣D.md"
             paths["I"] = "_🐣D/🐣D.md" # Just mapping D to D for now.
        
        # Override for Intro/Disc specific files from user request
        if group["id"] == "intro":
             paths["I"] = "_🩸I/_🩸I.md"
        if group["id"] == "disc":
             paths["D"] = "_🐣D/🐣D.md"

        # Dummy counts for display matching architecture
        counts = {"I": "-", "T": "-", "E": "-", "D": "-"}
        if group["id"] == "intro": counts = {"I": 4, "T": "-", "E": "-", "D": 3}
        elif group["id"] == "u": counts = {"I": 7, "T": 9, "E": 11, "D": 5}
        elif group["id"] == "c": counts = {"I": 7, "T": 9, "E": 11, "D": 5}
        elif group["id"] == "n": counts = {"I": 7, "T": 9, "E": 11, "D": 5}
        elif group["id"] == "disc": counts = {"I": 3, "T": "-", "E": "-", "D": 2}
        
        # Progress bar logic
        progress_pct = 0
        if group["id"] == "intro": progress_pct = 57
        elif group["id"] == "u": progress_pct = 25
        elif group["id"] == "c": progress_pct = 12
        
        verified = "●" if group["id"] in ["intro", "u"] else "○"
        verified_class = "verified-yes" if verified == "●" else "verified-no"
        
        # Helper to create cell
        def make_cell(sect):
            count = counts[sect]
            if count == "-": return f'<div class="col-sect">{count}</div>'
            
            path = paths.get(sect, "")
            if path:
                url = get_obsidian_url(path)
                return f'<div class="col-sect clickable" onclick="window.location.href=\'{url}\'">{count}</div>'
            else:
                return f'<div class="col-sect">{count}</div>'

        html += f"""
            <div class="matrix-row">
                <div class="col-group"><span class="group-icon">{group['icon']}</span> {group['name']}</div>
                {make_cell("I")}
                {make_cell("T")}
                {make_cell("E")}
                {make_cell("D")}
                <div class="col-verify {verified_class}">{verified}</div>
                <div class="col-progress">
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {progress_pct}%"></div>
                    </div>
                    <span class="progress-text">{progress_pct}%</span>
                </div>
            </div>
        """
        
    html += """
            <div class="matrix-footer">
                TOTAL: 23/108 ¶ (21%)
            </div>
        </div>
    </div>
    <style>
        .clickable { cursor: pointer; color: var(--accent-blue); text-decoration: underline; }
        .clickable:hover { color: #fff; }
    </style>
    """
    return html


def generate_asset_tracker(assets_data):
    html = """
    <div class="panel asset-tracker">
        <div class="panel-header">🎯 ASSETS</div>
        <div class="asset-section">
            <div class="asset-title">🖼️ Figures [3/8]</div>
            <ul class="asset-list">
    """
    
    for fig in assets_data.get("figures", []):
        status_icon = "■" if fig.get("status") == "done" else "□"
        status_class = "status-done" if fig.get("status") == "done" else "status-pending"
        html += f'<li class="asset-item {status_class}"><span class="asset-icon">{status_icon}</span> {fig["id"]}</li>'
        
    html += """
            </ul>
        </div>
        <div class="asset-section">
            <div class="asset-title">🗄️ Tables [2/5]</div>
            <ul class="asset-list">
    """
    
    for tbl in assets_data.get("tables", []):
        status_icon = "■" if tbl.get("status") == "done" else "□"
        status_class = "status-done" if tbl.get("status") == "done" else "status-pending"
        html += f'<li class="asset-item {status_class}"><span class="asset-icon">{status_icon}</span> {tbl["id"]}</li>'

    html += """
            </ul>
        </div>
    </div>
    """
    return html

def generate_diamond_flow(flow_data):
    current_task = flow_data.get("current_task", {})
    task_desc = f"Current: [{current_task.get('assignee', 'Unknown')}] → {current_task.get('target', 'Unknown')} 작업중"
    
    html = f"""
    <div class="panel diamond-flow">
        <div class="panel-header">💎 DIAMOND FLOW</div>
        <div class="flow-visual">
            <div class="flow-nodes">
                <div class="node node-m">
                    <div class="node-icon">🌙</div>
                    <div class="node-label">M</div>
                </div>
                <div class="arrow">▶</div>
                <div class="node node-g active">
                    <div class="node-icon">🟠</div>
                    <div class="node-label">G</div>
                </div>
                <div class="arrow">▶</div>
                <div class="node node-j">
                    <div class="node-icon">🟢</div>
                    <div class="node-label">J</div>
                </div>
                <div class="arrow">▶</div>
                <div class="node node-k">
                    <div class="node-icon">🔴</div>
                    <div class="node-label">K</div>
                </div>
            </div>
            <div class="flow-status">
                {task_desc}
            </div>
        </div>
    </div>
    """
    return html

def generate_issue_queue():
    # Hardcoded for now based on architecture example
    html = """
    <div class="panel issue-queue">
        <div class="panel-header">📋 ISSUE QUEUE (Scale Mode)</div>
        <table class="issue-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Target</th>
                    <th>Title</th>
                    <th>Stage</th>
                    <th>Next Action</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>#01</td>
                    <td>✌️U-T</td>
                    <td>D definition</td>
                    <td><span class="badge badge-merge">MERGE</span></td>
                    <td><button class="btn-action">🇰🇷 APPROVE</button></td>
                </tr>
                <tr>
                    <td>#02</td>
                    <td>✌️U-T</td>
                    <td>H1 Linear vs U</td>
                    <td><span class="badge badge-merge">MERGE</span></td>
                    <td><button class="btn-action">🇰🇷 APPROVE</button></td>
                </tr>
                <tr>
                    <td>#14</td>
                    <td>✌️U-T</td>
                    <td>Dorfman citation</td>
                    <td><span class="badge badge-flag">FLAG</span></td>
                    <td><button class="btn-action">⚙️ Review (Kwon)</button></td>
                </tr>
                <tr>
                    <td>#15</td>
                    <td>✌️U-T</td>
                    <td>Believer/Analyst</td>
                    <td><span class="badge badge-review">REVIEW</span></td>
                    <td><button class="btn-action">🔧 Build (Na)</button></td>
                </tr>
            </tbody>
        </table>
    </div>
    """
    return html

def generate_html(paragraphs, assets, flow):
    css = """
    <style>
        :root {
            --bg-color: #0b0c15;
            --panel-bg: rgba(20, 30, 40, 0.6);
            --border-color: rgba(255, 255, 255, 0.1);
            --text-color: #e0e0e0;
            --accent-green: #00ff9d;
            --accent-orange: #ffcc00;
            --accent-pink: #ff0099;
            --accent-blue: #00ccff;
        }
        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Courier New', monospace;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }
        .container {
            width: 100%;
            max_width: 1200px;
            display: grid;
            grid-template-columns: 2fr 1fr;
            grid-template-rows: auto auto auto;
            gap: 20px;
        }
        .header {
            grid-column: 1 / -1;
            font-size: 1.5rem;
            font-weight: bold;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 10px;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
        }
        .panel {
            background: var(--panel-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 15px;
        }
        .panel-header {
            font-weight: bold;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
            margin-bottom: 12px;
            color: var(--accent-blue);
        }
        
        /* Production Matrix */
        .matrix-grid { display: flex; flex-direction: column; gap: 5px; }
        .matrix-header, .matrix-row {
            display: grid;
            grid-template-columns: 2fr 0.5fr 0.5fr 0.5fr 0.5fr 0.5fr 2fr;
            gap: 10px;
            align-items: center;
            font-size: 0.9rem;
        }
        .matrix-header { font-weight: bold; color: #888; border-bottom: 1px solid #333; padding-bottom: 5px; }
        .col-sect { text-align: center; }
        .col-verify { text-align: center; }
        .verified-yes { color: var(--accent-green); }
        .verified-no { color: #555; }
        .progress-bar {
            background: #333;
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            flex-grow: 1;
        }
        .progress-fill { background: var(--accent-green); height: 100%; }
        .col-progress { display: flex; align-items: center; gap: 8px; }
        .progress-text { font-size: 0.8rem; color: #aaa; }
        .matrix-footer { margin-top: 10px; text-align: right; font-weight: bold; color: var(--accent-green); }
        
        /* Asset Tracker */
        .asset-section { margin-bottom: 15px; }
        .asset-title { font-weight: bold; margin-bottom: 5px; color: #aaa; }
        .asset-list { list-style: none; padding: 0; margin: 0; }
        .asset-item { display: flex; align-items: center; gap: 8px; margin-bottom: 4px; }
        .status-done { color: var(--text-color); }
        .status-pending { color: #666; }
        
        /* Diamond Flow */
        .flow-visual { display: flex; flex-direction: column; align-items: center; gap: 15px; }
        .flow-nodes { display: flex; align-items: center; gap: 10px; }
        .node {
            border: 1px solid #555;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            width: 40px;
            background: rgba(0,0,0,0.3);
        }
        .node.active { border-color: var(--accent-orange); box-shadow: 0 0 10px rgba(255, 204, 0, 0.2); }
        .node-icon { font-size: 1.2rem; }
        .node-label { font-size: 0.8rem; font-weight: bold; margin-top: 4px; }
        .arrow { color: #555; }
        .flow-status { font-size: 0.9rem; color: var(--accent-orange); font-weight: bold; }
        
        /* Issue Queue */
        .issue-queue { grid-column: 1 / -1; }
        .issue-table { width: 100%; border-collapse: collapse; }
        .issue-table th { text-align: left; color: #888; border-bottom: 1px solid #333; padding: 8px; }
        .issue-table td { padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.05); }
        .badge { padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: bold; }
        .badge-merge { background: rgba(255, 0, 153, 0.2); color: var(--accent-pink); }
        .badge-flag { background: rgba(255, 255, 255, 0.1); color: #fff; }
        .badge-review { background: rgba(0, 255, 157, 0.1); color: var(--accent-green); }
        .btn-action {
            background: #333; border: 1px solid #555; color: #fff;
            padding: 4px 8px; border-radius: 4px; cursor: pointer; font-family: inherit; font-size: 0.8rem;
        }
        .btn-action:hover { background: #444; border-color: #777; }
    </style>
    """
    
    body = f"""
    <div class="container">
        <div class="header">
            <span>⚓ SCALE CONTROL TOWER v1.0</span>
            <span style="font-size: 1rem; color: #888;">[Diamond Squad: G→J→K→M]</span>
        </div>
        
        {generate_production_matrix(paragraphs)}
        {generate_asset_tracker(assets)}
        {generate_diamond_flow(flow)}
        {generate_issue_queue()}
    </div>
    """
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scale Control Tower</title>
        {css}
    </head>
    <body>
        {body}
    </body>
    </html>
    """

def main():
    print("🚀 Generating Scale Dashboard...")
    
    # Load Data
    paragraphs = load_json("paragraphs.json")
    assets = load_json("assets.json")
    flow = load_json("flow_state.json")
    
    # Generate HTML
    html_content = generate_html(paragraphs, assets, flow)
    
    # Save
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"✅ Dashboard saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
