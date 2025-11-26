#!/usr/bin/env python3
"""
Life Spaceship Visualizer
=========================

Generates an interactive HTML dashboard for your Life Spaceship.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
import sys

# --- Configuration ---
BASE_DIR = Path("/Users/hyunjimoon/tolzul")
DATA_FILE = BASE_DIR / "spaceship_data.csv"
OUTPUT_FILE = BASE_DIR / "spaceship_dashboard.html"

def generate_dashboard():
    if not DATA_FILE.exists():
        print(f"Error: Data file {DATA_FILE} not found.")
        print("Please run 'operate_spaceship.py' first.")
        sys.exit(1)

    print(f"📂 Loading data from {DATA_FILE}...")
    df = pd.read_csv(DATA_FILE)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    # Create content snippet for hover
    df['snippet'] = df['content'].fillna('').str.slice(0, 200) + "..."
    df['snippet'] = df['snippet'].apply(lambda x: x.replace('\n', '<br>'))

    print("🎨 Generating interactive dashboard...")

    # Create figure with secondary y-axis
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=False,
        vertical_spacing=0.1,
        subplot_titles=("Daily Vagueness Rhythm (Space vs Front)", "Monthly Distribution", "Yearly Trend"),
        specs=[[{"secondary_y": True}], [{"secondary_y": False}], [{"secondary_y": False}]]
    )

    # --- 1. Daily Rhythm (Scatter + Trend) ---
    # Scatter points
    fig.add_trace(
        go.Scatter(
            x=df['date'], 
            y=df['V_raw'],
            mode='markers',
            name='Daily Note',
            marker=dict(
                size=10,
                color=df['V_raw'],
                colorscale='RdBu_r', # Red (Low V/Front) to Blue (High V/Space)
                showscale=True,
                colorbar=dict(title="Vagueness", len=0.3, y=0.85)
            ),
            text=df['snippet'],
            hovertemplate="<b>%{x}</b><br>V: %{y:.1f}<br><br>%{text}<extra></extra>"
        ),
        row=1, col=1
    )

    # Trend Line (Rolling Mean)
    df['V_rolling'] = df['V_raw'].rolling(window=7, center=True).mean()
    fig.add_trace(
        go.Scatter(
            x=df['date'],
            y=df['V_rolling'],
            mode='lines',
            name='7-Day Trend',
            line=dict(color='rgba(100, 100, 100, 0.5)', width=3, dash='dot')
        ),
        row=1, col=1
    )
    
    # Zones
    fig.add_hrect(y0=60, y1=100, fillcolor="blue", opacity=0.05, layer="below", line_width=0, row=1, col=1, annotation_text="Space (Ear)", annotation_position="top left")
    fig.add_hrect(y0=0, y1=40, fillcolor="red", opacity=0.05, layer="below", line_width=0, row=1, col=1, annotation_text="Front (Eye)", annotation_position="bottom left")

    # --- 2. Monthly Distribution (Box Plot) ---
    df['month'] = df['date'].dt.to_period('M').astype(str)
    
    fig.add_trace(
        go.Box(
            x=df['month'],
            y=df['V_raw'],
            name='Monthly Dist',
            marker_color='gray',
            boxpoints='all',
            jitter=0.3,
            pointpos=-1.8
        ),
        row=2, col=1
    )

    # --- 3. Yearly Trend (Bar) ---
    df['year'] = df['date'].dt.year
    yearly = df.groupby('year')['V_raw'].mean().reset_index()
    
    fig.add_trace(
        go.Bar(
            x=yearly['year'],
            y=yearly['V_raw'],
            name='Yearly Avg',
            marker_color='teal'
        ),
        row=3, col=1
    )

    # Layout updates
    fig.update_layout(
        title_text="<b>Life Spaceship Dashboard</b>: Strategic Ambiguity Operation",
        height=1200,
        showlegend=False,
        template="plotly_dark", # Dark theme for Space Mode
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Courier New, monospace", color="#00ffcc") # Neon font
    )
    
    fig.update_yaxes(title_text="Vagueness (0-100)", range=[0, 100], row=1, col=1, gridcolor='#333')
    fig.update_yaxes(title_text="Vagueness Distribution", range=[0, 100], row=2, col=1, gridcolor='#333')
    fig.update_yaxes(title_text="Average Vagueness", range=[0, 100], row=3, col=1, gridcolor='#333')
    fig.update_xaxes(gridcolor='#333')

    # Save to HTML string first to inject custom CSS/JS
    html_content = fig.to_html(include_plotlyjs='cdn', full_html=True)
    
    # Custom CSS for Space Mode
    custom_style = """
    <style>
        body {
            background-color: #050510;
            background-image: 
                radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 3px),
                radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 2px),
                radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 3px);
            background-size: 550px 550px, 350px 350px, 250px 250px;
            background-position: 0 0, 40px 60px, 130px 270px;
            color: #00ffcc;
            font-family: 'Courier New', monospace;
        }
        .main-svg {
            background: transparent !important;
        }
        h1, h2, h3 {
            text-shadow: 0 0 10px #00ffcc;
        }
        .music-player {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
            opacity: 0.7;
            transition: opacity 0.3s;
        }
        .music-player:hover {
            opacity: 1;
        }
    </style>
    """
    
    # Audio Player (Interstellar OST - Cornfield Chase)
    # Using a different video ID that is more likely to allow embedding
    # "Interstellar Main Theme - Extra Extended - Soundtrack by Hans Zimmer"
    audio_player = """
    <div class="music-player">
        <iframe width="300" height="80" src="https://www.youtube.com/embed/UDVtMYqUAyw?autoplay=1&loop=1&playlist=UDVtMYqUAyw" 
        title="Interstellar Theme" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    """
    
    # Inject into HTML
    final_html = html_content.replace('</body>', f'{custom_style}{audio_player}</body>')
    
    with open(OUTPUT_FILE, 'w') as f:
        f.write(final_html)

    print(f"✅ Vivid Dashboard saved to {OUTPUT_FILE}")
    print(f"   Open this file in your browser to interact.")

if __name__ == "__main__":
    generate_dashboard()
