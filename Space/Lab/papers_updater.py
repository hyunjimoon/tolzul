#!/usr/bin/env python3
import os, re, yaml
from datetime import datetime
from pathlib import Path

PAPERS_DIR = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Space/Sources/Papers"
PEOPLE_DIR = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Space/Dots/People"

AUTHOR_MAP = {
    'gelman': 'andrew_gelman',
    'felin': 'teppo_felin', 
    'kauffman': 'stuart_kauffman',
    'gans': 'joshua_gans',
    'stern': 'scott_stern',
    'tenenbaum': 'josh_tenenbaum',
    'goodman': 'noah_goodman',
    'andriani': 'pierpaolo_andriani',
    'camuffo': 'arnaldo_camuffo',
    'mcelreath': 'richard_mcelreath',
    'bolton': 'patrick_bolton',
    'arrow': 'kenneth_arrow',
    'sterman': 'john_sterman',
    'parker': 'geoffrey_parker',
    'kim': 'yongwook_kim',
    'corbett': 'andrew_corbett',
    'alvarez': 'sharon_alvarez',
    'yarkoni': 'tal_yarkoni'
}

def load_people_fields():
    mapping = {}
    for root, dirs, files in os.walk(PEOPLE_DIR):
        for f in files:
            if not f.endswith('.md') or 'atom(' in f:
                continue
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if content.startswith('---'):
                        fm = content.split('---')[1]
                        data = yaml.safe_load(fm) or {}
                        if 'field' in data:
                            mapping[f.replace('.md', '')] = data['field']
            except:
                pass
    return mapping

def extract_info(filename):
    name = filename.replace('📜', '').replace('.md', '')
    
    # 이모지 prefix 제거
    name = re.sub(r'^[👾🐙🐢🐅]_', '', name)
    
    # Year
    year_match = re.search(r'\d{2,4}', name)
    year = year_match.group() if year_match else None
    if year and len(year) == 2:
        year = '20' + year
    
    # Author part
    if year:
        author_part = name.split(year)[0].strip('_')
    else:
        author_part = name.split('_')[0]
    
    # Authors: 대문자 OR 소문자
    authors = []
    caps = re.findall(r'[A-Z][a-z]+', author_part)
    if caps:
        authors = [a.lower() for a in caps]
    else:
        lower = re.findall(r'^([a-z]+)', author_part)
        if lower:
            authors = [lower[0]]
    
    author_ids = [AUTHOR_MAP.get(a, a) for a in authors]
    
    # Field hints
    field_hints = set()
    orig = filename.lower()
    if '🐅_' in filename or any(x in orig for x in ['bayesian', 'model']):
        field_hints.add('🐅cba')
    if '🐙_' in filename or any(x in orig for x in ['optim', 'inventory']):
        field_hints.add('🐙ops')
    if '🐢_' in filename or any(x in orig for x in ['innov', 'disrupt', 'strategy']):
        field_hints.add('🐢inv')
    if '👾_' in filename or any(x in orig for x in ['cognit', 'decision', 'learn']):
        field_hints.add('👾cog')
    
    return author_ids, year, field_hints

def infer_fields(author_ids, field_hints, people_map):
    fields = set(field_hints)
    for aid in author_ids:
        if aid in people_map:
            fields.update(people_map[aid])
    return sorted(fields) if fields else ['🐢inv']

def process_paper(filepath, people_map):
    filename = os.path.basename(filepath)
    if not filename.startswith('📜') or not filename.endswith('.md'):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False
    
    # 기존 frontmatter 확인
    if content.startswith('---'):
        parts = content.split('---')
        if len(parts) >= 3:
            existing = yaml.safe_load(parts[1]) or {}
            if 'author_ids' in existing and existing.get('author_ids'):
                return False  # 이미 올바르게 처리됨
    
    author_ids, year, field_hints = extract_info(filename)
    
    if not author_ids:
        print(f"⚠️  No authors: {filename}")
        return False
    
    fields = infer_fields(author_ids, field_hints, people_map)
    
    stat = os.stat(filepath)
    created = datetime.fromtimestamp(
        stat.st_birthtime if hasattr(stat, 'st_birthtime') else stat.st_ctime
    ).strftime('%Y-%m-%d')
    
    fm = f"""---
collection:
  - "[[Papers]]"
author_ids:
"""
    for aid in author_ids:
        fm += f"  - {aid}\n"
    
    fm += "field:\n"
    for f in fields:
        fm += f"  - {f}\n"
    
    if year:
        fm += f"year: {year}\n"
    fm += f"created: {created}\n---\n\n"
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        content = parts[2] if len(parts) > 2 else content
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fm + content.lstrip())
    
    print(f"✅ {filename}")
    print(f"   {', '.join(author_ids)} | {', '.join(fields)}")
    return True

def main():
    people_map = load_people_fields()
    print(f"Loaded {len(people_map)} people\n")
    
    processed = 0
    for f in sorted(os.listdir(PAPERS_DIR)):
        if process_paper(os.path.join(PAPERS_DIR, f), people_map):
            processed += 1
    
    print(f"\n✅ Fixed: {processed}")

if __name__ == "__main__":
    main()
