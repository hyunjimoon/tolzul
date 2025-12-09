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
                <div class="col-fig">FIG</div>
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
        fig_paths = []
        
        if group["id"] == "intro":
            paths["I"] = "_🩸I/_🩸I.md"
            paths["D"] = "_🐣D/🐣D.md" 
        elif group["id"] == "u":
            paths["I"] = "✌️U/📝product/section1(u).md"
            paths["T"] = "✌️U/📝product/section2(u).md"
            paths["E"] = "✌️U/📝product/section3(u).md"
            paths["D"] = "✌️U/📝product/section4(u).md"
            fig_paths = ["spec_curve_analysis.png", "_🩸I/midV_trap_analysis.png"]
        elif group["id"] == "c":
            paths["I"] = "🦾C/📝product/section1(c).md"
            paths["T"] = "🦾C/📝product/section2(c).md"
            paths["E"] = "🦾C/📝product/section3(c).md"
            paths["D"] = "🦾C/📝product/section4(c).md"
            fig_paths = ["🦾C/⚙️process/figures/fig1_mechanism_3panel.png", "🦾C/⚙️process/figures/fig2_cost_by_decile.png"]
        elif group["id"] == "n":
            paths["I"] = "🤹N/📝product/section1(n).md"
            paths["T"] = "🤹N/📝product/section2(n).md"
            paths["E"] = "🤹N/📝product/section3(n).md"
            paths["D"] = "🤹N/📝product/section4(n).md"
            fig_paths = ["🤹N/⚙️process/figures/mixed audience/fig_simple_murky_v2.png", "🤹N/⚙️process/figures/P3_cr_kstar_curve.png"]
        elif group["id"] == "disc":
             paths["D"] = "_🐣D/🐣D.md"
             paths["I"] = "_🐣D/🐣D.md" 
        
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
        
        # Figure Thumbnail HTML (Dual)
        fig_html = '<div class="col-fig"></div>'
        if fig_paths:
            imgs = ""
            for fp in fig_paths:
                rel_path = f"../../output/{fp}"
                imgs += f'<img src="{rel_path}" class="thumb-img" title="{fp}">'
            fig_html = f'<div class="col-fig">{imgs}</div>'

        # Determine color class
        color_class = ""
        if group["id"] == "intro": color_class = "group-intro"
        elif group["id"] == "u": color_class = "group-u"
        elif group["id"] == "c": color_class = "group-c"
        elif group["id"] == "n": color_class = "group-n"
        elif group["id"] == "disc": color_class = "group-disc"

        html += f"""
            <div class="matrix-row">
                <div class="col-group {color_class}"><span class="group-icon">{group['icon']}</span> {group['name']}</div>
                {fig_html}
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
        .thumb-img { height: 30px; width: auto; border-radius: 4px; border: 1px solid #555; transition: transform 0.2s; }
        .thumb-img:hover { transform: scale(5); z-index: 100; position: relative; border-color: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.8); }
        .col-fig { width: 40px; text-align: center; }
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

def generate_command_deck():
    html = """
    <div class="panel command-deck">
        <div class="panel-header">📡 COMMAND DECK (HQ)</div>
        <div class="deck-grid">
            <div class="deck-card" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_%F0%9F%A9%B8I/squad_prompts.md'">
                <div class="card-icon">🎭</div>
                <div class="card-title">SQUAD PROMPTS</div>
                <div class="card-desc">Role Personas</div>
            </div>
            <div class="deck-card" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/%F0%9F%93%A2BULLETIN.md'">
                <div class="card-icon">📢</div>
                <div class="card-title">BULLETIN</div>
                <div class="card-desc">Single Truth</div>
            </div>
            <div class="deck-card" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/%F0%9F%97%84%EF%B8%8FREGISTRY.md'">
                <div class="card-icon">🗄️</div>
                <div class="card-title">REGISTRY</div>
                <div class="card-desc">Asset Modules</div>
            </div>
            <div class="deck-card" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/toc%28iucnd%29.md'">
                <div class="card-icon">🗺️</div>
                <div class="card-title">MASTER TOC</div>
                <div class="card-desc">Full Blueprint</div>
            </div>
        </div>
    </div>
    <style>
        .command-deck { margin-bottom: 20px; grid-column: 1 / -1; }
        .deck-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; }
        .deck-card { 
            background: rgba(255, 255, 255, 0.05); 
            border: 1px solid #333; 
            border-radius: 6px; 
            padding: 15px; 
            text-align: center; 
            cursor: pointer; 
            transition: all 0.2s;
        }
        .deck-card:hover { background: rgba(255, 255, 255, 0.1); border-color: var(--squad-green); transform: translateY(-2px); }
        .card-icon { font-size: 1.5rem; margin-bottom: 5px; }
        .card-title { font-weight: bold; color: var(--squad-green); font-size: 0.9rem; }
        .card-desc { font-size: 0.7rem; color: #888; margin-top: 3px; }
    </style>
    """
    return html

def generate_html(paragraphs, assets, flow):
    # ... (CSS remains mostly the same, just adding the call)
    css = """
    <style>
        :root {
            --bg-color: #0b0c15;
            --panel-bg: rgba(20, 30, 40, 0.6);
            --border-color: rgba(255, 255, 255, 0.1);
            --text-color: #e0e0e0;
            
            /* Squad Colors */
            --squad-green: #00ff9d; /* J-Squad */
            --squad-orange: #f97316; /* G-Squad */
            --squad-pink: #ff0099; /* K-Squad */
            
            /* Paper Colors */
            --paper-red: #ff4444;    /* Intro */
            --paper-yellow: #ffcc00; /* U-Shape */
            --paper-gray: #888888;   /* Commitment */
            --paper-blue: #3b82f6;   /* Newsvendor */
            --paper-purple: #a855f7; /* Discussion */
            
            /* Legacy Accents (mapped to new scheme where possible) */
            --accent-green: var(--squad-green);
            --accent-orange: var(--squad-orange);
            --accent-pink: var(--squad-pink);
            --accent-blue: var(--paper-blue);
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
            color: var(--paper-blue);
        }
        
        /* Production Matrix */
        .matrix-grid { display: flex; flex-direction: column; gap: 5px; }
        .matrix-header, .matrix-row {
            display: grid;
            grid-template-columns: 2fr 1.2fr 0.5fr 0.5fr 0.5fr 0.5fr 0.5fr 2fr;
            gap: 10px;
            align-items: center;
            font-size: 0.9rem;
        }
        .matrix-header { font-weight: bold; color: #888; border-bottom: 1px solid #333; padding-bottom: 5px; }
        .col-sect { text-align: center; }
        .col-verify { text-align: center; }
        .verified-yes { color: var(--squad-green); }
        .verified-no { color: #555; }
        .progress-bar {
            background: #333;
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            flex-grow: 1;
        }
        .progress-fill { background: var(--squad-green); height: 100%; }
        .col-progress { display: flex; align-items: center; gap: 8px; }
        .progress-text { font-size: 0.8rem; color: #aaa; }
        .matrix-footer { margin-top: 10px; text-align: right; font-weight: bold; color: var(--squad-green); }
        
        /* Group Colors */
        .group-intro { color: var(--paper-red); }
        .group-u { color: var(--paper-yellow); }
        .group-c { color: var(--paper-gray); }
        .group-n { color: var(--paper-blue); }
        .group-disc { color: var(--paper-purple); }
        
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
        .node-m { border-color: #fff; color: #fff; }
        .node-g { border-color: var(--squad-orange); color: var(--squad-orange); }
        .node-j { border-color: var(--squad-green); color: var(--squad-green); }
        .node-k { border-color: var(--squad-pink); color: var(--squad-pink); }
        
        .node.active { box-shadow: 0 0 10px rgba(255, 255, 255, 0.2); background: rgba(255,255,255,0.1); }
        
        .node-icon { font-size: 1.2rem; }
        .node-label { font-size: 0.8rem; font-weight: bold; margin-top: 4px; }
        .arrow { color: #555; }
        .flow-status { font-size: 0.9rem; color: var(--squad-orange); font-weight: bold; }
        
        /* Issue Queue */
        .issue-queue { grid-column: 1 / -1; }
        .issue-table { width: 100%; border-collapse: collapse; }
        .issue-table th { text-align: left; color: #888; border-bottom: 1px solid #333; padding: 8px; }
        .issue-table td { padding: 8px; border-bottom: 1px solid rgba(255,255,255,0.05); }
        .badge { padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: bold; }
        .badge-merge { background: rgba(255, 0, 153, 0.2); color: var(--squad-pink); }
        .badge-flag { background: rgba(255, 255, 255, 0.1); color: #fff; }
        .badge-review { background: rgba(0, 255, 157, 0.1); color: var(--squad-green); }
        .btn-action {
            background: #333; border: 1px solid #555; color: #fff;
            padding: 4px 8px; border-radius: 4px; cursor: pointer; font-family: inherit; font-size: 0.8rem;
        }
        .btn-action:hover { background: #444; border-color: #777; }
        
        /* Thumbnails */
        .col-fig { display: flex; gap: 5px; justify-content: center; }
        .thumb-img { height: 30px; width: auto; border-radius: 4px; border: 1px solid #555; transition: transform 0.2s; cursor: zoom-in; }
        .thumb-img:hover { transform: scale(5); z-index: 100; position: relative; border-color: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.8); }
    </style>
    """
    
    body = f"""
    <div class="container">
        <div class="header">
            <span>⚓ SCALE CONTROL TOWER v2.1 (COMMAND DECK)</span>
            <span style="font-size: 1rem; color: #888;">[Diamond Squad: G→J→K→M]</span>
        </div>
        
        {generate_command_deck()}
        
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
