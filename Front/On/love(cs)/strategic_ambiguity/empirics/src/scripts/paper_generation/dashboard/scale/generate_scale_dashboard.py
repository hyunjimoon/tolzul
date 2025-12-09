#!/usr/bin/env python3
"""
Scale Dashboard Generator v3.0
==============================
Generates the 'Scale Control Tower' dashboard based on dashboard_state.json.
Features:
- 4-Day Sprint Countdown
- Paper Status Cards (U, C, N)
- Bottleneck Tracker
- Rally Point Progress
- Gatekeeper Logs
"""

import json
import datetime
import os
import urllib.parse
from pathlib import Path
import datetime
import base64

# Configuration
CURRENT_DIR = Path(__file__).parent.resolve()
DATA_FILE = CURRENT_DIR / "dashboard_state.json"
OUTPUT_FILE = CURRENT_DIR / "scale_dashboard.html"

def load_data():
    if not DATA_FILE.exists():
        print(f"Error: {DATA_FILE} not found.")
        return {}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_obsidian_url(path_suffix):
    """Generates an Obsidian URL for a given relative path."""
    base_path = "Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output"
    full_path = f"{base_path}/{path_suffix}"
    import urllib.parse
    encoded_path = urllib.parse.quote(full_path)
    return f"obsidian://open?vault=tolzul&file={encoded_path}"

def generate_header(meta):
    start_date = datetime.datetime.strptime(meta["startDate"], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(meta["endDate"], "%Y-%m-%d")
    now = datetime.datetime.now()
    
    # Calculate remaining time (mock logic for static generation, JS handles real-time)
    total_days = (end_date - start_date).days + 1
    current_day = meta["currentDay"]
    
    html = f"""
    <div class="header-section">
        <div class="header-title">
            <div class="battle-name">🏴 {meta['battle']}: {meta['codename']}</div>
            <div class="motto">"{meta['motto']}"</div>
        </div>
        <div class="header-info">
            <div>Period: {meta['startDate']} ~ {meta['endDate']} ({total_days} Days)</div>
            <div class="countdown">Current: Day {current_day} of {total_days}</div>
        </div>
    </div>
    """
    return html

def generate_paper_cards(papers):
    html = '<div class="paper-cards-container">'
    
    for pid, data in papers.items():
        # Color mapping
        color_class = f"paper-{pid.lower()}"
        
        # Bottlenecks
        bottlenecks_html = ""
        for b in data.get("bottlenecks", []):
            icon = "🔴" if b["priority"] == "critical" else "🟡"
            status_icon = "✅" if b["status"] == "done" else "⬜"
            bottlenecks_html += f'<div class="bottleneck-item">{status_icon} {icon} {b["desc"]} <span class="owner">({b["owner"]})</span></div>'
            
        # Key Metric
        metric = data.get("keyMetric", {})
        metric_verified = "✅ Verified" if metric.get("verified") else "⚠️ Pending"
        metric_class = "metric-verified" if metric.get("verified") else "metric-pending"
        
        # Visuals
        visuals_html = ""
        if data.get("figures"):
            visuals_html = '<div class="visual-section"><div class="section-title">Visual Intel</div><div class="visual-grid">'
            for fig in data["figures"]:
                # Relative path logic: ../../output/{fig}
                rel_path = f"../../output/{fig}"
                visuals_html += f'<img src="{rel_path}" class="thumb-img" title="{fig}">'
            visuals_html += '</div></div>'
        
        html += f"""
        <div class="paper-card {color_class}">
            <div class="card-header">
                <div class="card-icon">{pid}</div>
                <div class="card-title">{data['name']}</div>
                <div class="card-target">{data['target']}</div>
            </div>
            <div class="card-body">
                <div class="progress-section">
                    <div class="progress-label">Progress: {data['progress']}%</div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {data['progress']}%"></div>
                    </div>
                </div>
                {visuals_html}
                <div class="bottleneck-section">
                    <div class="section-title">Bottlenecks</div>
                    {bottlenecks_html}
                </div>
                <div class="metric-section">
                    <div class="section-title">Key Metric</div>
                    <div class="metric-value">{metric.get('name')}: {metric.get('current')}</div>
                    <div class="metric-status {metric_class}">{metric_verified}</div>
                </div>
            </div>
        </div>
        """
    html += '</div>'
    return html

def generate_bottleneck_tracker(papers):
    html = """
    <div class="panel bottleneck-tracker">
        <div class="panel-header">🚦 BOTTLENECK RESOLUTION TRACKER</div>
        <table class="tracker-table">
            <thead>
                <tr>
                    <th>Paper</th>
                    <th>Bottleneck</th>
                    <th>Priority</th>
                    <th>Status</th>
                    <th>Owner</th>
                    <th>Due</th>
                </tr>
            </thead>
            <tbody>
    """
    
    all_bottlenecks = []
    for pid, pdata in papers.items():
        for b in pdata.get("bottlenecks", []):
            b["paper"] = pid
            all_bottlenecks.append(b)
            
    # Sort by priority (critical first)
    priority_map = {"critical": 0, "important": 1, "normal": 2}
    all_bottlenecks.sort(key=lambda x: priority_map.get(x["priority"], 2))
    
    for b in all_bottlenecks:
        p_icon = "🔴" if b["priority"] == "critical" else "🟡"
        status_icon = "✅" if b["status"] == "done" else "⬜"
        if b["status"] == "in_progress": status_icon = "🔄"
        
        paper_icon = "✌️U" if b["paper"] == "U" else ("🦾C" if b["paper"] == "C" else "🤹N")
        
        html += f"""
        <tr>
            <td style="text-align:center">{paper_icon}</td>
            <td>{b['desc']}</td>
            <td style="text-align:center">{p_icon}</td>
            <td style="text-align:center">{status_icon} {b['status'].upper()}</td>
            <td style="text-align:center">{b['owner']}</td>
            <td style="text-align:center">{b['due']}</td>
        </tr>
        """
        
    html += """
            </tbody>
        </table>
    </div>
    """
    return html

def generate_rally_points(rally_points):
    html = """
    <div class="panel rally-points">
        <div class="panel-header">🚩 RALLY POINT PROGRESS</div>
        <div class="rp-container">
    """
    
    for rid, rdata in rally_points.items():
        status_class = rdata["status"]
        html += f"""
        <div class="rp-card {status_class}">
            <div class="rp-header">
                <span class="rp-id">{rid}</span>
                <span class="rp-name">{rdata['name']}</span>
            </div>
            <div class="rp-progress">
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {rdata['progress']}%"></div>
                </div>
                <div class="rp-pct">{rdata['progress']}%</div>
            </div>
            <div class="rp-gate">Gate: {rdata['gate']}</div>
        </div>
        """
        
    html += """
        </div>
    </div>
    """
    return html

def generate_gatekeeper_log(decisions):
    html = """
    <div class="panel gatekeeper-log">
        <div class="panel-header">🔴 K (GATEKEEPER) LOG</div>
        <div class="log-list">
    """
    
    for d in decisions:
        timestamp = d["timestamp"].replace("T", " ")
        decision_icon = "🇰🇷 승인" if d["decision"] == "approved" else "🚨 반려"
        decision_class = "approved" if d["decision"] == "approved" else "rejected"
        
        html += f"""
        <div class="log-item {decision_class}">
            <span class="log-time">[{timestamp}]</span>
            <span class="log-target">{d['paper']} {d['section']}</span>:
            <span class="log-decision">{decision_icon}</span> — 
            <span class="log-note">{d['note']}</span>
        </div>
        """
        
    html += """
        </div>
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
            </div>
            <div class="deck-card" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/%F0%9F%93%A2BULLETIN.md'">
                <div class="card-icon">📢</div>
                <div class="card-title">BULLETIN</div>
            </div>
            <div class="deck-card" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/%F0%9F%97%84%EF%B8%8FREGISTRY.md'">
                <div class="card-icon">🗄️</div>
                <div class="card-title">REGISTRY</div>
            </div>
            <div class="deck-card" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/toc%28iucnd%29.md'">
                <div class="card-icon">🗺️</div>
                <div class="card-title">MASTER TOC</div>
            </div>
        </div>
    </div>
    """
    return html

def generate_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@400;700&display=swap');
        
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --card-border: #334155;
            --accent-gold: #fbbf24;
            --success-green: #34d399;
            --warning-orange: #fb923c;
            --critical-red: #f87171;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            
            --paper-u: #facc15;
            --paper-c: #94a3b8;
            --paper-n: #60a5fa;
        }
        
        * { box-sizing: border-box; }
        
        body {
            background-color: var(--bg-color);
            color: var(--text-primary);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            margin: 0;
            padding: 40px;
            line-height: 1.5;
        }
        
        .container {
            max-width: 1600px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            gap: 24px;
        }
        
        /* Typography */
        h1, h2, h3 { margin: 0; font-weight: 800; letter-spacing: -0.02em; }
        .mono { font-family: 'JetBrains Mono', monospace; }
        
        /* Header (Span 12) */
        .header-section {
            grid-column: span 12;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-bottom: 20px;
            border-bottom: 1px solid var(--card-border);
            padding-bottom: 20px;
        }
        .battle-title { font-size: 2rem; color: var(--text-primary); }
        .battle-meta { font-size: 1rem; color: var(--text-secondary); display: flex; gap: 20px; align-items: center; }
        .countdown-badge { 
            background: rgba(52, 211, 153, 0.1); 
            color: var(--success-green); 
            padding: 4px 12px; 
            border-radius: 99px; 
            font-weight: 600;
            border: 1px solid rgba(52, 211, 153, 0.2);
        }
        
        /* Command Deck (Span 12 -> Toolbar) */
        .command-deck {
            grid-column: span 12;
            display: flex;
            gap: 12px;
            margin-bottom: 10px;
        }
        .cmd-btn {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            color: var(--text-secondary);
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .cmd-btn:hover {
            background: #334155;
            color: var(--text-primary);
            border-color: var(--text-secondary);
            transform: translateY(-1px);
        }
        
        /* Paper Cards (Span 4 each) */
        .paper-card {
            grid-column: span 4;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            position: relative;
            overflow: hidden;
        }
        .paper-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 4px;
        }
        .paper-u::before { background: var(--paper-u); }
        .paper-c::before { background: var(--paper-c); }
        .paper-n::before { background: var(--paper-n); }
        
        .card-header { display: flex; justify-content: space-between; align-items: flex-start; }
        .paper-name { font-size: 1.25rem; font-weight: 700; }
        .paper-target { 
            font-size: 0.75rem; 
            text-transform: uppercase; 
            letter-spacing: 0.05em; 
            color: var(--text-secondary); 
            background: rgba(0,0,0,0.2);
            padding: 2px 8px;
            border-radius: 4px;
        }
        
        /* Progress Hero */
        .progress-hero { display: flex; flex-direction: column; gap: 8px; }
        .progress-val { font-size: 3rem; font-weight: 800; line-height: 1; letter-spacing: -0.05em; }
        .progress-bar-bg { background: #334155; height: 6px; border-radius: 99px; overflow: hidden; }
        .progress-fill { height: 100%; border-radius: 99px; }
        
        /* Visuals */
        .visual-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; height: 100px; }
        .thumb-img { 
            width: 100%; 
            height: 100%; 
            object-fit: cover; 
            border-radius: 6px; 
            border: 1px solid var(--card-border);
            opacity: 0.8;
            transition: all 0.2s;
            cursor: zoom-in;
        }
        .thumb-img:hover { opacity: 1; border-color: var(--text-primary); transform: scale(1.05); z-index: 10; }
        
        /* Metrics & Bottlenecks Compact */
        .meta-grid { display: grid; grid-template-columns: 1fr; gap: 12px; border-top: 1px solid var(--card-border); padding-top: 16px; }
        .metric-row { display: flex; justify-content: space-between; align-items: center; }
        .metric-label { font-size: 0.85rem; color: var(--text-secondary); }
        .metric-val { font-weight: 700; color: var(--success-green); }
        
        .bottleneck-list { display: flex; flex-direction: column; gap: 6px; }
        .bottleneck-item { 
            font-size: 0.85rem; 
            display: flex; 
            align-items: center; 
            gap: 8px; 
            color: var(--text-secondary);
        }
        .priority-dot { width: 8px; height: 8px; border-radius: 50%; }
        .dot-critical { background: var(--critical-red); box-shadow: 0 0 8px rgba(248, 113, 113, 0.4); }
        .dot-important { background: var(--warning-orange); }
        
        /* Bottom Section (Span 12) */
        .dashboard-footer {
            grid-column: span 12;
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 24px;
        }
        
        /* Minimal Table */
        .tracker-panel { 
            background: var(--card-bg); 
            border: 1px solid var(--card-border); 
            border-radius: 12px; 
            padding: 24px;
        }
        .panel-title { 
            font-size: 0.9rem; 
            text-transform: uppercase; 
            letter-spacing: 0.05em; 
            color: var(--text-secondary); 
            margin-bottom: 16px; 
            font-weight: 700;
        }
        
        .min-table { width: 100%; border-collapse: collapse; }
        .min-table th { text-align: left; color: var(--text-secondary); font-size: 0.75rem; padding-bottom: 12px; border-bottom: 1px solid var(--card-border); }
        .min-table td { padding: 12px 0; border-bottom: 1px solid rgba(51, 65, 85, 0.5); font-size: 0.9rem; }
        .min-table tr:last-child td { border-bottom: none; }
        
        .status-badge { 
            font-size: 0.75rem; 
            padding: 2px 8px; 
            border-radius: 4px; 
            background: rgba(255,255,255,0.05); 
            color: var(--text-secondary);
        }
        
        /* Rally Points Minimal */
        .rally-list { display: flex; flex-direction: column; gap: 12px; }
        .rally-item { display: flex; align-items: center; gap: 12px; }
        .rally-name { width: 100px; font-size: 0.85rem; color: var(--text-secondary); text-align: right; }
        .rally-bar-bg { flex-grow: 1; height: 4px; background: #334155; border-radius: 99px; }
        .rally-fill { height: 100%; background: var(--accent-gold); border-radius: 99px; }
        
        /* Copy Button */
        .copy-btn {
            background: rgba(255,255,255,0.1);
            border: 1px solid var(--card-border);
            color: var(--text-primary);
            padding: 4px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.75rem;
            transition: all 0.2s;
        }
        .copy-btn:hover { background: var(--accent-gold); color: #000; }
        .copy-btn.copied { background: var(--success-green); color: #000; border-color: var(--success-green); }
        
        .copy-btn-mini {
            background: none;
            border: none;
            cursor: pointer;
            font-size: 1rem;
            opacity: 0.5;
            transition: opacity 0.2s;
        }
        .copy-btn-mini:hover { opacity: 1; }
        
        /* Source Badge */
        .thumb-container { position: relative; width: 100%; height: 100%; }
        .source-badge {
            position: absolute;
            bottom: 4px;
            right: 4px;
            background: rgba(0,0,0,0.7);
            color: #fff;
            font-size: 0.6rem;
            padding: 2px 4px;
            border-radius: 3px;
            pointer-events: none;
            font-family: 'JetBrains Mono', monospace;
        }
    </style>
    """

def generate_html(data):
    css = generate_css()
    meta = data["meta"]
    
    # Header
    start_date = datetime.datetime.strptime(meta["startDate"], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(meta["endDate"], "%Y-%m-%d")
    total_days = (end_date - start_date).days + 1
    
    header = f"""
    <div class="header-section">
        <div>
            <div class="battle-title">{meta['battle']}</div>
            <div class="battle-meta">{meta['codename']} <span style="opacity:0.3">|</span> {meta['motto']}</div>
        </div>
        <div class="countdown-badge mono">
            DAY {meta['currentDay']} / {total_days}
        </div>
    </div>
    """
    
    # Command Deck
    command_deck = """
    <div class="command-deck">
        <button class="cmd-btn" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_%F0%9F%A9%B8I/squad_prompts.md'">🎭 Prompts</button>
        <button class="cmd-btn" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/%F0%9F%93%A2BULLETIN.md'">📢 Bulletin</button>
        <button class="cmd-btn" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/%F0%9F%97%84%EF%B8%8FREGISTRY.md'">🗄️ Registry</button>
        <button class="cmd-btn" onclick="window.location.href='obsidian://open?vault=tolzul&file=Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/output/toc%28iucnd%29.md'">🗺️ Master TOC</button>
    </div>
    """
    
    # Cards
    cards_html = ""
    for pid, pdata in data["papers"].items():
        color_var = f"var(--paper-{pid.lower()})"
        
        # Visuals
        visuals = ""
        if pdata.get("figures"):
            visuals = '<div class="visual-grid">'
            for fig_data in pdata["figures"]:
                # Handle both string (legacy) and object (new) formats
                if isinstance(fig_data, str):
                    path = fig_data
                    source = "Unknown Source"
                    func = ""
                else:
                    path = fig_data["path"]
                    source = fig_data.get("source", "Unknown Source")
                    func = fig_data.get("function", "")
                
                # URL Encode path components to handle emojis
                # Split by / to encode each segment separately, preserving the slashes
                encoded_path = "/".join([urllib.parse.quote(part) for part in path.split("/")])
                
                tooltip = f"Source: {source}"
                if func:
                    tooltip += f" :: {func}()"
                    
                visuals += f'''
                <div class="thumb-container" title="{tooltip}">
                    <img src="../../output/{encoded_path}" class="thumb-img">
                    <div class="source-badge">src</div>
                </div>
                '''
            visuals += '</div>'
            
        # Bottlenecks (Top 3 only)
        bottlenecks = ""
        for b in pdata.get("bottlenecks", [])[:3]:
            dot_class = "dot-critical" if b["priority"] == "critical" else "dot-important"
            status_style = "text-decoration: line-through; opacity: 0.5" if b["status"] == "done" else ""
            
            # Prompt Button
            prompt_btn = ""
            if b.get("prompt"):
                prompt_safe = b["prompt"].replace("'", "&apos;").replace('"', "&quot;")
                prompt_btn = f'''
                <button class="copy-btn-mini" onclick="copyPrompt(this, '{prompt_safe}')" title="Copy Delegation Prompt">
                    📋
                </button>
                '''
                
            bottlenecks += f"""
            <div class="bottleneck-item" style="{status_style}">
                <div class="priority-dot {dot_class}"></div>
                <span style="flex-grow:1">{b['desc']}</span>
                {prompt_btn}
            </div>
            """
            
        cards_html += f"""
        <div class="paper-card paper-{pid.lower()}">
            <div class="card-header">
                <div>
                    <div class="paper-name">{pdata['name']}</div>
                    <div class="paper-target mono">{pdata['target']}</div>
                </div>
                <div class="mono" style="font-size: 2rem; opacity: 0.2; font-weight: 800">{pid}</div>
            </div>
            
            <div class="progress-hero">
                <div class="progress-val mono" style="color: {color_var}">{pdata['progress']}%</div>
                <div class="progress-bar-bg">
                    <div class="progress-fill" style="width: {pdata['progress']}%; background: {color_var}"></div>
                </div>
            </div>
            
            {visuals}
            
            <div class="meta-grid">
                <div class="metric-row">
                    <span class="metric-label mono">KEY METRIC</span>
                    <span class="metric-val mono">{pdata['keyMetric']['current']}</span>
                </div>
                <div class="bottleneck-list">
                    {bottlenecks}
                </div>
            </div>
        </div>
        """
        
    # Tracker (Minimal)
    tracker_rows = ""
    all_bottlenecks = []
    for pid, pdata in data["papers"].items():
        for b in pdata.get("bottlenecks", []):
            b["paper"] = pid
            all_bottlenecks.append(b)
    
    # Sort: Critical Pending > Important Pending > Done
    priority_map = {"critical": 0, "important": 1, "normal": 2}
    status_map = {"pending": 0, "in_progress": 1, "done": 2}
    all_bottlenecks.sort(key=lambda x: (status_map.get(x["status"], 2), priority_map.get(x["priority"], 2)))
    
    for b in all_bottlenecks[:5]: # Top 5 only
        p_color = f"var(--paper-{b['paper'].lower()})"
        
        prompt_btn = ""
        if b.get("prompt"):
            prompt_safe = b["prompt"].replace("'", "&apos;").replace('"', "&quot;")
            prompt_btn = f'''
            <button class="copy-btn" onclick="copyPrompt(this, '{prompt_safe}')">
                📋 Copy Prompt
            </button>
            '''
            
        tracker_rows += f"""
        <tr>
            <td style="color: {p_color}; font-weight: 700">{b['paper']}</td>
            <td>{b['desc']}</td>
            <td><span class="status-badge mono">{b['owner']}</span></td>
            <td class="mono" style="color: var(--text-secondary)">{b['due']}</td>
            <td>{prompt_btn}</td>
        </tr>
        """

    # Rally Points
    rally_html = ""
    for rid, rdata in data["rallyPoints"].items():
        emoji = rdata.get("emoji", "")
        name = rdata.get("name", rid)
        rally_html += f"""
        <div class="rally-item">
            <div class="rally-name mono" style="width: 120px; text-align: left">
                <span style="font-size: 1.2rem; margin-right: 8px">{emoji}</span> {name}
            </div>
            <div class="rally-bar-bg">
                <div class="rally-fill" style="width: {rdata['progress']}%"></div>
            </div>
            <div class="mono" style="font-size: 0.75rem; color: var(--accent-gold)">{rdata['progress']}%</div>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Scale Control Tower</title>
        {css}
        <script>
            setTimeout(function() {{ location.reload(); }}, 300000);
            
            // Fix for html-preview.github.io: Set base URL to raw github content
            if (window.location.hostname.includes('html-preview')) {{
                var base = document.createElement('base');
                // Point to the raw file location of this HTML file
                base.href = 'https://raw.githubusercontent.com/hyunjimoon/tolzul/master/Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/dashboard/scale/';
                document.head.appendChild(base);
                console.log('Adjusted base URL for html-preview');
            }}
            
            function copyPrompt(btn, text) {{
                navigator.clipboard.writeText(text).then(() => {{
                    const original = btn.innerHTML;
                    btn.innerHTML = '✅ Copied!';
                    btn.classList.add('copied');
                    setTimeout(() => {{
                        btn.innerHTML = original;
                        btn.classList.remove('copied');
                    }}, 2000);
                }});
            }}
        </script>
    </head>
    <body>
        <div class="container">
            {header}
            {command_deck}
            {cards_html}
            
            <div class="dashboard-footer">
                <div class="tracker-panel">
                    <div class="panel-title">Active Bottlenecks</div>
                    <table class="min-table">
                        <thead><tr><th>PAPER</th><th>ISSUE</th><th>OWNER</th><th>DUE</th><th>ACTION</th></tr></thead>
                        <tbody>{tracker_rows}</tbody>
                    </table>
                </div>
                <div class="tracker-panel">
                    <div class="panel-title">Rally Points</div>
                    <div class="rally-list">
                        {rally_html}
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

def generate_markdown_dashboard(data, html_content=None):
    """Generate a Markdown version of the dashboard for Obsidian Publish."""
    
    # Hosted Approach: GitHub Pages Iframe
    # We point the iframe to the GitHub Pages URL where the HTML will be hosted.
    # URL Structure: https://<user>.github.io/<repo>/<path/to/file>
    # Repo: tolzul (Public)
    # Path: Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/dashboard/scale/scale_dashboard.html
    
    # URL Encode the path to handle parentheses in 'love(cs)'
    # love(cs) -> love%28cs%29
    gh_pages_url = "https://hyunjimoon.github.io/tolzul/Front/On/love%28cs%29/strategic_ambiguity/empirics/src/scripts/paper_generation/dashboard/scale/scale_dashboard.html"
    
    md = f"# 🚀 Scale Command Center (v3.0)\n\n"
    md += f"> **Battle**: {data['meta']['battle']} ({data['meta']['codename']})\n"
    md += f"> **Day**: {data['meta']['currentDay']} | **Motto**: {data['meta']['motto']}\n\n"
    
    md += "## 🖥️ Live Dashboard\n\n"
    md += "*(Loading live command center from HQ...)*\n\n"
    # Wrap in div to ensure block rendering and avoid Markdown parser issues
    md += f'<div><iframe src="{gh_pages_url}" width="100%" height="1000" frameborder="0"></iframe></div>\n\n'
    md += f"🔗 [**Open Full Screen**]({gh_pages_url})\n\n"
    
    md += "> [!TIP] Troubleshooting\n"
    md += "> If the dashboard shows a 404 error:\n"
    md += "> 1. **Wait**: GitHub Pages takes 1-5 minutes to deploy after you push.\n"
    md += "> 2. **Check Settings**: Ensure GitHub Pages is enabled in the `tolzul` repo settings (Source: Deploy from branch).\n"
    md += f"> 3. **Test Link**: Click [here]({gh_pages_url}) to verify the URL works in your browser.\n\n"
    
    md += "---\n\n"
    
    # 1. Paper Progress
    md += "## 📊 Paper Status\n\n"
    md += "| Paper | Target | Progress | Key Metric | Status |\n"
    md += "|:---|:---|:---|:---|:---|\n"
    
    for pid, pdata in data["papers"].items():
        status_icon = "🟢" if pdata['progress'] >= 80 else "🟡" if pdata['progress'] >= 50 else "🔴"
        md += f"| **{pdata['name']}** | {pdata['target']} | {status_icon} {pdata['progress']}% | {pdata['keyMetric']['current']} | {pdata['keyMetric']['target']} |\n"
    
    md += "\n---\n\n"
    
    # 2. Rally Points (IDTS)
    md += "## 🚩 Rally Points (IDTS)\n\n"
    md += "| Phase | Status | Gate |\n"
    md += "|:---|:---|:---|\n"
    for rid, rdata in data["rallyPoints"].items():
        emoji = rdata.get("emoji", "")
        name = rdata.get("name", rid)
        status = "✅ Done" if rdata['status'] == 'done' else "🔄 In Progress" if rdata['status'] == 'in_progress' else "⏳ Pending"
        md += f"| {emoji} **{name}** | {status} | {rdata['gate']} |\n"
        
    md += "\n---\n\n"
    
    # 3. Active Bottlenecks
    md += "## 🚨 Active Bottlenecks\n\n"
    md += "| Paper | Issue | Owner | Due | Prompt |\n"
    md += "|:---|:---|:---|:---|:---|\n"
    
    all_bottlenecks = []
    for pid, pdata in data["papers"].items():
        for b in pdata.get("bottlenecks", []):
            b["paper"] = pid
            all_bottlenecks.append(b)
            
    # Sort
    priority_map = {"critical": 0, "important": 1, "normal": 2}
    status_map = {"pending": 0, "in_progress": 1, "done": 2}
    all_bottlenecks.sort(key=lambda x: (status_map.get(x["status"], 2), priority_map.get(x["priority"], 2)))
    
    for b in all_bottlenecks[:10]:
        if b['status'] == 'done': continue
        prompt_snippet = (b.get('prompt', '')[:50] + '...') if b.get('prompt') else '-'
        md += f"| **{b['paper']}** | {b['desc']} | {b['owner']} | {b['due']} | `{prompt_snippet}` |\n"
        
    return md

def main():
    print("🚀 Generating Scale Dashboard v3.0...")
    
    # Load state
    data = load_data()
    
    # Generate HTML
    html_content = generate_html(data)
    output_path = CURRENT_DIR / "scale_dashboard.html"
    with open(output_path, "w") as f:
        f.write(html_content)
    print(f"✅ HTML Dashboard saved to {output_path}")
    
    # Generate Markdown (New)
    md_content = generate_markdown_dashboard(data, html_content)
    md_output_path = CURRENT_DIR / "scale_dashboard.md"
    with open(md_output_path, "w") as f:
        f.write(md_content)
    print(f"✅ Markdown Dashboard saved to {md_output_path}")

if __name__ == "__main__":
    main()
