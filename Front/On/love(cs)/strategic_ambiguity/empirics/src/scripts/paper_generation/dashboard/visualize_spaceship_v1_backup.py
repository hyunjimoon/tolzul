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
# --- Configuration ---
# Updated for new location in paper_generation
CURRENT_DIR = Path(__file__).parent.resolve()
PARENT_DIR = CURRENT_DIR.parent
BASE_DIR = Path("/Users/hyunjimoon/tolzul") 
DATA_FILE = CURRENT_DIR / "spaceship_data.csv"
STAMPS_FILE = PARENT_DIR / "journal" / "fleet_stamps.json"
OUTPUT_FILE = CURRENT_DIR / "battle_dashboard.html"

def generate_matrix_row(pdata, issue_data):
    html = ""
    
    # Map columns to file suffixes for loose matching
    cols = ["introduction", "theory", "empirics", "discussion"]
    
    for col in cols:
        # Find matching file in pdata['structure']
        match = None
        for s in pdata["structure"]:
            if col in s["full_filename"]:
                match = s
                break
        
        if match:
            # Check for active issues
            has_issue = False
            issue_icon = ""
            issues_list = issue_data.get("issues", []) if issue_data else []
            for issue in issues_list:
                if issue["target_code"].startswith(pdata["name"][0]) and issue["stage"] != "CLOSED":
                    # Simple heuristic: if issue target matches project and column (e.g. U-T for Theory)
                    code_map = {"I": "introduction", "T": "theory", "E": "empirics", "D": "discussion"}
                    parts = issue["target_code"].split('-')
                    if len(parts) == 2:
                        if parts[0] == pdata["name"][0] and code_map.get(parts[1]) == col:
                            has_issue = True
                            issue_icon = "🐙" # Default icon
                            if issue["stage"] == "FLAG": issue_icon = "🏴"
                            elif issue["stage"] == "REVIEW": issue_icon = "🐢"
                            elif issue["stage"] == "BUILD": issue_icon = "🐅"
                            elif issue["stage"] == "MERGE": issue_icon = "🐙"
                            break
            
            issue_html = f'<div class="issue-flag">{issue_icon}</div>' if has_issue else ''
            
            # Paragraph Metrics
            para_metric = f'{match["current"]}/{match["target"]} ¶'
            
            # Dots (Progress)
            dots = ""
            # 1 dot per 2 paragraphs, max 5 dots
            num_dots = min(5, match["current"] // 2)
            for _ in range(num_dots):
                dots += '<div class="dot filled"></div>'
            
            active_cls = "active"
            
            html += f'''
            <div class="matrix-cell {active_cls}" onclick="openFile('{str(PARENT_DIR / pdata['folder'] / match['full_filename'])}')" title="{match['full_filename']}">
                {issue_html}
                <div class="cell-title">{match['file']}</div>
                <div class="cell-metrics">{para_metric}</div>
                <div class="cell-dots">{dots}</div>
            </div>
            '''
        else:
            html += '<div class="matrix-cell empty-cell" style="opacity:0.3; cursor:default;"></div>'
            
    return html

def generate_issue_queue_html(issue_data):
    if not issue_data or "issues" not in issue_data:
        return '<div style="padding:10px; color:#666;">No active issues.</div>'
        
    html = '<table class="issue-table"><thead><tr><th>ID</th><th>Target</th><th>Title</th><th>Stage</th><th>Next Action (Affordance)</th></tr></thead><tbody>'
    
    for issue in issue_data["issues"]:
        stage_cls = f"stage-{issue['stage']}"
        STAGE_ICONS = {
            "FLAG": "🏴",
            "REVIEW": "🐢",
            "BUILD": "🐅",
            "MERGE": "🐙"
        }
        icon = STAGE_ICONS.get(issue['stage'], "🏴")
        
        # Affordance Logic
        next_action = ""
        action_cls = "action-wait"
        onclick = ""
        
        if issue['stage'] == "FLAG":
            next_action = "👉 Review (Kwon)"
            action_cls = "action-review"
            onclick = f"updateIssue('{issue['id']}', 'advance')"
        elif issue['stage'] == "REVIEW":
            next_action = "👉 Build (Na)"
            action_cls = "action-build"
            onclick = f"updateIssue('{issue['id']}', 'advance')"
        elif issue['stage'] == "BUILD":
            next_action = "👉 Verify (Kim)"
            action_cls = "action-verify"
            onclick = f"updateIssue('{issue['id']}', 'advance')"
        elif issue['stage'] == "MERGE":
            next_action = "🔴 APPROVE (Commander)"
            action_cls = "action-approve" # Pulsing red button
            onclick = f"updateIssue('{issue['id']}', 'close')"
        elif issue['stage'] == "CLOSED":
            next_action = "✅ CLOSED"
            action_cls = "action-closed"
            onclick = ""
        
        # Extract Product Code (U, C, N) from target_code (e.g., U-I -> U)
        product_code = issue['target_code'].split('-')[0] if '-' in issue['target_code'] else "ALL"
        
        row_style = "cursor:grab;"
        if issue['stage'] == "CLOSED":
            row_style = "opacity: 0.5; text-decoration: line-through;"

        html += f'''
        <tr class="issue-row" data-product="{product_code}" data-stage="{issue['stage']}" draggable="true" ondragstart="drag(event, '{issue['id']}')" style="{row_style}">
            <td style="color:#aaa;">#{issue['id']}</td>
            <td>{issue['target_code']}</td>
            <td>{issue['title']}</td>
            <td><span class="stage-badge stage-{issue['stage']}">{icon} {issue['stage']}</span></td>
            <td><span class="action-badge {action_cls}" onclick="{onclick}" style="cursor:pointer;">{next_action}</span></td>
        </tr>
        '''
    html += '</tbody></table>'
    return html

def generate_agent_html(agents, agent_type):
    html = ""
    for agent in agents:
        log_html = ""
        if agent.get("log_file"):
            # Pre-format the onclick string to avoid backslashes in f-string expression
            onclick = f"openFile('{agent['log_file']}')"
            log_html = f'<div class="log-badge" onclick="{onclick}">{agent["log_icon"]}</div>'
            
        onclick_attr = f'onclick="{agent.get("onclick", "")}"' if agent.get("onclick") else ""
        cursor_style = "cursor:pointer;" if agent.get("onclick") else ""
        
        html += f'''
        <div class="agent-card {agent_type}" title="{agent['name']}-{agent['role']}" {onclick_attr} style="{cursor_style}">
            <div class="agent-icon">{agent['icon']}</div>
            <div class="agent-name">{agent['name']}</div>
            <div class="agent-role">{agent['role']}</div>
            {log_html}
        </div>
        '''
    return html

def load_stamps():
    """Load stamp collection from JSON file."""
    if not STAMPS_FILE.exists():
        return {"metadata": {"total_stamps": 0}, "stamps": []}
    
    try:
        with open(STAMPS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"metadata": {"total_stamps": 0}, "stamps": []}

def generate_stamp_panel_html(stamps_data):
    """Generate HTML for stamp collection panel."""
    stamps = stamps_data.get("stamps", [])
    total = stamps_data.get("metadata", {}).get("total_stamps", 0)
    
    html = f'''
    <div class="stamp-panel">
        <div class="stamp-header">
            <span class="stamp-icon">🇰🇷</span>
            <span class="stamp-title">STAMP COLLECTION</span>
            <span class="stamp-count">[{total}]</span>
        </div>
        <div class="stamp-list">
    '''
    
    # Show latest 3 stamps
    for stamp in stamps[-3:]:
        praise_html = f'<div class="stamp-praise">👍 {stamp.get("praise", "")}</div>' if stamp.get("praise") else ''
        tags_html = ' | '.join(stamp.get("tags", [])[:3])
        
        html += f'''
        <div class="stamp-item" data-id="{stamp['id']}">
            <div class="stamp-meta">#{stamp['id'].split('-')[1]} | {stamp['date']} | {tags_html}</div>
            <div class="stamp-insight">"{stamp['insight'][:60]}..."</div>
            {praise_html}
        </div>
        '''
    
    html += '''
        </div>
        <div class="stamp-actions">
            <button onclick="viewAllStamps()">View All</button>
            <button onclick="exportStamps()">Export for Handover</button>
        </div>
    </div>
    '''
    return html

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
    paragraphs = content.count('\n\n') + 1

    # Scores
    recency_score = max(0, 100 - (age_seconds / 86400 * 100))
    if age_hours < 1: recency_score = 100
    
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

def load_achievements():
    """Loads all achievements from the achievements file."""
    if not ACHIEVEMENTS_FILE.exists():
        return {"achievements": []}
    try:
        with open(ACHIEVEMENTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"achievements": []}

def load_critique_report():
    """Loads the critique report from its JSON file."""
    CRITIQUE_FILE = PARENT_DIR / "critique_report.json"
    if not CRITIQUE_FILE.exists():
        return {}
    try:
        with open(CRITIQUE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def load_issue_queue():
    """Loads the issue queue from its JSON file."""
    ISSUE_FILE = PARENT_DIR / "issue_queue.json"
    if not ISSUE_FILE.exists():
        return {}
    try:
        with open(ISSUE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def generate_color_wheel_svg(jeong, na, o, kim, moon):
    """Generates the SVG Color Wheel Interface."""
    
    # SVG Config - Optimized for Space
    width, height = 1000, 800
    cx, cy = width // 2, height // 2
    radius = 300  # Increased radius
    
    svg = f'''
    <div class="color-wheel-container">
        <svg viewBox="0 0 {width} {height}" class="color-wheel-svg" preserveAspectRatio="xMidYMid meet">
            <!-- Definitions for gradients/filters -->
            <defs>
                <filter id="glow">
                    <feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
                    <feMerge>
                        <feMergeNode in="coloredBlur"/>
                        <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                </filter>
                <radialGradient id="bg-gradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" stop-color="#1a1a2e" stop-opacity="1" />
                    <stop offset="100%" stop-color="#0b0c15" stop-opacity="0" />
                </radialGradient>
            </defs>
            
            <!-- Background Aura -->
            <circle cx="{cx}" cy="{cy}" r="{radius + 100}" fill="url(#bg-gradient)" opacity="0.5" />
            
            <!-- Central Hub (Moon) -->
            <g class="sector-center" onclick="{moon['onclick']}" style="cursor:pointer">
                <circle cx="{cx}" cy="{cy}" r="80" fill="#1a1a2e" stroke="#fbbf24" stroke-width="3" filter="url(#glow)"/>
                <text x="{cx}" y="{cy-40}" text-anchor="middle" fill="#fbbf24" font-size="24">{moon['icon']}</text>
                <text x="{cx}" y="{cy-15}" text-anchor="middle" fill="#fbbf24" font-size="10">COMMANDER</text>
                
                <!-- 3-Screen Workflow Visualization -->
                <!-- Screen 3: Products (Top) -->
                <g transform="translate({cx-40}, {cy-10})">
                    <rect x="0" y="0" width="80" height="25" rx="4" fill="rgba(255,255,255,0.1)" stroke="#fff" stroke-width="1"/>
                    <text x="40" y="17" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">U  C  N</text>
                </g>
                
                <!-- Screen 2: Logic (Center) -->
                <g transform="translate({cx-30}, {cy+20})">
                    <rect x="0" y="0" width="60" height="25" rx="4" fill="rgba(255, 204, 0, 0.2)" stroke="#fbbf24" stroke-width="1"/>
                    <text x="30" y="17" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">5  4</text>
                </g>
                
                <!-- Screen 1: Execution (Bottom) -->
                <g transform="translate({cx-50}, {cy+50})">
                    <rect x="0" y="0" width="100" height="25" rx="4" fill="rgba(0, 255, 157, 0.2)" stroke="#00ff9d" stroke-width="1"/>
                    <text x="50" y="17" text-anchor="middle" fill="#00ff9d" font-size="10" font-weight="bold">10 9 8 6</text>
                </g>
                
                <!-- Flow Arrows -->
                <path d="M {cx} {cy+50} L {cx} {cy+45}" stroke="#fff" stroke-width="1" marker-end="url(#arrow)"/>
                <path d="M {cx} {cy+20} L {cx} {cy+15}" stroke="#fff" stroke-width="1" marker-end="url(#arrow)"/>
            </g>
            
            <!-- Arrow Marker -->
            <defs>
                <marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth">
                    <path d="M0,0 L0,6 L9,3 z" fill="#fff" />
                </marker>
            </defs>
            
            <!-- Sectors -->
            <!-- 1. Kim (Red) - 12:00 -->
            <g class="sector-group" transform="translate({cx}, {cy-radius})">
                <line x1="0" y1="60" x2="0" y2="0" stroke="#ef4444" stroke-width="2" stroke-dasharray="4" opacity="0.5"/>
                <text x="0" y="-20" text-anchor="middle" fill="#ef4444" font-weight="bold" font-size="14">EVALUATION (K)</text>
                <!-- Agents -->
                <g transform="translate(-80, 30)">{generate_node_svg(kim[0], "#ef4444")}</g>
                <g transform="translate(0, 0)">{generate_node_svg(kim[1], "#ef4444")}</g>
                <g transform="translate(80, 30)">{generate_node_svg(kim[2], "#ef4444")}</g>
            </g>
            
            <!-- 2. Na (Orange) - 3:00 -->
            <g class="sector-group" transform="translate({cx+radius}, {cy})">
                <line x1="-60" y1="0" x2="0" y2="0" stroke="#f97316" stroke-width="2" stroke-dasharray="4" opacity="0.5"/>
                <text x="20" y="5" text-anchor="start" fill="#f97316" font-weight="bold" font-size="14">STRUCTURE (G)</text>
                <!-- Agents -->
                <g transform="translate(-30, -80)">{generate_node_svg(na[0], "#f97316")}</g>
                <g transform="translate(0, 0)">{generate_node_svg(na[1], "#f97316")}</g>
                <g transform="translate(-30, 80)">{generate_node_svg(na[2], "#f97316")}</g>
            </g>
            
            <!-- 3. Jeong (Green) - 6:00 -->
            <g class="sector-group" transform="translate({cx}, {cy+radius})">
                <line x1="0" y1="-60" x2="0" y2="0" stroke="#22c55e" stroke-width="2" stroke-dasharray="4" opacity="0.5"/>
                <text x="0" y="35" text-anchor="middle" fill="#22c55e" font-weight="bold" font-size="14">EXECUTION (J)</text>
                <!-- Agents -->
                <g transform="translate(80, -30)">{generate_node_svg(jeong[0], "#22c55e")}</g>
                <g transform="translate(0, 0)">{generate_node_svg(jeong[1], "#22c55e")}</g>
                <g transform="translate(-80, -30)">{generate_node_svg(jeong[2], "#22c55e")}</g>
            </g>
            
            <!-- 4. O (Blue) - 9:00 -->
            <g class="sector-group" transform="translate({cx-radius}, {cy})">
                <line x1="60" y1="0" x2="0" y2="0" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4" opacity="0.5"/>
                <text x="-20" y="5" text-anchor="end" fill="#3b82f6" font-weight="bold" font-size="14">ORIGIN (O)</text>
                <!-- Agents -->
                <g transform="translate(30, 80)">{generate_node_svg(o[0], "#3b82f6")}</g>
                <g transform="translate(0, 0)">{generate_node_svg(o[1], "#3b82f6")}</g>
                <g transform="translate(30, -80)">{generate_node_svg(o[2], "#3b82f6")}</g>
            </g>
            
            <!-- Signal Path -->
            <path id="signal-path" d="M {cx} {cy+radius} A {radius} {radius} 0 0 1 {cx+radius} {cy} A {radius} {radius} 0 0 1 {cx} {cy-radius} A {radius} {radius} 0 0 1 {cx-radius} {cy} Z" fill="none" stroke="none"/>
            
            <!-- Signal Particle -->
            <circle r="6" fill="#fff" filter="url(#glow)">
                <animateMotion dur="6s" repeatCount="indefinite" path="M {cx} {cy+radius} A {radius} {radius} 0 0 1 {cx+radius} {cy} A {radius} {radius} 0 0 1 {cx} {cy-radius} A {radius} {radius} 0 0 1 {cx-radius} {cy} Z" />
            </circle>
        </svg>
    </div>
    '''
    return svg

def generate_node_svg(agent, color):
    """Helper to generate an individual agent node SVG."""
    onclick = agent.get('onclick', '')
    cursor = "pointer" if onclick else "default"
    
    return f'''
    <g class="agent-node" onclick="{onclick}" style="cursor: {cursor}">
        <circle r="25" fill="#1a1a2e" stroke="{color}" stroke-width="2"/>
        <text text-anchor="middle" dy="5" fill="#fff" font-size="16">{agent['icon']}</text>
        <text text-anchor="middle" dy="40" fill="{color}" font-size="10">{agent['name']}</text>
        <text text-anchor="middle" dy="52" fill="#888" font-size="8">{agent['role']}</text>
    </g>
    '''

def get_obsidian_url(paper_folder, filename):
    """Generates an Obsidian URL for a given file."""
    # Base path relative to vault root
    # Vault: tolzul
    # Root: /Users/hyunjimoon/tolzul
    # File: Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/{paper_folder}/📝product/{filename}
    
    base_path = "Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output"
    full_path = f"{base_path}/{paper_folder}/📝product/{filename}"
    
    # URL Encode
    import urllib.parse
    encoded_path = urllib.parse.quote(full_path)
    
    return f"obsidian://open?vault=tolzul&file={encoded_path}"

def generate_paper_deck():
    """Generates the Paper Deck (Obsidian Links) HTML."""
    
    papers = [
        {"id": "U", "name": "P1: U-Shape", "folder": "P1✌️", "icon": "✌️", "color": "#00ff9d"},
        {"id": "C", "name": "P2: Commit", "folder": "P2🦾", "icon": "🦾", "color": "#ffcc00"},
        {"id": "N", "name": "P3: News", "folder": "P3🤹", "icon": "🤹", "color": "#ff0099"}
    ]
    
    chapters = [
        {"id": "c1", "name": "Chap 1", "file": "chap1_intro.md"},
        {"id": "c2", "name": "Chap 2", "file": "chap2_theory.md"},
        {"id": "c3", "name": "Chap 3", "file": "chap3_empirics.md"},
        {"id": "c4", "name": "Chap 4", "file": "chap4_discussion.md"}
    ]
    
    html = '<div class="paper-deck-dock">'
    
    for p in papers:
        html += f'''
        <div class="paper-card" style="border: 1px solid {p['color']}; background: rgba(0,0,0,0.5); padding: 8px 12px; border-radius: 8px; width: 100px; transition: all 0.2s;">
            <div class="paper-header" style="color: {p['color']}; font-weight: bold; font-size: 0.75rem; margin-bottom: 6px; display: flex; align-items: center; justify-content: center; gap: 4px;">
                <span>{p['icon']}</span> {p['id']}
            </div>
            <div class="chapter-list" style="display: flex; flex-direction: column; gap: 3px;">
        '''
        
        for c in chapters:
            url = get_obsidian_url(p['folder'], c['file'])
            html += f'''
                <a href="{url}" class="chapter-link" style="color: #aaa; text-decoration: none; font-size: 0.65rem; padding: 2px 4px; border-radius: 3px; transition: all 0.2s; display: block; text-align: center;">
                    {c['name']}
                </a>
            '''
        
        html += '</div></div>'
        
    html += '</div>'
    
    # Add CSS for hover effects
    html += '''
    <style>
        .paper-card:hover { transform: translateY(-5px); background: rgba(255,255,255,0.05); }
        .chapter-link:hover { background: rgba(255,255,255,0.2); color: #fff; }
    </style>
    '''
    
    return html

def generate_completion_index(papers):
    """Generates a Completion Index visual (7, 9, 11, 5)."""
    html = '<div class="completion-index" style="position: absolute; top: 20px; left: 20px; background: rgba(0,0,0,0.6); padding: 15px; border-radius: 10px; border: 1px solid var(--border-dim);">'
    html += '<div style="font-size: 0.8rem; font-weight: bold; margin-bottom: 10px; color: #fff;">📊 Completion Index</div>'
    
    for pid, p in papers.items():
        html += f'<div style="margin-bottom: 8px; display: flex; align-items: center; gap: 10px;">'
        html += f'<span style="font-size: 1.2rem;">{p["icon"]}</span>'
        
        # Progress Bars for 4 chapters
        targets = [7, 9, 11, 5] # Intro, Theory, Empirics, Discuss
        
        # Get current counts from structure status if available
        current_counts = [0, 0, 0, 0]
        if 'structure' in p:
            # p['structure'] is a list of dicts. We assume order matches files list.
            for i, s in enumerate(p['structure']):
                if i < 4: current_counts[i] = s['current']
        
        html += '<div style="display: flex; gap: 2px;">'
        for i, target in enumerate(targets):
            current = current_counts[i]
            pct = min(100, (current / target) * 100)
            
            if p['state'] == 'green': color_hex = '#00ff9d'
            elif p['state'] == 'yellow': color_hex = '#ffcc00'
            else: color_hex = '#ff0099'
            
            html += f'''
            <div style="width: 30px; height: 6px; background: #333; border-radius: 2px; overflow: hidden;" title="Chap {i+1}: {current}/{target} Para">
                <div style="width: {pct}%; height: 100%; background: {color_hex};"></div>
            </div>
            '''
        html += '</div></div>'
        
    html += '</div>'
    return html

def generate_live_ticker():
    """Generates the Live Ticker for O-Agent updates."""
    return '''
    <div class="live-ticker" style="position: absolute; top: 20px; right: 20px; width: 300px; background: rgba(0,0,0,0.8); border: 1px solid var(--jeong-green); border-radius: 5px; padding: 10px; font-family: 'Courier New', monospace; font-size: 0.75rem; overflow: hidden; display: flex; flex-direction: column;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 5px; border-bottom: 1px solid #333; padding-bottom: 3px;">
            <span style="color: var(--jeong-green); font-weight: bold;">📡 FLEET COMMS</span>
            <span id="ticker-timer" style="color: #666;">Updating...</span>
        </div>
        <div id="ticker-content" style="flex: 1; overflow-y: hidden; display: flex; flex-direction: column; justify-content: flex-end;">
            <div class="ticker-item" style="margin-bottom: 5px;">> 11OU: Connecting to Mgmt Sci DB...</div>
            <div class="ticker-item" style="margin-bottom: 5px;">> 12OC: Scanning Strategy Journals...</div>
        </div>
    </div>
    <script>
        const messages = {
            "11OU": [
                "Reviewer 2 is smiling... suspicious. 🤔",
                "Vagueness index rising. Good? Bad? Who knows. 🤷",
                "Mgmt Science E&I dept pinged. They want more U-shapes. 📉📈",
                "Found a citation that contradicts us. Deleting it... just kidding. 🤥",
                "Calculating p-value... p < 0.05! Party time! 🎉"
            ],
            "12OC": [
                "Strategy alignment 98%... World domination imminent. 🌍",
                "First Mover Curse detected. Suggesting we move second. 🥈",
                "Commitment trap engaged. We are stuck, but happily! 🔒",
                "Network effects analyzing... It's a bubble! 🎈",
                "Competitor analysis: They are vague. We win. 🏆"
            ],
            "13ON": [
                "Ops Mgmt efficiency at 110%. Breaking laws of physics. 🚀",
                "Newsvendor model says: Buy more paper! 📰",
                "FOMO levels critical. Everyone is buying NVIDIA. 📉",
                "Flexibility cost calculated. It's expensive to be free. 💸",
                "LIDAR vs Vision? Why not both? Oh, budget. 💰"
            ]
        };
        
        function updateTicker() {
            const agents = ["11OU", "12OC", "13ON"];
            const agent = agents[Math.floor(Math.random() * agents.length)];
            const msgs = messages[agent];
            const msg = msgs[Math.floor(Math.random() * msgs.length)];
            
            const div = document.createElement('div');
            div.className = 'ticker-item';
            div.style.marginBottom = '5px';
            div.style.color = agent === '11OU' ? '#00ff9d' : (agent === '12OC' ? '#ffcc00' : '#ff0099');
            div.innerHTML = `> <b>${agent}</b>: ${msg}`;
            
            const container = document.getElementById('ticker-content');
            container.insertBefore(div, container.firstChild);
            
            if (container.children.length > 4) {
                container.removeChild(container.lastChild);
            }
            
            document.getElementById('ticker-timer').innerText = new Date().toLocaleTimeString();
        }
        
        setInterval(updateTicker, 3000); // Update every 3 seconds for fun

        function showMonitorInfo(screen) {
            let msg = "";
            let title = "";
            if (screen === 'LEFT') {
                title = "LEFT VERTICAL: ORIGIN BASE";
                msg = "Agents: 11OU, 12OC, 13ON\\nRole: Data Ingestion & Mgmt Science\\nStatus: Active Scanning";
            } else if (screen === 'CENTER') {
                title = "CENTER MAIN: OPS THEATER";
                msg = "Agents: J-Group (Execution) & G-Group (Structure)\\nRole: Drafting & Logic Construction\\nStatus: Collaborative Mode";
            } else if (screen === 'BOTTOM') {
                title = "BOTTOM SMALL: COMMAND DECK";
                msg = "Agents: 7M (Commander)\\nTools: Antigravity & NotebookLM\\nRole: Strategic Direction & Verification";
            }
            alert(title + "\\n\\n" + msg);
        }

        function openAgentWorkspace(agentId) {
            // Construct Obsidian URL for Agent Workspace
            // Format: O(K(JG(O))) -> Nested structure concept
            // For now, we link to a specific agent note in the vault
            
            // Base path for agents
            const basePath = "Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/agents";
            const filename = `agent_${agentId.toLowerCase()}.md`;
            const fullPath = `${basePath}/${filename}`;
            const encodedPath = encodeURIComponent(fullPath);
            
            const url = `obsidian://open?vault=tolzul&file=${encodedPath}`;
            
            // Create a temporary link and click it
            // Note: In a real browser this might be blocked, but for local use it often works
            window.location.href = url;
            
            console.log(`Opening workspace for ${agentId}: ${url}`);
        }
    </script>
    '''

def generate_dashboard():
    print("🎨 Generating Jeolla Left Navy Dashboard (MFS View)...")

    # Load Data
    achievements = load_achievements()
    critique_data = load_critique_report()
    issue_data = load_issue_queue()
    stamps_data = load_stamps()


    # --- The 13 Deputies (Color Wheel Model) ---
    
    # 1. Jeong (Green) - Execution (6:00) -> 8, 9, 10
    jeong_agents = [
        {"id": "j1", "name": "8JID", "role": "Intro", "icon": "🐢", "onclick": "openAgentWorkspace('8JID')"},
        {"id": "j2", "name": "9JT", "role": "Theory", "icon": "🐢", "onclick": "openAgentWorkspace('9JT')"},
        {"id": "j3", "name": "10JE", "role": "Empirics", "icon": "🐢", "onclick": "openAgentWorkspace('10JE')"}
    ]

    # 2. Na (Orange) - Structure (3:00) -> 6, 5, 4
    na_agents = [
        {"id": "n1", "name": "6GID", "role": "Struct", "icon": "🐅", "onclick": "openAgentWorkspace('6GID')"},
        {"id": "n2", "name": "5GT", "role": "Logic", "icon": "🏗️", "onclick": "openAgentWorkspace('5GT')"},
        {"id": "n3", "name": "4GE", "role": "Code", "icon": "💻", "onclick": "openAgentWorkspace('4GE')"}
    ]

    # 3. O (Blue) - Origin (9:00) -> 11, 12, 13
    o_agents = [
        {"id": "o1", "name": "11OU", "role": "MgmtSci", "icon": "💾", "onclick": "openAgentWorkspace('11OU')"},
        {"id": "o2", "name": "12OC", "role": "Strategy", "icon": "📚", "onclick": "openAgentWorkspace('12OC')"},
        {"id": "o3", "name": "13ON", "role": "OpsMgmt", "icon": "📜", "onclick": "openAgentWorkspace('13ON')"}
    ]

    # 4. Kim (Red) - Evaluation (12:00) -> 1, 2, 3
    kim_agents = [
        {"id": "k1", "name": "1KU", "role": "Audit U", "icon": "🛡️", "onclick": "openAgentWorkspace('1KU')"},
        {"id": "k2", "name": "2KC", "role": "Audit C", "icon": "⚖️", "onclick": "openAgentWorkspace('2KC')"},
        {"id": "k3", "name": "3KN", "role": "Audit N", "icon": "💪", "onclick": "openAgentWorkspace('3KN')"}
    ]

    # 5. Moon (Center) - Commander -> 7M
    moon_agent = {"id": "m1", "name": "7M", "role": "Commander", "icon": "🌙", "onclick": "openAgentWorkspace('7M')"}

    # Fleet Data
    # U: Focused (All modules active)
    papers = {
        "U": {
            "name": "U: U-Shaped", "icon": "✌️", "state": "green", "desc": "Mature", 
            "folder": "✌️U",
            "target_words": 8000, 
            "structure_target": {
                "chap1_intro.md": 7, 
                "chap2_theory.md": 9, 
                "chap3_empirics.md": 11, 
                "chap4_discussion.md": 5
            }, 
            "files": ["chap1_intro.md", "chap2_theory.md", "chap3_empirics.md", "chap4_discussion.md"], 
            "current_rp": 1
        },
        "C": {
            "name": "C: Commitment", "icon": "🦾", "state": "yellow", "desc": "Struct OK", 
            "folder": "🦾C",
            "target_words": 6000, 
            "structure_target": {
                "chap1_intro.md": 7, 
                "chap2_theory.md": 9, 
                "chap3_empirics.md": 11, 
                "chap4_discussion.md": 5
            }, 
            "files": ["chap1_intro.md", "chap2_theory.md", "chap3_empirics.md", "chap4_discussion.md"], 
            "current_rp": 1
        },
        "N": {
            "name": "N: Newsvendor", "icon": "🤹", "state": "red", "desc": "Redesign", 
            "folder": "🤹N",
            "target_words": 5000, 
            "structure_target": {
                "chap1_intro.md": 7, 
                "chap2_theory.md": 9, 
                "chap3_empirics.md": 11, 
                "chap4_discussion.md": 5
            }, 
            "files": ["chap1_intro.md", "chap2_theory.md", "chap3_empirics.md", "chap4_discussion.md"], 
            "current_rp": 0
        }
    }
    
    # Calculate Metrics
    for pid, pdata in papers.items():
        metrics = {"words": 0, "figures": 0, "citations": 0, "recency_sum": 0, "risk_max": 0, "paragraphs": 0, "target_paragraphs": 0}
        count = 0
        structure_status = []
        
        for fname in pdata["files"]:
            fpath = PARENT_DIR / pdata["folder"] / fname
            m = get_file_metrics(fpath)
            
            # Get Risk from Critique Report if available
            risk_level = 0
            critiques_list = []
            if fname in critique_data:
                risk_level = critique_data[fname].get("risk_level", 0)
                critiques_list = critique_data[fname].get("critiques", [])
            
            metrics["words"] += m["words"]
            metrics["figures"] += m["figures"]
            metrics["citations"] += m["citations"]
            metrics["recency_sum"] += m["recency_score"]
            metrics["risk_max"] = max(metrics["risk_max"], m["risk"])
            
            target_para = pdata["structure_target"].get(fname, 0)
            metrics["paragraphs"] += m["paragraphs"]
            metrics["target_paragraphs"] += target_para
            
            structure_status.append({
                "file": fname.replace(".md", ""),
                "full_filename": fname,
                "current": m["paragraphs"],
                "target": target_para,
                "risk_level": risk_level,
                "critiques": critiques_list
            })
            count += 1
        
        pdata["structure"] = structure_status
        word_progress = min(100, (metrics["words"] / pdata["target_words"]) * 100)
        recency_avg = metrics["recency_sum"] / max(1, count) if count > 0 else 0
        final_score = int((word_progress * 0.6) + (recency_avg * 0.4))
        pdata["score"] = final_score
        pdata["metrics"] = metrics
        
        if final_score >= 80: pdata["state"] = "green"
        elif final_score >= 50: pdata["state"] = "yellow"
        else: pdata["state"] = "red"


    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MFS Control Tower v2.6</title>
    <style>
        :root {{
            --bg-color: #0b0c15;
            --jeong-green: #00ff9d;  /* Turtle Green */
            --na-orange: #ffcc00;    /* Tiger Orange */
            --verify-pink: #ff0099;
            --glass-bg: rgba(20, 30, 40, 0.6);
            --border-dim: rgba(255, 255, 255, 0.1);
        }}
        
        body {{
            background-color: var(--bg-color);
            color: #fff;
            font-family: 'Courier New', monospace;
            margin: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            background-image: linear-gradient(0deg, rgba(255,255,255,0.03) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
            background-size: 50px 50px;
        }}

        /* Layout Containers */
        .dashboard-container {{ display: flex; flex: 1; overflow: hidden; }}
        .dashboard-left {{ flex: 1; display: flex; flex-direction: column; padding: 10px; overflow-y: auto; }}
        .dashboard-right {{ width: 450px; border-left: 1px solid var(--border-dim); background: rgba(0,0,0,0.3); display: flex; flex-direction: column; }}

        /* Header */
        .header {{
            height: 60px; display: flex; align-items: center; justify-content: space-between; padding: 0 20px;
            background: rgba(0,0,0,0.8); border-bottom: 1px solid var(--border-dim); flex-shrink: 0;
        }}
        .brand {{ font-size: 1.5rem; font-weight: bold; letter-spacing: 2px; color: #fff; }}
        .brand span {{ color: var(--jeong-green); }}
        
        /* Main Grid */
        .pantos-grid {{
            flex: 1;
            display: grid;
            grid-template-columns: 120px 1fr 1fr 1fr 1fr 100px; /* Label, I, T, E, D, Verify */
            grid-template-rows: 40px 60px 1fr 1fr 1fr 60px 40px; /* Labels, Jeong, U, C, N, KwonNa, Labels */
            gap: 5px;
            min-height: 600px;
        }}

        /* Zones */
        .zone-label {{ display: flex; align-items: center; justify-content: center; font-weight: bold; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }}
        .jeong-zone {{ background: rgba(0, 255, 157, 0.1); color: var(--jeong-green); border: 1px solid var(--jeong-green); }}
        .kwon-zone {{ background: rgba(255, 204, 0, 0.1); color: var(--na-orange); border: 1px solid var(--na-orange); }}
        
        /* Color Wheel Interface */
        .color-wheel-container {{ width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; position: relative; }}
        .color-wheel-svg {{ width: 100%; height: 100%; max-width: 1200px; max-height: 900px; }}
        .sector-group text {{ font-family: 'Courier New', monospace; letter-spacing: 1px; }}
        .agent-node circle {{ transition: all 0.3s ease; }}
        .agent-node:hover circle {{ stroke-width: 4px; filter: url(#glow); }}
        .agent-node:hover text {{ font-weight: bold; }}
        
        /* Paper Deck Dock */
        .paper-deck-dock {{
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(10, 10, 20, 0.8);
            border: 1px solid var(--border-dim);
            border-radius: 12px;
            padding: 10px 20px;
            display: flex;
            gap: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            z-index: 100;
        }}
        
        /* Agents */
        .agent-card {{ display: flex; flex-direction: column; align-items: center; justify-content: center; background: rgba(255,255,255,0.05); border: 1px solid var(--border-dim); position: relative; transition: all 0.2s; }}
        .agent-card:hover {{ background: rgba(255,255,255,0.1); }}
        .jeong-agent {{ border-top: 2px solid var(--jeong-green); }}
        .na-agent {{ border-bottom: 2px solid var(--na-orange); }}
        
        .agent-icon {{ font-size: 1.5rem; }}
        .agent-name {{ font-size: 1.1rem; margin-top: 4px; font-weight: 800; text-shadow: 0 0 5px currentColor; letter-spacing: 1px; }}
        .agent-role {{ font-size: 0.6rem; color: #aaa; font-weight: normal; }}
        .agent-role {{ font-size: 0.6rem; color: #888; }}
        
        .log-badge {{ position: absolute; top: 2px; right: 2px; font-size: 0.7rem; cursor: pointer; }}

        /* Project Rows */
        .project-label {{ display: flex; flex-direction: column; align-items: center; justify-content: center; background: rgba(255,255,255,0.05); border-left: 3px solid #fff; }}
        .p-icon {{ font-size: 2rem; }}
        .p-name {{ font-size: 1.2rem; font-weight: bold; }}
        .p-desc {{ font-size: 0.6rem; color: #aaa; }}

        /* Matrix Cells */
        .matrix-cell {{ background: rgba(255,255,255,0.02); border: 1px solid var(--border-dim); padding: 8px; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.2s; cursor: pointer; }}
        .matrix-cell:hover {{ background: rgba(255,255,255,0.08); border-color: #fff; }}
        .matrix-cell.active {{ border-color: #666; }}
        .cell-title {{ font-size: 0.7rem; color: #888; }}
        .cell-metrics {{ font-size: 0.8rem; color: #fff; font-weight: bold; margin-top: 5px; }}
        .cell-dots {{ display: flex; gap: 2px; margin-top: 5px; }}
        .dot {{ width: 5px; height: 5px; border-radius: 50%; background: #333; }}
        .dot.filled {{ background: #fff; }}
        .issue-flag {{ position: absolute; top: -5px; right: -5px; font-size: 0.8rem; z-index: 10; animation: bounce 2s infinite; }}

        /* Verifier Column */
        .verifier-cell {{ display: flex; flex-direction: column; align-items: center; justify-content: center; background: rgba(255, 0, 153, 0.05); border-right: 2px solid var(--verify-pink); }}
        .v-icon {{ font-size: 1.5rem; }}
        .v-name {{ font-size: 0.7rem; color: var(--verify-pink); font-weight: bold; }}
        .v-role {{ font-size: 0.6rem; color: #aaa; text-align: center; padding: 2px; }}

        /* Server Status */
        .server-status {{ font-size: 0.7rem; color: #666; display: flex; align-items: center; gap: 5px; }}
        .status-dot {{ width: 8px; height: 8px; border-radius: 50%; background: #444; }}
        .status-dot.online {{ background: var(--jeong-green); box-shadow: 0 0 5px var(--jeong-green); }}

        /* Issue Queue */
        .issue-queue {{ flex: 1; overflow-y: auto; font-size: 0.7rem; }}
        .issue-header {{ padding: 10px; background: rgba(0,0,0,0.5); border-bottom: 1px solid var(--border-dim); font-weight: bold; color: #aaa; text-transform: uppercase; letter-spacing: 1px; }}
        .issue-table {{ width: 100%; border-collapse: collapse; }}
        .issue-table th {{ text-align: left; color: #888; border-bottom: 1px solid #444; padding: 8px; position: sticky; top: 0; background: #111; z-index: 10; }}
        .issue-table td {{ padding: 8px; border-bottom: 1px solid #222; }}
        
        .stage-badge {{ padding: 2px 6px; border-radius: 4px; font-weight: bold; display: inline-block; }}
        .stage-FLAG {{ background: #333; color: #fff; border: 1px solid #666; }}
        .stage-REVIEW {{ background: rgba(0, 255, 157, 0.2); color: var(--jeong-green); border: 1px solid var(--jeong-green); }}
        .stage-BUILD {{ background: rgba(255, 204, 0, 0.2); color: var(--na-orange); border: 1px solid var(--na-orange); }}
        .stage-MERGE {{ background: rgba(255, 0, 255, 0.2); color: #f0f; border: 1px solid #f0f; }}

        .action-badge {{ padding: 4px 8px; border-radius: 4px; font-size: 0.85em; font-weight: bold; display: inline-block; }}
        .action-wait {{ color: #666; }}
        .action-review {{ background: rgba(0, 255, 0, 0.1); color: var(--jeong-green); border: 1px solid var(--jeong-green); }}
        .action-build {{ background: rgba(255, 165, 0, 0.1); color: var(--na-orange); border: 1px solid var(--na-orange); }}
        .action-verify {{ background: rgba(255, 0, 255, 0.1); color: var(--verify-pink); border: 1px solid var(--verify-pink); }}
        
        .action-approve {{ background: rgba(255, 0, 0, 0.2); color: #ff4444; border: 1px solid #ff4444; animation: pulse 2s infinite; cursor: pointer; }}
        .action-closed {{ background: #333; color: #888; border: 1px solid #555; }}
        
        @keyframes pulse {{ 0% {{ box-shadow: 0 0 0 0 rgba(255, 68, 68, 0.4); }} 70% {{ box-shadow: 0 0 0 10px rgba(255, 68, 68, 0); }} 100% {{ box-shadow: 0 0 0 0 rgba(255, 68, 68, 0); }} }}
        @keyframes bounce {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-3px); }} }}

        /* Filter Buttons */
        .filter-btn {{ background: rgba(255,255,255,0.05); border: 1px solid var(--border-dim); color: #aaa; padding: 4px 8px; margin-left: 5px; cursor: pointer; font-family: 'Courier New', monospace; font-size: 0.7rem; border-radius: 3px; transition: all 0.2s; }}
        .filter-btn:hover {{ background: rgba(255,255,255,0.15); border-color: #fff; color: #fff; }}
        .filter-btn.active {{ background: var(--jeong-green); border-color: var(--jeong-green); color: var(--bg-color); font-weight: bold; }}

        .signal-dot {{ position: absolute; width: 8px; height: 8px; border-radius: 50%; background: #fff; pointer-events: none; z-index: 100; transition: all 0.5s ease-in-out; }}
        
        /* Stamp Panel CSS */
        .stamp-panel {{
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            border: 2px solid #c9a227;  /* Korean gold */
            border-radius: 8px;
            padding: 15px;
            margin-top: 20px;
        }}

        .stamp-header {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 15px;
            border-bottom: 1px solid #c9a227;
            padding-bottom: 10px;
        }}

        .stamp-icon {{ font-size: 24px; }}
        .stamp-title {{ color: #c9a227; font-weight: bold; font-size: 0.9rem; }}
        .stamp-count {{ color: #888; margin-left: auto; font-size: 0.8rem; }}

        .stamp-item {{
            background: rgba(201, 162, 39, 0.1);
            border-left: 3px solid #c9a227;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 0 5px 5px 0;
        }}

        .stamp-meta {{ color: #888; font-size: 11px; margin-bottom: 5px; }}
        .stamp-insight {{ color: #fff; font-style: italic; font-size: 0.8rem; }}
        .stamp-praise {{ color: #4ade80; font-size: 12px; margin-top: 5px; }}

        .stamp-actions {{
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }}

        .stamp-actions button {{
            background: transparent;
            border: 1px solid #c9a227;
            color: #c9a227;
            padding: 5px 10px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 0.7rem;
        }}

        .stamp-actions button:hover {{
            background: #c9a227;
            color: #000;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="brand">MFS <span>CONTROL TOWER</span></div>
        <div class="server-status">
            <div class="monitor-map" style="display: flex; flex-direction: column; align-items: flex-end; margin-right: 15px; opacity: 0.8;" title="Physical Monitor Layout: Left(Vertical), Center(Main), Bottom(Small)">
                <div style="font-size: 0.6rem; color: #888; margin-bottom: 2px;">PHYSICAL LAYOUT</div>
                <div style="display: flex; gap: 4px; align-items: flex-end;">
                    <div style="width: 10px; height: 18px; background: #333; border: 1px solid #555; border-radius: 2px; cursor: pointer;" title="Left Vertical: O-Base (11,12,13)" onclick="showMonitorInfo('LEFT')"></div>
                    <div style="display: flex; flex-direction: column; gap: 2px; align-items: center;">
                        <div style="width: 26px; height: 14px; background: var(--jeong-green); border: 1px solid var(--jeong-green); border-radius: 2px; box-shadow: 0 0 5px var(--jeong-green); cursor: pointer;" title="Center Main: J-G Ops" onclick="showMonitorInfo('CENTER')"></div>
                        <div style="width: 18px; height: 8px; background: #333; border: 1px solid #555; border-radius: 2px; cursor: pointer;" title="Bottom Small: M-Command" onclick="showMonitorInfo('BOTTOM')"></div>
                    </div>
                </div>
            </div>
            <div class="status-dot" id="server-dot"></div>
            <span id="server-text">Link Offline</span>
        </div>
    </div>

    <div class="dashboard-container">
        <!-- LEFT PANEL: Matrix & Status -->
        <div class="dashboard-left">
            <div class="color-wheel-wrapper" style="flex: 1; display: flex; justify-content: center; align-items: center; background: radial-gradient(circle at center, #1a1a2e 0%, #0b0c15 70%); flex-direction: column; position: relative;">
                {generate_completion_index(papers)}
                {generate_color_wheel_svg(jeong_agents, na_agents, o_agents, kim_agents, moon_agent)}
                {generate_paper_deck()}
            </div>
        </div>
        </div>

        <!-- RIGHT PANEL: Issue Tracker -->
        <div class="dashboard-right">
            <div class="issue-header">
                📋 Issue Command Center
                <span style="float: right;">
                    <button class="filter-btn active" onclick="filterIssues('ALL')">ALL</button>
                    <button class="filter-btn" onclick="filterIssues('U')">U</button>
                    <button class="filter-btn" onclick="filterIssues('C')">C</button>
                    <button class="filter-btn" onclick="filterIssues('N')">N</button>
                </span>
            </div>
            <div class="issue-queue">
                <table class="issue-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Task</th>
                            <th>Team</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody id="issue-body">
                        <!-- Issues injected by JS -->
                    </tbody>
                </table>
            </div>
            
            <!-- FLEET COMMS (Bottom Right) -->
            {generate_live_ticker().replace('position: absolute; top: 20px; right: 20px; width: 300px;', 'flex: 1; width: auto; margin: 10px; position: relative; top: auto; right: auto; height: auto;')}
            
            <!-- Stamp Collection Panel -->
            <div class="stamp-panel" style="margin: 10px; margin-top: 0;">
                <div class="stamp-header">
                    <span class="stamp-icon">🎖️</span>
                    <span class="stamp-title">STAMP COLLECTION</span>
                    <span class="stamp-count">[{len(stamps_data)}]</span>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        function filterIssues(product) {{
            const rows = document.querySelectorAll('.issue-row');
            const btns = document.querySelectorAll('.filter-btn');
            
            // Update Buttons
            btns.forEach(b => {{
                if (b.innerText.startsWith(product) || (product === 'ALL' && b.innerText === 'ALL')) {{
                    b.classList.add('active');
                }} else {{
                    b.classList.remove('active');
                }}
            }});

            // Filter Rows
            rows.forEach(row => {{
                const rowProduct = row.dataset.product;
                const rowStage = row.dataset.stage;
                
                let show = false;
                
                if (product === 'CLOSED') {{
                    // Only show closed issues
                    if (rowStage === 'CLOSED') show = true;
                }} else {{
                    // Show active issues matching product
                    if (rowStage !== 'CLOSED') {{
                        if (product === 'ALL' || rowProduct === product) show = true;
                    }}
                }}
                
                row.style.display = show ? '' : 'none';
            }});
        }}
        
        function updateIssue(issueId, action) {{
            if (!action) return;
            
            fetch('/update_issue', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ issue_id: issueId, action: action }})
            }})
            .then(r => {{
                if (r.ok) window.location.reload();
                else console.error("Update failed");
            }});
        }}
        
        function launchApp(appName) {{
            if (!appName) return;
            console.log("Launching " + appName);
            
            fetch('/launch', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ app: appName }})
            }})
            .then(r => {{
                if (r.ok) console.log("Launched " + appName);
                else console.error("Launch failed");
            }});
        }}

        function openFile(path) {{
            if (!path || path === 'None') return;
            fetch(`/open?file=${{encodeURIComponent(path)}}`)
                .then(r => console.log("Opened", path))
                .catch(e => console.error(e));
        }}

        // Signal Flow Visualization
        function spawnSignal() {{
            const grid = document.getElementById('main-grid');
            const dot = document.createElement('div');
            dot.className = 'signal-dot';
            document.body.appendChild(dot);

            // Coordinates (Hardcoded for demo, normally dynamic)
            // We can try to find elements dynamically
            try {{
                const moon = document.getElementById('zone-moon').getBoundingClientRect();
                const jeong = document.querySelector('.jeong-agent').getBoundingClientRect(); // First Jeong agent
                const na = document.querySelector('.na-agent').getBoundingClientRect(); // First Na agent
                const kim = document.querySelector('.verifier-cell').getBoundingClientRect(); // First Verifier
                
                dot.style.left = (moon.left + moon.width/2) + 'px';
                dot.style.top = (moon.top + moon.height/2) + 'px';
                dot.style.opacity = 1;

                setTimeout(() => {{ 
                    dot.style.left = (jeong.left + jeong.width/2) + 'px'; 
                    dot.style.top = (jeong.top + jeong.height/2) + 'px'; 
                    dot.style.boxShadow = '0 0 15px var(--jeong-green)'; 
                }}, 100);
                
                setTimeout(() => {{ 
                    dot.style.left = (na.left + na.width/2) + 'px'; 
                    dot.style.top = (na.top + na.height/2) + 'px'; 
                    dot.style.boxShadow = '0 0 15px var(--na-orange)'; 
                }}, 1000);
                
                setTimeout(() => {{ 
                    dot.style.left = (kim.left + kim.width/2) + 'px'; 
                    dot.style.top = (kim.top + kim.height/2) + 'px'; 
                    dot.style.boxShadow = '0 0 15px var(--verify-pink)'; 
                }}, 2000);
                
                setTimeout(() => {{ dot.remove(); }}, 3000);
            }} catch(e) {{
                dot.remove();
            }}
        }}

        setInterval(spawnSignal, 4000);
        spawnSignal(); // Initial spawn
        
        // Drag and Drop Logic
        function drag(ev, issueId) {{
            ev.dataTransfer.setData("issueId", issueId);
            ev.target.style.opacity = "0.5";
        }}

        function allowDrop(ev) {{
            ev.preventDefault();
        }}
        
        function dragEnter(ev) {{
            ev.preventDefault();
            ev.currentTarget.style.background = "rgba(255, 255, 255, 0.2)";
            ev.currentTarget.style.borderColor = "#fff";
        }}
        
        function dragLeave(ev) {{
            ev.currentTarget.style.background = "";
            ev.currentTarget.style.borderColor = "";
        }}

        function drop(ev, targetFile) {{
            ev.preventDefault();
            ev.currentTarget.style.background = ""; // Reset style
            ev.currentTarget.style.borderColor = "";
            
            var issueId = ev.dataTransfer.getData("issueId");
            console.log("Dropped Issue #" + issueId + " on " + targetFile);
            
            // Send to backend
            fetch('/assign_issue', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{
                    issue_id: issueId,
                    target_file: targetFile
                }}),
            }})
            .then(response => {{
                if (response.ok) {{
                    console.log("Assignment successful");
                    // Reload page to reflect changes
                    window.location.reload();
                }} else {{
                    console.error("Assignment failed");
                }}
            }})
            .catch((error) => {{
                console.error('Error:', error);
            }});
        }}

        setInterval(() => {{
            fetch('/').then(r => {{
                if(r.ok) {{
                    document.getElementById('server-dot').classList.add('online');
                    document.getElementById('server-text').innerText = "Link Online";
                    document.getElementById('server-text').style.color = "var(--jeong-green)";
                }}
            }}).catch(() => {{
                document.getElementById('server-dot').classList.remove('online');
                document.getElementById('server-text').innerText = "Link Offline";
                document.getElementById('server-text').style.color = "#666";
            }});
        }}, 5000);
        
        // Initial check
        fetch('/').then(r => {{
            if(r.ok) {{
                document.getElementById('server-dot').classList.add('online');
                document.getElementById('server-text').innerText = "Link Online";
                document.getElementById('server-text').style.color = "var(--jeong-green)";
            }}
        }});
    </script>
</body>
</html>
    """

    with open(OUTPUT_FILE, 'w') as f:
        f.write(html_content)

    print(f"✅ Jeolla Left Navy Dashboard saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_dashboard()
