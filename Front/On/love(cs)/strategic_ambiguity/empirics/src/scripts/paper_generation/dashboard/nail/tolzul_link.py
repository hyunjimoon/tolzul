#!/usr/bin/env python3
import http.server
import socketserver
import urllib.parse
import subprocess
import os
import json
from pathlib import Path

PORT = 8000
DASHBOARD_FILE = Path(__file__).parent / "battle_dashboard.html"

class TolzulHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        
        if parsed_path.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            if DASHBOARD_FILE.exists():
                with open(DASHBOARD_FILE, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b"Dashboard not found. Run visualize_spaceship.py first.")
            return

        elif parsed_path.path == "/open":
            file_path = query.get("file", [None])[0]
            if file_path:
                print(f"📂 Opening: {file_path}")
                subprocess.run(["open", file_path])
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Opened")
            else:
                self.send_error(400, "Missing file parameter")
            return
            
        elif parsed_path.path == "/code":
            file_path = query.get("file", [None])[0]
            if file_path:
                print(f"💻 VS Code: {file_path}")
                subprocess.run(["code", file_path])
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Opened in Code")
            else:
                self.send_error(400, "Missing file parameter")
            return

        else:
            # Serve static files if needed, or 404
            super().do_GET()

    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        if parsed_path.path == "/assign_issue":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                issue_id = data.get("issue_id")
                target_file = data.get("target_file")
                
                print(f"🔄 Assigning Issue #{issue_id} to {target_file}")
                
                # Update JSON
                # issue_queue.json is in the parent directory (paper_generation)
                issue_file = Path(__file__).parent.parent / "issue_queue.json"
                if issue_file.exists():
                    with open(issue_file, 'r') as f:
                        jdata = json.load(f)
                    
                    updated = False
                    for issue in jdata.get("issues", []):
                        if issue["id"] == issue_id:
                            issue["target"] = target_file
                            # Update target code (e.g. chap1_U_intro -> U-I)
                            # Simple heuristic for code
                            parts = target_file.split('_')
                            if len(parts) >= 3:
                                code_map = {"introduction.md": "I", "theory.md": "T", "empirics.md": "E", "discussion.md": "D"}
                                suffix = parts[-1]
                                letter = code_map.get(suffix, "?")
                                issue["target_code"] = f"{parts[1]}-{letter}"
                            updated = True
                            break
                    
                    if updated:
                        with open(issue_file, 'w') as f:
                            json.dump(jdata, f, indent=2)
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(b"Updated")
                    else:
                        self.send_error(404, "Issue not found")
                else:
                    self.send_error(500, "Issue file not found")
                    
            except Exception as e:
                print(f"Error: {e}")
                self.send_error(500, str(e))
            return
        
        elif parsed_path.path == "/update_issue":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                issue_id = data.get("issue_id")
                action = data.get("action") # "advance" or "close"
                
                print(f"🔄 Updating Issue #{issue_id}: {action}")
                
                # Update JSON
                issue_file = Path(__file__).parent.parent / "issue_queue.json"
                if issue_file.exists():
                    with open(issue_file, 'r') as f:
                        jdata = json.load(f)
                    
                    updated = False
                    for issue in jdata.get("issues", []):
                        if issue["id"] == issue_id:
                            current_stage = issue["stage"]
                            new_stage = current_stage
                            
                            STAGES = ["FLAG", "REVIEW", "BUILD", "MERGE", "CLOSED"]
                            
                            if action == "advance":
                                try:
                                    idx = STAGES.index(current_stage)
                                    if idx < len(STAGES) - 1:
                                        new_stage = STAGES[idx + 1]
                                except ValueError:
                                    pass
                            elif action == "close":
                                new_stage = "CLOSED"
                                
                            if new_stage != current_stage:
                                issue["stage"] = new_stage
                                issue["updated_at"] = "2025-12-01T12:00:00Z" # Mock timestamp for now
                                updated = True
                            break
                    
                    if updated:
                        with open(issue_file, 'w') as f:
                            json.dump(jdata, f, indent=2)
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(b"Updated")
                    else:
                        self.send_error(404, "Issue not found or no change")
                else:
                    self.send_error(500, "Issue file not found")
                    
            except Exception as e:
                print(f"Error: {e}")
                self.send_error(500, str(e))
            return
        
        elif parsed_path.path == "/launch":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                app_name = data.get("app")
                
                if app_name:
                    print(f"🚀 Launching App: {app_name}")
                    # Use 'open -a' on Mac
                    subprocess.Popen(["open", "-a", app_name])
                    
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"Launched")
                else:
                    self.send_error(400, "Missing app name")
            except Exception as e:
                print(f"Error launching app: {e}")
                self.send_error(500, str(e))
            return
        
        self.send_error(404, "Not Found")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), TolzulHandler) as httpd:
        print(f"⚓️ Jeolla Left Navy Command Link Active at http://localhost:{PORT}")
        print(f"   - Dashboard: http://localhost:{PORT}/")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Link Severed.")
