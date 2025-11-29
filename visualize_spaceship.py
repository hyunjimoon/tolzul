#!/usr/bin/env python3
"""
Jeolla Fleet Thesis Board Visualizer
====================================

Generates the "Jeolla Fleet Thesis Board" dashboard.
A 30-second looping 2D animation of a mission-control dashboard.
"""

import csv
from pathlib import Path
import sys
import json
import os
import time
import re

# --- Configuration ---
BASE_DIR = Path("/Users/hyunjimoon/tolzul")
DATA_FILE = BASE_DIR / "spaceship_data.csv"
OUTPUT_FILE = BASE_DIR / "battle_dashboard.html"
PAPER_GEN_DIR = BASE_DIR / "Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation"
PAPER_OUT_DIR = PAPER_GEN_DIR / "output"
ACHIEVEMENTS_FILE = PAPER_GEN_DIR / "journal/fleet_achievements.json"

def get_file_metrics(filepath):
    """Returns detailed metrics for a file."""
    if not filepath.exists():
        return {"size": 0, "words": 0, "figures": 0, "citations": 0, "recency_score": 0, "risk": 2, "age_hours": 999, "paragraphs": 0}
    
    stats = filepath.stat()
    size = stats.st_size
    mtime = stats.st_mtime
    age_seconds = time.time() - mtime
    age_hours = age_seconds / 3600
    
    content = ""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        pass

    words = len(content.split())
    figures = len(re.findall(r'!\[.*?\]\(.*?\)', content))
    citations = len(re.findall(r'\[@.*?\]', content)) # Pandoc style citations
    
    # Count Paragraphs (Key Sentences)
    # Simple heuristic: non-empty lines that are not headers/code/lists
    paragraphs = 0
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('```') and not line.startswith('-') and not line.startswith('!') and len(line) > 50:
            paragraphs += 1

    # Scores
    size_score = min(100, (size / 10000) * 100)
    recency_score = max(0, 100 - (age_seconds / 864))
    if age_seconds < 3600: recency_score = 100
    
    risk = 0
    if age_hours > 48: risk = 2
    elif age_hours > 24: risk = 1
        
    return {
        "size": size,
        "words": words,
        "figures": figures,
        "citations": citations,
        "paragraphs": paragraphs,
        "recency_score": int(recency_score),
        "risk": risk,
        "age_hours": int(age_hours)
    }

def get_latest_achievement(paper_tag):
    """Reads the latest achievement for a given paper tag (P1, P2, P3)."""
    if not ACHIEVEMENTS_FILE.exists():
        return None
    
    try:
        with open(ACHIEVEMENTS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Filter for achievements impacting this paper
        relevant = [a for a in data.get("achievements", []) if paper_tag in a.get("impact_areas", [])]
        if relevant:
            # Sort by date desc
            relevant.sort(key=lambda x: x.get("date", ""), reverse=True)
            return relevant[0]
    except:
        pass
    return None

def generate_dashboard():
    print("🎨 Generating Jeolla Left Navy Dashboard with Quantified Metrics...")

    # --- Data Gathering ---
    # Map Papers to Files (P1, P2, P3)
    # We map to the PRODUCT files (Markdown) for metrics
    papers = {
        "P1": {
            "name": "P1: Vagueness", "icon": "✌️", "state": "green", "desc": "Mature (Ready)", 
            "target_words": 8000, 
            "structure_target": {"chap1_introduction.md": 7, "chap2_theory.md": 9},
            "files": ["chap1_introduction.md", "chap2_theory.md"]
        },
        "P2": {
            "name": "P2: Trap", "icon": "🦾", "state": "yellow", "desc": "Struct OK / Data Low", 
            "target_words": 6000, 
            "structure_target": {"chap2_theory.md": 9, "chap3_empirics.md": 11},
            "files": ["chap2_theory.md", "chap3_empirics.md"]
        },
        "P3": {
            "name": "P3: Newsvendor", "icon": "🤹", "state": "red", "desc": "Redesigning Engine", 
            "target_words": 5000, 
            "structure_target": {"chap3_empirics.md": 11, "chap4_discussion.md": 5},
            "files": ["chap3_empirics.md", "chap4_discussion.md"]
        }
    }
    
    # Calculate Real Metrics
    for pid, pdata in papers.items():
        metrics = {"words": 0, "figures": 0, "citations": 0, "recency_sum": 0, "risk_max": 0, "paragraphs": 0, "target_paragraphs": 0}
        count = 0
        
        # Structure Tracking
        structure_status = [] # List of {name, current, target}
        
        for fname in pdata["files"]:
            fpath = PAPER_OUT_DIR / fname
            m = get_file_metrics(fpath)
            
            metrics["words"] += m["words"]
            metrics["figures"] += m["figures"]
            metrics["citations"] += m["citations"]
            metrics["recency_sum"] += m["recency_score"]
            metrics["risk_max"] = max(metrics["risk_max"], m["risk"])
            
            # Paragraph Structure
            target_para = pdata["structure_target"].get(fname, 0)
            metrics["paragraphs"] += m["paragraphs"]
            metrics["target_paragraphs"] += target_para
            
            structure_status.append({
                "file": fname.replace(".md", ""),
                "current": m["paragraphs"],
                "target": target_para
            })
            
            count += 1
        
        pdata["structure"] = structure_status
        
        # Calculate Score
        # Score = (WordCount / Target) * 50% + Recency * 50%
        word_progress = min(100, (metrics["words"] / pdata["target_words"]) * 100)
        recency_avg = metrics["recency_sum"] / max(1, count)
        
        final_score = int((word_progress * 0.6) + (recency_avg * 0.4)) # Weight progress more than recency for "Maturity"
        
        pdata["score"] = final_score
        pdata["metrics"] = metrics
        
        # Update State
        if final_score >= 80: pdata["state"] = "green"
        elif final_score >= 50: pdata["state"] = "yellow"
        else: pdata["state"] = "red"
        
        # Get Achievement
        ach = get_latest_achievement(pid)
        if ach:
            pdata["achievement"] = f"{ach['title']} ({ach['member_id']})"
        else:
            pdata["achievement"] = "No recent intel"

    # Agents
    agents = [
        {"id": "a1", "name": "Jungwoon", "role": "Generator", "icon": "🐢", "desc": "Speed/Creativity"},
        {"id": "a2", "name": "Kwonjun", "role": "Structurer", "icon": "🐅", "desc": "Logic/Structure"},
        {"id": "a3", "name": "Gimwan", "role": "Verifier", "icon": "🐙", "desc": "Rigor/Critique"}
    ]

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jeolla Left Navy: Mgmt Sci Ops</title>
    <style>
        :root {{
            --bg-color: #050510;
            --neon-blue: #00f3ff;
            --neon-green: #00ff9d;
            --neon-red: #ff3333;
            --neon-amber: #ffcc00;
            --glass-bg: rgba(20, 30, 40, 0.8);
            --border-color: rgba(0, 243, 255, 0.3);
        }}
        
        body {{
            background-color: var(--bg-color);
            color: var(--neon-blue);
            font-family: 'Courier New', monospace;
            margin: 0;
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            background-image: 
                radial-gradient(circle at 50% 50%, rgba(0, 40, 80, 0.3) 0%, transparent 70%),
                linear-gradient(0deg, rgba(0,255,255,0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0,255,255,0.02) 1px, transparent 1px);
            background-size: 100% 100%, 40px 40px, 40px 40px;
        }}

        /* Header */
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 30px;
            border-bottom: 1px solid var(--border-color);
            background: var(--glass-bg);
            z-index: 100;
        }}
        .title {{ font-size: 1.5rem; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; }}
        .subtitle {{ font-size: 0.8rem; color: #888; }}

        /* Main Battlefield */
        .battlefield {{
            flex: 1;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}

        /* Agent Pipeline */
        .pipeline-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 80%;
            margin-bottom: 50px;
            position: relative;
        }}

        .agent-node {{
            width: 120px;
            height: 120px;
            border: 2px solid var(--neon-blue);
            border-radius: 50%;
            background: rgba(0,0,0,0.6);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
            z-index: 10;
            transition: all 0.3s ease;
            cursor: grab;
        }}
        .agent-node:active {{ cursor: grabbing; transform: scale(1.1); }}
        
        .agent-icon {{ font-size: 3rem; margin-bottom: 5px; }}
        .agent-name {{ font-size: 0.9rem; font-weight: bold; color: #fff; }}
        .agent-role {{ font-size: 0.7rem; color: var(--neon-blue); }}
        
        /* Flow Lines */
        .flow-line {{
            flex: 1;
            height: 4px;
            background: #222;
            position: relative;
            margin: 0 20px;
            border-radius: 2px;
        }}
        
        .flow-particle {{
            position: absolute;
            top: 0; left: 0;
            width: 20px; height: 4px;
            background: var(--neon-green);
            box-shadow: 0 0 10px var(--neon-green);
            border-radius: 2px;
            animation: flowRight 2s linear infinite;
        }}
        
        .back-particle {{
            position: absolute;
            top: 0; right: 0;
            width: 20px; height: 4px;
            background: var(--neon-red);
            box-shadow: 0 0 10px var(--neon-red);
            border-radius: 2px;
            animation: flowLeft 2s linear infinite;
            display: none; /* Hidden by default */
        }}

        /* Turtle Ships (Papers) */
        .fleet-container {{
            display: flex;
            gap: 40px;
            z-index: 20;
        }}

        .paper-card {{
            width: 240px;
            background: var(--glass-bg);
            border: 1px solid #444;
            border-radius: 10px;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
        }}
        .paper-card:hover {{ transform: translateY(-5px); box-shadow: 0 5px 15px rgba(0,0,0,0.5); }}
        
        .paper-icon {{ font-size: 3rem; margin-bottom: 10px; }}
        .paper-name {{ font-size: 1rem; font-weight: bold; margin-bottom: 5px; }}
        .paper-desc {{ font-size: 0.7rem; color: #aaa; text-align: center; margin-bottom: 10px; }}
        
        .score-bar {{ width: 100%; height: 6px; background: #333; border-radius: 3px; overflow: hidden; margin-bottom: 10px; }}
        .score-fill {{ height: 100%; transition: width 1s ease; }}

        /* Metrics Grid */
        .metrics-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 5px;
            width: 100%;
            margin-top: 10px;
            border-top: 1px solid #333;
            padding-top: 10px;
        }}
        .metric-item {{ text-align: center; }}
        .metric-val {{ font-size: 0.9rem; font-weight: bold; color: #fff; }}
        .metric-label {{ font-size: 0.6rem; color: #888; text-transform: uppercase; }}

        /* Structure Dots */
        .structure-container {{
            width: 100%;
            margin-top: 10px;
            background: rgba(0,0,0,0.3);
            padding: 5px;
            border-radius: 5px;
        }}
        .structure-row {{
            display: flex;
            align-items: center;
            margin-bottom: 2px;
        }}
        .structure-label {{ font-size: 0.6rem; color: #aaa; width: 40px; }}
        .structure-dots {{ display: flex; gap: 2px; flex: 1; }}
        .dot {{ width: 6px; height: 6px; border-radius: 50%; background: #333; }}
        .dot.filled {{ background: var(--neon-green); box-shadow: 0 0 2px var(--neon-green); }}

        /* Achievement Badge */
        .achievement-badge {{
            position: absolute;
            top: -10px;
            right: -10px;
            background: var(--neon-blue);
            color: #000;
            font-size: 0.6rem;
            padding: 2px 6px;
            border-radius: 10px;
            font-weight: bold;
            box-shadow: 0 0 5px var(--neon-blue);
            max-width: 150px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        /* States */
        .state-green {{ border-color: var(--neon-green); }}
        .state-green .paper-icon {{ filter: drop-shadow(0 0 5px var(--neon-green)); }}
        .state-green .score-fill {{ background: var(--neon-green); }}
        
        .state-yellow {{ border-color: var(--neon-amber); }}
        .state-yellow .paper-icon {{ filter: drop-shadow(0 0 5px var(--neon-amber)); }}
        .state-yellow .score-fill {{ background: var(--neon-amber); }}
        
        .state-red {{ border-color: var(--neon-red); animation: pulseRed 2s infinite; }}
        .state-red .paper-icon {{ filter: drop-shadow(0 0 5px var(--neon-red)); }}
        .state-red .score-fill {{ background: var(--neon-red); }}

        /* Siren Alert */
        .siren-overlay {{
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle, transparent 50%, rgba(255, 0, 0, 0.2) 100%);
            pointer-events: none;
            opacity: 0;
            z-index: 0;
            animation: sirenFlash 1s infinite;
            display: none;
        }}

        /* Connection Line (SVG) */
        #connection-svg {{
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 5;
        }}
        .collab-line {{
            stroke: var(--neon-blue);
            stroke-width: 2;
            stroke-dasharray: 5,5;
            animation: dash 1s linear infinite;
        }}

        @keyframes flowRight {{ 0% {{ left: 0%; opacity: 0; }} 20% {{ opacity: 1; }} 80% {{ opacity: 1; }} 100% {{ left: 100%; opacity: 0; }} }}
        @keyframes flowLeft {{ 0% {{ right: 0%; opacity: 0; }} 20% {{ opacity: 1; }} 80% {{ opacity: 1; }} 100% {{ right: 100%; opacity: 0; }} }}
        @keyframes pulseRed {{ 0% {{ box-shadow: 0 0 5px var(--neon-red); }} 50% {{ box-shadow: 0 0 20px var(--neon-red); }} 100% {{ box-shadow: 0 0 5px var(--neon-red); }} }}
        @keyframes sirenFlash {{ 0% {{ opacity: 0; }} 50% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}
        @keyframes dash {{ to {{ stroke-dashoffset: -10; }} }}
        
        .dimmed {{ opacity: 0.2; filter: grayscale(100%); }}

    </style>
</head>
<body>
    <div class="siren-overlay" id="siren"></div>
    <svg id="connection-svg"></svg>

    <div class="header">
        <div>
            <div class="title">Jeolla Left Navy HQ</div>
            <div class="subtitle">Management Science Operation</div>
        </div>
        <div style="text-align: right;">
            <div class="subtitle">Acceptance Probability</div>
            <div style="font-size: 1.2rem; font-weight: bold; color: var(--neon-green);">
                {sum(p['score'] for p in papers.values()) / 3:.1f}%
            </div>
        </div>
    </div>

    <div class="battlefield">
        
        <!-- Agent Pipeline -->
        <div class="pipeline-container">
            <!-- Jungwoon -->
            <div class="agent-node" id="a1" draggable="true">
                <div class="agent-icon">🐢</div>
                <div class="agent-name">Jungwoon</div>
                <div class="agent-role">Generator</div>
            </div>
            
            <div class="flow-line">
                <div class="flow-particle"></div>
                <div class="back-particle" id="back-1"></div>
            </div>
            
            <!-- Kwonjun -->
            <div class="agent-node" id="a2" draggable="true">
                <div class="agent-icon">🐅</div>
                <div class="agent-name">Kwonjun</div>
                <div class="agent-role">Structurer</div>
            </div>
            
            <div class="flow-line">
                <div class="flow-particle"></div>
                <div class="back-particle" id="back-2"></div>
            </div>
            
            <!-- Gimwan -->
            <div class="agent-node" id="a3" draggable="true">
                <div class="agent-icon">🐙</div>
                <div class="agent-name">Gimwan</div>
                <div class="agent-role">Verifier</div>
            </div>
        </div>

        <!-- Fleet (Papers) -->
        <div class="fleet-container">
            <!-- P1 -->
            <div class="paper-card state-{papers['P1']['state']}" id="p1" onclick="filterView('P1')">
                <div class="achievement-badge" title="{papers['P1']['achievement']}">{papers['P1']['achievement']}</div>
                <div class="paper-icon">{papers['P1']['icon']}</div>
                <div class="paper-name">{papers['P1']['name']}</div>
                <div class="paper-desc">{papers['P1']['desc']}</div>
                <div class="score-bar"><div class="score-fill" style="width: {papers['P1']['score']}%"></div></div>
                <div style="font-size:0.8rem; margin-bottom: 5px;">{papers['P1']['score']}% Maturity</div>
                
                <div class="metrics-grid">
                    <div class="metric-item">
                        <div class="metric-val">{papers['P1']['metrics']['words']}</div>
                        <div class="metric-label">Words</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-val">{papers['P1']['metrics']['figures']}</div>
                        <div class="metric-label">Figs</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-val">{papers['P1']['metrics']['citations']}</div>
                        <div class="metric-label">Refs</div>
                    </div>
                </div>

                <div class="structure-container">
                    {''.join([f'<div class="structure-row"><div class="structure-label">{s["file"][:5]}</div><div class="structure-dots">' + ('<div class="dot filled"></div>' * min(s["current"], s["target"])) + ('<div class="dot"></div>' * max(0, s["target"] - s["current"])) + '</div></div>' for s in papers['P1']['structure']])}
                </div>
            </div>
            
            <!-- P2 -->
            <div class="paper-card state-{papers['P2']['state']}" id="p2" onclick="filterView('P2')">
                <div class="achievement-badge" title="{papers['P2']['achievement']}">{papers['P2']['achievement']}</div>
                <div class="paper-icon">{papers['P2']['icon']}</div>
                <div class="paper-name">{papers['P2']['name']}</div>
                <div class="paper-desc">{papers['P2']['desc']}</div>
                <div class="score-bar"><div class="score-fill" style="width: {papers['P2']['score']}%"></div></div>
                <div style="font-size:0.8rem; margin-bottom: 5px;">{papers['P2']['score']}% Maturity</div>
                
                <div class="metrics-grid">
                    <div class="metric-item">
                        <div class="metric-val">{papers['P2']['metrics']['words']}</div>
                        <div class="metric-label">Words</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-val">{papers['P2']['metrics']['figures']}</div>
                        <div class="metric-label">Figs</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-val">{papers['P2']['metrics']['citations']}</div>
                        <div class="metric-label">Refs</div>
                    </div>
                </div>

                <div class="structure-container">
                    {''.join([f'<div class="structure-row"><div class="structure-label">{s["file"][:5]}</div><div class="structure-dots">' + ('<div class="dot filled"></div>' * min(s["current"], s["target"])) + ('<div class="dot"></div>' * max(0, s["target"] - s["current"])) + '</div></div>' for s in papers['P2']['structure']])}
                </div>
            </div>
            
            <!-- P3 -->
            <div class="paper-card state-{papers['P3']['state']}" id="p3" onclick="filterView('P3')">
                <div class="achievement-badge" title="{papers['P3']['achievement']}">{papers['P3']['achievement']}</div>
                <div class="paper-icon">{papers['P3']['icon']}</div>
                <div class="paper-name">{papers['P3']['name']}</div>
                <div class="paper-desc">{papers['P3']['desc']}</div>
                <div class="score-bar"><div class="score-fill" style="width: {papers['P3']['score']}%"></div></div>
                <div style="font-size:0.8rem; margin-bottom: 5px;">{papers['P3']['score']}% Maturity</div>
                
                <div class="metrics-grid">
                    <div class="metric-item">
                        <div class="metric-val">{papers['P3']['metrics']['words']}</div>
                        <div class="metric-label">Words</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-val">{papers['P3']['metrics']['figures']}</div>
                        <div class="metric-label">Figs</div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-val">{papers['P3']['metrics']['citations']}</div>
                        <div class="metric-label">Refs</div>
                    </div>
                </div>

                <div class="structure-container">
                    {''.join([f'<div class="structure-row"><div class="structure-label">{s["file"][:5]}</div><div class="structure-dots">' + ('<div class="dot filled"></div>' * min(s["current"], s["target"])) + ('<div class="dot"></div>' * max(0, s["target"] - s["current"])) + '</div></div>' for s in papers['P3']['structure']])}
                </div>
            </div>
        </div>

    </div>

    <script>
        // Data Injection
        const papers = {json.dumps(papers)};
        
        // Siren Logic
        const siren = document.getElementById('siren');
        const hasCriticalRisk = Object.values(papers).some(p => p.score < 50); // < 50% triggers siren
        if (hasCriticalRisk) {{
            siren.style.display = 'block';
        }}

        // Back-propagation Logic (Random Simulation)
        setInterval(() => {{
            if (Math.random() > 0.7) {{
                document.getElementById('back-2').style.display = 'block';
                setTimeout(() => document.getElementById('back-2').style.display = 'none', 2000);
            }}
            if (Math.random() > 0.8) {{
                document.getElementById('back-1').style.display = 'block';
                setTimeout(() => document.getElementById('back-1').style.display = 'none', 2000);
            }}
        }}, 3000);

        // Filter View Logic
        let activeFilter = null;
        function filterView(pid) {{
            const allPapers = document.querySelectorAll('.paper-card');
            const allAgents = document.querySelectorAll('.agent-node');
            
            if (activeFilter === pid) {{
                // Reset
                allPapers.forEach(el => el.classList.remove('dimmed'));
                allAgents.forEach(el => el.classList.remove('dimmed'));
                activeFilter = null;
            }} else {{
                // Filter
                activeFilter = pid;
                allPapers.forEach(el => {{
                    if (el.id !== pid.toLowerCase()) el.classList.add('dimmed');
                    else el.classList.remove('dimmed');
                }});
                // Agents stay active for now (they work on everything)
            }}
        }}

        // Drag and Drop Logic (Collaboration)
        let dragged = null;
        const agents = document.querySelectorAll('.agent-node');
        
        agents.forEach(agent => {{
            agent.addEventListener('dragstart', (e) => {{
                dragged = e.target;
                e.dataTransfer.effectAllowed = 'link';
            }});
            
            agent.addEventListener('dragover', (e) => {{
                e.preventDefault(); // Allow drop
            }});
            
            agent.addEventListener('drop', (e) => {{
                e.preventDefault();
                const target = e.target.closest('.agent-node');
                if (target && target !== dragged) {{
                    drawConnection(dragged, target);
                }}
            }});
        }});

        function drawConnection(el1, el2) {{
            const svg = document.getElementById('connection-svg');
            const rect1 = el1.getBoundingClientRect();
            const rect2 = el2.getBoundingClientRect();
            
            const x1 = rect1.left + rect1.width / 2;
            const y1 = rect1.top + rect1.height / 2;
            const x2 = rect2.left + rect2.width / 2;
            const y2 = rect2.top + rect2.height / 2;
            
            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', x1);
            line.setAttribute('y1', y1);
            line.setAttribute('x2', x2);
            line.setAttribute('y2', y2);
            line.classList.add('collab-line');
            
            svg.appendChild(line);
            
            // Remove after 2 seconds
            setTimeout(() => line.remove(), 2000);
        }}

    </script>
</body>
</html>
    """

    with open(OUTPUT_FILE, 'w') as f:
        f.write(html_content)

    print(f"✅ Jeolla Left Navy Dashboard saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_dashboard()
