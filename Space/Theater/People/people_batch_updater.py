#!/usr/bin/env python3
"""
People Field Property Updater
Atom 폴더 기반으로 field property 추가 (기존 frontmatter 유지)
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime

# Atom → Field 매핑 (엄격)
ATOM_FIELDS = {
    '⚡️atom(BE⬇️⬆️)': ['🐢inv', '👾cog'],  # 이론가
    '👓atom(BE🔄)': ['🐢inv', '🐙ops'],      # 실무자
    '🗺️atom(PCO⬆️⬇️)': ['🐙ops', '🐢inv', '👾cog'],  # 측정/시뮬레이션
    '🧭atom(PCO🔃)': ['👾cog']  # 기본은 cog만, 아래 school로 cba 추가
}

# 🐅cba 엄격 조건: 특정 school 소속만
CBA_SCHOOLS = {
    'stan_school', 'biogeme_school', 'gurobi_school', 
    'webppl_gen_school', '💎biogeme_school', '🌀stan_school',
    '🧊gurobi_school', '🧬webppl_gen_school'
}

# 알려진 Bayes 전문가 (추가 확인된 경우만)
CBA_EXPERTS = {
    'andrew_gelman', 'vikash_mansinghka', 'patrick_jalliet',
    'bob_carpenter', 'aki_vehtari', 'ben_goodrich'
}

def get_atom_from_path(filepath):
    """경로에서 atom 추출"""
    parts = Path(filepath).parts
    for part in parts:
        if 'atom' in part:
            return part
    return None

def is_in_cba_school(filepath):
    """CBA school 소속 여부 확인"""
    path_str = str(filepath)
    return any(school in path_str for school in CBA_SCHOOLS)

def is_cba_expert(filename):
    """알려진 Bayes 전문가 여부"""
    name_lower = filename.lower().replace('.md', '')
    return any(expert in name_lower for expert in CBA_EXPERTS)

def infer_fields(filepath, filename):
    """파일 경로와 이름으로부터 field 추론"""
    fields = []
    
    # Atom 기반 field
    atom = get_atom_from_path(filepath)
    if atom in ATOM_FIELDS:
        fields.extend(ATOM_FIELDS[atom])
    
    # 🐅cba 엄격 조건 확인
    if atom == '🧭atom(PCO🔃)':
        if is_in_cba_school(filepath) or is_cba_expert(filename):
            if '🐅cba' not in fields:
                fields.append('🐅cba')
    
    return sorted(set(fields))

def parse_existing_frontmatter(content):
    """기존 frontmatter 파싱"""
    if not content.startswith('---'):
        return None, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    
    return parts[1], '---' + parts[2]

def get_file_creation_date(filepath):
    """파일 생성날짜 가져오기 (ISO 8601 형식)"""
    try:
        # macOS: st_birthtime, Linux: st_ctime
        stat = os.stat(filepath)
        if hasattr(stat, 'st_birthtime'):
            timestamp = stat.st_birthtime
        else:
            timestamp = stat.st_ctime
        
        dt = datetime.fromtimestamp(timestamp)
        return dt.strftime('%Y-%m-%d')
    except:
        return None

def merge_frontmatter(existing, fields, atom, created_date):
    """기존 frontmatter와 새 properties 병합"""
    import yaml
    
    if existing:
        try:
            data = yaml.safe_load(existing) or {}
        except:
            data = {}
    else:
        data = {}
    
    # collection 추가
    if 'collection' not in data:
        data['collection'] = ["[[People]]"]
    elif "[[People]]" not in data['collection']:
        data['collection'].append("[[People]]")
    
    # field 추가
    data['field'] = fields
    
    # atom 추가
    if atom:
        data['atom'] = atom
    
    # created 추가 (없는 경우만)
    if 'created' not in data and created_date:
        data['created'] = created_date
    
    # YAML 출력
    output = "---\n"
    output += yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False)
    output += "---\n\n"
    
    return output

def process_person(filepath):
    """개별 인물 파일 처리"""
    filename = os.path.basename(filepath)
    
    # .md 파일만 처리
    if not filename.endswith('.md'):
        return False
    
    # atom 설명 파일 제외
    if 'atom(' in filename and filename.endswith(')).md'):
        return False
    
    # 파일 읽기
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        print(f"⚠️  Could not read {filename}")
        return False
    
    # 기존 frontmatter 파싱
    existing_fm, remaining_content = parse_existing_frontmatter(content)
    
    # Field 추론
    fields = infer_fields(filepath, filename)
    atom = get_atom_from_path(filepath)
    created_date = get_file_creation_date(filepath)
    
    if not fields:
        print(f"⚠️  No fields for {filename}")
        return False
    
    # Frontmatter 병합
    try:
        new_frontmatter = merge_frontmatter(existing_fm, fields, atom, created_date)
    except Exception as e:
        print(f"❌ Error merging frontmatter for {filename}: {e}")
        return False
    
    # 새 내용 작성
    new_content = new_frontmatter + remaining_content.lstrip()
    
    # 파일 쓰기
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    except:
        print(f"❌ Could not write {filename}")
        return False
    
    cba_marker = " [🐅CBA]" if '🐅cba' in fields else ""
    print(f"✅ {filename}{cba_marker}")
    print(f"   Fields: {', '.join(fields)}")
    print(f"   Created: {created_date or 'N/A'}")
    
    return True

def process_atom_folder(atom_path):
    """Atom 폴더 내 모든 인물 파일 처리"""
    processed = 0
    skipped = 0
    
    for root, dirs, files in os.walk(atom_path):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                if process_person(filepath):
                    processed += 1
                else:
                    skipped += 1
    
    return processed, skipped

def main():
    """메인 함수"""
    people_dir = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Space/Dots/People"
    
    if not os.path.exists(people_dir):
        print(f"❌ Directory not found: {people_dir}")
        return
    
    print(f"📂 Processing people in: {people_dir}\n")
    print("🐅 CBA 엄격 기준 적용: school 소속 or 확인된 전문가만\n")
    
    total_processed = 0
    total_skipped = 0
    
    # 각 atom 폴더 처리
    atoms = ['⚡️atom(BE⬇️⬆️)', '👓atom(BE🔄)', '🗺️atom(PCO⬆️⬇️)', '🧭atom(PCO🔃)']
    
    for atom in atoms:
        atom_path = os.path.join(people_dir, atom)
        if os.path.exists(atom_path):
            print(f"\n{'='*50}")
            print(f"Processing {atom}")
            print(f"{'='*50}\n")
            
            processed, skipped = process_atom_folder(atom_path)
            total_processed += processed
            total_skipped += skipped
    
    print(f"\n{'='*50}")
    print(f"✅ Total processed: {total_processed}")
    print(f"⏭️  Total skipped: {total_skipped}")
    print(f"🐅 CBA assignments: Check output for [🐅CBA] marker")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()