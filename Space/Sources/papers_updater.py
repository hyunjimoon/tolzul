#!/usr/bin/env python3
import os, re, yaml
from datetime import datetime
from pathlib import Path

PAPERS_DIR = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Space/Sources/Papers"
PEOPLE_DIR = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Space/Dots/People"

# 저자명 → 파일명 매핑 (canonical IDs)
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
    'kim': 'yongwook_kim'
}

def load_people_fields():
    """People 폴더에서 author_id → fields 매핑"""
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
                            author_id = f.replace('.md', '')
                            mapping[author_id] = data['field']
            except:
                pass
    return mapping

def extract_info(filename):
    """파일명에서 정보 추출"""
    name = filename.replace('📜', '').replace('.md', '')
    
    # Year
    year_match = re.search(r'\d{2,4}', name)
    year = year_match.group() if year_match else None
    if year and len(year) == 2:
        year = '20' + year
    
    # Authors (대문자 시작 단어들)
    author_part = name.split(year)[0] if year else name.split('_')[0]
    authors = [a.lower() for a in re.findall(r'[A-Z][a-z]+', author_part)]
    
    # Canonical author IDs
    author_ids = [AUTHOR_MAP.get(a, a) for a in authors]
    
    # Field hints from filename
    field_hints = set()
    if '🐅_' in filename or any(x in name.lower() for x in ['bayesian', 'model']):
        field_hints.add('🐅cba')
    if '🐙_' in filename or any(x in name.lower() for x in ['optim', 'inventory', 'platform']):
        field_hints.add('🐙ops')
    if '🐢_' in filename or any(x in name.lower() for x in ['innov', 'disrupt', 'strategy']):
        field_hints.add('🐢inv')
    if '👾_' in filename or any(x in name.lower() for x in ['cognit', 'decision', 'learn']):
        field_hints.add('👾cog')
    
    return author_ids, year, field_hints

def infer_fields(author_ids, field_hints, people_map):
    """저자 fields 병합"""
    fields = set(field_hints)
    for aid in author_ids:
        if aid in people_map:
            fields.update(people_map[aid])
    return sorted(fields) if fields else ['🐢inv']

def process_paper(filepath, people_map):
    """논문 파일 처리"""
    filename = os.path.basename(filepath)
    if not filename.startswith('📜') or not filename.endswith('.md'):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False
    
    # 이미 처리됨
    if content.startswith('---') and 'author_ids' in content:
        return False
    
    # 정보 추출
    author_ids, year, field_hints = extract_info(filename)
    fields = infer_fields(author_ids, field_hints, people_map)
    
    # Frontmatter
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
    
    # 기존 frontmatter 제거
    if content.startswith('---'):
        parts = content.split('---', 2)
        content = parts[2] if len(parts) > 2 else content
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fm + content.lstrip())
    
    print(f"✅ {filename}")
    print(f"   Authors: {', '.join(author_ids)}")
    print(f"   Fields: {', '.join(fields)}\n")
    return True

def main():
    people_map = load_people_fields()
    print(f"Loaded {len(people_map)} people\n")
    
    processed = 0
    for f in sorted(os.listdir(PAPERS_DIR)):
        if process_paper(os.path.join(PAPERS_DIR, f), people_map):
            processed += 1
    
    print(f"\n✅ Processed: {processed}")

if __name__ == "__main__":
    main()