#!/usr/bin/env python3
import os

PAPERS_DIR = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Space/Sources/Papers"

def clean_filename(name):
    """📜🐅_ → 📜"""
    if not name.startswith('📜'):
        return name
    
    # 이모지 제거
    cleaned = name.replace('📜🐅_', '📜').replace('📜🐙_', '📜').replace('📜🐢_', '📜').replace('📜👾_', '📜')
    return cleaned

def main():
    renamed = 0
    for old in os.listdir(PAPERS_DIR):
        if not old.startswith('📜') or not old.endswith('.md'):
            continue
        
        new = clean_filename(old)
        if new != old:
            old_path = os.path.join(PAPERS_DIR, old)
            new_path = os.path.join(PAPERS_DIR, new)
            
            if os.path.exists(new_path):
                print(f"⚠️  Exists: {new}")
                continue
            
            os.rename(old_path, new_path)
            print(f"✅ {old} → {new}")
            renamed += 1
    
    print(f"\n✅ Renamed: {renamed}")

if __name__ == "__main__":
    main()
