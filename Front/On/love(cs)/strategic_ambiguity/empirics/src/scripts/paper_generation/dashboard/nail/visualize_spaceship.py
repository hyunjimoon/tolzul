import http.server
import socketserver
import webbrowser
import os
import sys
import json
import re
from pathlib import Path

# Configuration
PORT = 8000
PARENT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PARENT_DIR / "output"
DASHBOARD_FILE = Path(__file__).parent / "battle_dashboard.html"

# --- Data Loading Functions (Mocked or Real) ---
def load_issue_queue():
    try:
        with open(PARENT_DIR / "issue_queue.json", "r") as f:
            return json.load(f)
    except:
        return []

def load_stamps():
    try:
        with open(PARENT_DIR / "journal/fleet_stamps.json", "r") as f:
            return json.load(f)
    except:
        return []

# --- HTML Generators ---

def generate_agent_card(agent, position_class):
    """Generates a Cyberpunk Agent Card HTML."""
    return f'''
    <div class="agent-card {position_class}" onclick="{agent['onclick']}">
        <div class="card-header">
            <span class="agent-icon">{agent['icon']}</span>
            <span class="agent-id">{agent['name']}</span>
        </div>
        <div class="card-body">
            <div class="agent-role">{agent['role']}</div>
            <div class="agent-status">
                <span class="status-dot online"></span> ONLINE
            </div>
        </div>
        <div class="card-footer">
            <div class="scan-line"></div>
        </div>
    </div>
    '''

def generate_group_section(title, agents, position_class, color_var):
    """Generates a Group Section (e.g., K-Group) with multiple cards."""
    cards_html = "".join([generate_agent_card(a, "") for a in agents])
    return f'''
    <div class="group-section {position_class}" style="--group-color: var({color_var});">
        <div class="group-title">{title}</div>
        <div class="group-cards">
            {cards_html}
        </div>
    </div>
    '''

def generate_center_hub(papers):
    """Generates the Central Command Hub (3-Screen Workflow)."""
    return f'''
    <div class="center-hub">
        <div class="hub-ring"></div>
        <div class="hub-core">
            <div class="hub-title">COMMANDER</div>
            <div class="hub-agent" onclick="openAgentWorkspace('7M')">
                <span class="hub-icon">🌙</span> 7M
            </div>
        </div>
        
        <!-- 3-Screen Visualization -->
        <div class="screen-array">
            <div class="screen screen-top" onclick="showMonitorInfo('CENTER')">
                <div class="screen-label">OPS THEATER</div>
                <div class="screen-content">J-G COLLAB</div>
            </div>
            <div class="screen-row">
                <div class="screen screen-left" onclick="showMonitorInfo('LEFT')">
                    <div class="screen-label">ORIGIN</div>
                    <div class="screen-content">O-BASE</div>
                </div>
                <div class="screen screen-bottom" onclick="showMonitorInfo('BOTTOM')">
                    <div class="screen-label">CMD</div>
                    <div class="screen-content">M-DECK</div>
                </div>
            </div>
        </div>
        
        <!-- Completion Index (Integrated) -->
        <div class="completion-ring">
            {generate_mini_progress(papers['U'])}
            {generate_mini_progress(papers['C'])}
            {generate_mini_progress(papers['N'])}
        </div>
    </div>
    '''

def generate_mini_progress(paper):
    """Generates a mini progress arc/bar for the center hub."""
    return f'''
    <div class="mini-progress" title="{paper['name']}">
        <span class="mp-icon">{paper['icon']}</span>
        <div class="mp-bar-container">
            <div class="mp-bar" style="width: {paper['current_rp']*10}%; background: {paper['state']};"></div>
        </div>
    </div>
    '''

def generate_dashboard():
    print("🚀 Launching MFS Control Tower v3.0 (Overhaul)...")
    
    # Load Data
    issue_data = load_issue_queue()
    stamps_data = load_stamps()
    
    # Agent Definitions
    jeong_agents = [
        {"id": "j1", "name": "8JID", "role": "Intro Draft", "icon": "🐢", "onclick": "openAgentWorkspace('8JID')"},
        {"id": "j2", "name": "9JT", "role": "Theory Draft", "icon": "🐢", "onclick": "openAgentWorkspace('9JT')"},
        {"id": "j3", "name": "10JE", "role": "Empirics Draft", "icon": "🐢", "onclick": "openAgentWorkspace('10JE')"}
    ]
    na_agents = [
        {"id": "n1", "name": "6GID", "role": "Structure", "icon": "🐅", "onclick": "openAgentWorkspace('6GID')"},
        {"id": "n2", "name": "5GT", "role": "Logic Flow", "icon": "🏗️", "onclick": "openAgentWorkspace('5GT')"},
        {"id": "n3", "name": "4GE", "role": "Code Arch", "icon": "💻", "onclick": "openAgentWorkspace('4GE')"}
    ]
    o_agents = [
        {"id": "o1", "name": "11OU", "role": "Mgmt Sci DB", "icon": "💾", "onclick": "openAgentWorkspace('11OU')"},
        {"id": "o2", "name": "12OC", "role": "Strategy DB", "icon": "📚", "onclick": "openAgentWorkspace('12OC')"},
        {"id": "o3", "name": "13ON", "role": "Ops Mgmt DB", "icon": "📜", "onclick": "openAgentWorkspace('13ON')"}
    ]
    kim_agents = [
        {"id": "k1", "name": "1KU", "role": "Audit U-Shape", "icon": "🛡️", "onclick": "openAgentWorkspace('1KU')"},
        {"id": "k2", "name": "2KC", "role": "Audit Commit", "icon": "⚖️", "onclick": "openAgentWorkspace('2KC')"},
        {"id": "k3", "name": "3KN", "role": "Audit News", "icon": "💪", "onclick": "openAgentWorkspace('3KN')"}
    ]
    
    # Paper Data (Mock for V3)
    papers = {
        "U": {"name": "U-Shape", "icon": "✌️", "state": "#00ff9d", "current_rp": 7},
        "C": {"name": "Commitment", "icon": "🦾", "state": "#ffcc00", "current_rp": 5},
        "N": {"name": "Newsvendor", "icon": "🤹", "state": "#ff0099", "current_rp": 2}
    }

    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>MFS CONTROL TOWER v3.0</title>
        <style>
            :root {{
                --bg-color: #050505;
                --grid-color: rgba(255, 255, 255, 0.03);
                --neon-green: #00ff9d;
                --neon-orange: #ffcc00;
                --neon-pink: #ff0099;
                --neon-blue: #00ccff;
                --card-bg: rgba(20, 20, 30, 0.8);
                --border-color: rgba(255, 255, 255, 0.1);
            }}
            
            body {{
                background-color: var(--bg-color);
                color: #fff;
                font-family: 'Segoe UI', 'Roboto', sans-serif;
                margin: 0;
                height: 100vh;
                overflow: hidden;
                background-image: 
                    linear-gradient(var(--grid-color) 1px, transparent 1px),
                    linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
                background-size: 40px 40px;
                display: flex;
                flex-direction: column;
            }}
            
            /* Header */
            .header {{
                height: 50px;
                background: rgba(0,0,0,0.8);
                border-bottom: 1px solid var(--border-color);
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 20px;
                z-index: 100;
            }}
            .brand {{ font-size: 1.2rem; font-weight: 900; letter-spacing: 2px; }}
            .brand span {{ color: var(--neon-green); }}
            
            /* Main Battlefield */
            .battlefield {{
                flex: 1;
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            
            /* Connecting Lines (SVG Background) */
            .connections-svg {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: 0;
            }}
            
            /* Group Sections */
            .group-section {{
                position: absolute;
                display: flex;
                flex-direction: column;
                gap: 10px;
                padding: 15px;
                background: rgba(0,0,0,0.3);
                border: 1px solid var(--border-color);
                border-radius: 10px;
                backdrop-filter: blur(5px);
                transition: transform 0.3s;
                z-index: 10;
            }}
            .group-section:hover {{ transform: scale(1.02); border-color: var(--group-color); box-shadow: 0 0 20px rgba(0,0,0,0.5); }}
            
            .group-top {{ top: 20px; left: 50%; transform: translateX(-50%); border-top: 3px solid var(--group-color); }}
            .group-right {{ top: 50%; right: 20px; transform: translateY(-50%); border-right: 3px solid var(--group-color); }}
            .group-bottom {{ bottom: 20px; left: 50%; transform: translateX(-50%); border-bottom: 3px solid var(--group-color); }}
            .group-left {{ top: 50%; left: 20px; transform: translateY(-50%); border-left: 3px solid var(--group-color); }}
            
            .group-title {{
                font-size: 1.5rem;
                font-weight: 900;
                color: var(--group-color);
                text-transform: uppercase;
                letter-spacing: 2px;
                text-align: center;
                margin-bottom: 10px;
                text-shadow: 0 0 10px var(--group-color);
            }}
            
            .group-cards {{ display: flex; gap: 15px; }}
            
            /* Agent Cards */
            .agent-card {{
                width: 140px;
                height: 100px;
                background: var(--card-bg);
                border: 1px solid var(--border-color);
                border-radius: 6px;
                padding: 10px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                cursor: pointer;
                transition: all 0.2s;
                position: relative;
                overflow: hidden;
            }}
            .agent-card:hover {{ background: rgba(255,255,255,0.1); border-color: #fff; }}
            
            .card-header {{ display: flex; align-items: center; gap: 8px; }}
            .agent-icon {{ font-size: 1.8rem; }}
            .agent-id {{ font-size: 1.4rem; font-weight: 900; color: #fff; text-shadow: 0 0 5px rgba(255,255,255,0.5); }}
            
            .agent-role {{ font-size: 0.75rem; color: #aaa; font-weight: 600; text-transform: uppercase; }}
            
            .agent-status {{ font-size: 0.6rem; color: var(--neon-green); display: flex; align-items: center; gap: 4px; font-weight: bold; }}
            .status-dot {{ width: 6px; height: 6px; background: var(--neon-green); border-radius: 50%; box-shadow: 0 0 4px var(--neon-green); }}
            
            .scan-line {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 2px;
                background: rgba(255,255,255,0.1);
                animation: scan 2s linear infinite;
            }}
            @keyframes scan {{ 0% {{ top: 0; }} 100% {{ top: 100%; }} }}
            
            /* Center Hub */
            .center-hub {{
                width: 300px;
                height: 300px;
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 20;
            }}
            .hub-ring {{
                position: absolute;
                width: 100%;
                height: 100%;
                border: 2px dashed var(--border-color);
                border-radius: 50%;
                animation: rotate 60s linear infinite;
            }}
            @keyframes rotate {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
            
            .hub-core {{
                width: 120px;
                height: 120px;
                background: rgba(0,0,0,0.8);
                border: 2px solid var(--neon-orange);
                border-radius: 50%;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                box-shadow: 0 0 30px rgba(255, 204, 0, 0.2);
                z-index: 30;
            }}
            .hub-title {{ font-size: 0.7rem; color: var(--neon-orange); letter-spacing: 1px; margin-bottom: 5px; }}
            .hub-agent {{ font-size: 1.5rem; font-weight: 900; color: #fff; cursor: pointer; }}
            .hub-agent:hover {{ transform: scale(1.1); text-shadow: 0 0 10px #fff; }}
            
            /* Screen Array */
            .screen-array {{
                position: absolute;
                width: 200px;
                height: 200px;
                pointer-events: none; /* Let clicks pass through to hub core if needed, but screens need pointer-events auto */
            }}
            .screen {{
                position: absolute;
                background: rgba(0, 255, 157, 0.1);
                border: 1px solid var(--neon-green);
                border-radius: 4px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                pointer-events: auto;
                cursor: pointer;
                transition: all 0.2s;
            }}
            .screen:hover {{ background: rgba(0, 255, 157, 0.3); box-shadow: 0 0 10px var(--neon-green); }}
            
            .screen-top {{ top: -60px; left: 50%; transform: translateX(-50%); width: 100px; height: 40px; }}
            .screen-left {{ top: 50%; left: -80px; transform: translateY(-50%); width: 40px; height: 80px; }}
            .screen-bottom {{ bottom: -60px; left: 50%; transform: translateX(-50%); width: 80px; height: 30px; }}
            
            .screen-label {{ font-size: 0.5rem; color: var(--neon-green); font-weight: bold; }}
            .screen-content {{ font-size: 0.6rem; color: #fff; }}
            
            /* Completion Ring */
            .completion-ring {{
                position: absolute;
                bottom: -40px;
                display: flex;
                gap: 10px;
            }}
            .mini-progress {{ display: flex; align-items: center; gap: 5px; }}
            .mp-icon {{ font-size: 1rem; }}
            .mp-bar-container {{ width: 40px; height: 4px; background: #333; border-radius: 2px; }}
            .mp-bar {{ height: 100%; border-radius: 2px; }}
            
            /* Bottom Panels */
            .bottom-panel {{
                position: absolute;
                bottom: 20px;
                display: flex;
                gap: 20px;
                width: 100%;
                justify-content: space-between;
                padding: 0 40px;
                box-sizing: border-box;
                pointer-events: none;
            }}
```
            .panel-box {{
                background: rgba(0,0,0,0.8);
                border: 1px solid var(--border-color);
                border-radius: 8px;
                padding: 10px;
                pointer-events: auto;
                max-width: 300px;
            }}
            
        </style>
        <script>
        <script>
            function openAgentWorkspace(agentId) {{
                // Map Agent IDs to specific file paths in the vault
                // Vault Root: tolzul
                // Relative Path from Vault Root: Space/Lab/choose(organization)/...
                
                const agentFiles = {{
                    // K-Group (Evaluation)
                    "1KU": "Space/Lab/choose(organization)/4_K_義/01_KU🔴.md",
                    "2KC": "Space/Lab/choose(organization)/4_K_義/02_KC🔴.md",
                    "3KN": "Space/Lab/choose(organization)/4_K_義/03_KN🔴.md",
                    
                    // G-Group (Structure)
                    "4GE": "Space/Lab/choose(organization)/2_G_思/04_GE🟠.md",
                    "5GT": "Space/Lab/choose(organization)/2_G_思/05_GT🟠.md",
                    "6GID": "Space/Lab/choose(organization)/2_G_思/06_GID🟠.md",
                    
                    // M-Group (Commander)
                    "7M": "Space/Lab/choose(organization)/0_M_統/README.md",
                    
                    // J-Group (Execution)
                    "8JID": "Space/Lab/choose(organization)/3_J_利/08_JID🟢.md",
                    "9JT": "Space/Lab/choose(organization)/3_J_利/09_JT🟢.md",
                    "10JE": "Space/Lab/choose(organization)/3_J_利/10_JE🟢.md",
                    
                    // O-Group (Origin)
                    "11OU": "Space/Lab/choose(organization)/1_O_見/11_OU🔵.md",
                    "12OC": "Space/Lab/choose(organization)/1_O_見/12_OC🔵.md",
                    "13ON": "Space/Lab/choose(organization)/1_O_見/13_ON🔵.md"
                }};
                
                const filePath = agentFiles[agentId];
                
                if (filePath) {{
                    const encodedPath = encodeURIComponent(filePath);
                    const url = `obsidian://open?vault=tolzul&file=${{encodedPath}}`;
                    console.log(`Opening workspace for ${{agentId}}: ${{url}}`);
                    window.location.href = url;
                }} else {{
                    alert(`Agent workspace for ${{agentId}} not found.`);
                }}
            }}
            
            function showMonitorInfo(screen) {{
                let msg = "";
                if (screen === 'LEFT') msg = "LEFT VERTICAL: O-BASE (Data Ingestion)";
                if (screen === 'CENTER') msg = "CENTER MAIN: OPS THEATER (Execution)";
                if (screen === 'BOTTOM') msg = "BOTTOM SMALL: COMMAND DECK (Strategy)";
                alert(msg);
            }}
        </script>
    </head>
    <body>
        <div class="header">
            <div class="brand">MFS <span>CONTROL TOWER</span> v3.0</div>
            <div style="font-size: 0.8rem; color: #888;">SYSTEM: ONLINE</div>
        </div>
        
        <div class="battlefield">
            <!-- SVG Connections -->
            <svg class="connections-svg">
                <defs>
                    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:rgba(255,255,255,0.1);stop-opacity:1" />
                        <stop offset="100%" style="stop-color:rgba(255,255,255,0);stop-opacity:1" />
                    </linearGradient>
                </defs>
                <!-- Lines connecting groups to center (Approximate coordinates) -->
                <line x1="50%" y1="15%" x2="50%" y2="40%" stroke="var(--border-color)" stroke-width="1" stroke-dasharray="5,5" />
                <line x1="85%" y1="50%" x2="60%" y2="50%" stroke="var(--border-color)" stroke-width="1" stroke-dasharray="5,5" />
                <line x1="50%" y1="85%" x2="50%" y2="60%" stroke="var(--border-color)" stroke-width="1" stroke-dasharray="5,5" />
                <line x1="15%" y1="50%" x2="40%" y2="50%" stroke="var(--border-color)" stroke-width="1" stroke-dasharray="5,5" />
            </svg>
            
            <!-- Groups -->
            {generate_group_section("EVALUATION (K)", kim_agents, "group-top", "--neon-pink")}
            {generate_group_section("STRUCTURE (G)", na_agents, "group-right", "--neon-orange")}
            {generate_group_section("EXECUTION (J)", jeong_agents, "group-bottom", "--neon-green")}
            {generate_group_section("ORIGIN (O)", o_agents, "group-left", "--neon-blue")}
            
            <!-- Center Hub -->
            {generate_center_hub(papers)}
            
        </div>
        
        <div class="bottom-panel">
            <div class="panel-box">
                <div style="font-weight: bold; color: var(--neon-orange); margin-bottom: 5px;">🎖️ STAMP COLLECTION</div>
                <div style="font-size: 0.8rem; color: #aaa;">{len(stamps_data)} Stamps Collected</div>
            </div>
            <div class="panel-box">
                <div style="font-weight: bold; color: var(--neon-green); margin-bottom: 5px;">📡 FLEET COMMS</div>
                <div style="font-size: 0.7rem; color: #fff;">> 11OU: Scanning...</div>
                <div style="font-size: 0.7rem; color: #fff;">> 12OC: Strategy aligned.</div>
            </div>
        </div>
        
    </body>
    </html>
    '''
    
    with open(DASHBOARD_FILE, "w") as f:
        f.write(html)
    
    print(f"✅ MFS v3.0 Dashboard saved to {DASHBOARD_FILE}")

if __name__ == "__main__":
    generate_dashboard()
    
    # Simple Server
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = '/battle_dashboard.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🌍 Serving at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
