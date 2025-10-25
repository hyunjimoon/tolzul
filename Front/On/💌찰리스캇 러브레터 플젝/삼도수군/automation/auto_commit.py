#!/usr/bin/env python3
"""
🤖 전투일지 자동 커밋 시스템
- 전투일지.md 변경사항을 파싱하여 자동으로 Git 커밋
- 완료 항목을 분석하여 적절한 커밋 메시지 생성
"""

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

# 설정
REPO_ROOT = Path(__file__).parent.parent.parent.parent.parent.parent
LOG_PATH = Path(__file__).parent.parent / "전투일지.md"
BRANCH = "develop"  # 기본 브랜치


class BattleLogParser:
    """전투일지 파싱 클래스"""
    
    def __init__(self, log_path):
        self.log_path = log_path
        self.content = self._read_log()
        
    def _read_log(self):
        """전투일지 읽기"""
        with open(self.log_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def get_today_section(self):
        """오늘 날짜의 Day 섹션 찾기"""
        today = datetime.now()
        
        # 패턴: ## 🗓️ Day X - 2025.10.25 (금)
        patterns = [
            rf"## 🗓️ Day \d+ - {today.strftime('%Y.%m.%d')}",
            rf"## Day \d+ - {today.strftime('%Y.%m.%d')}",
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content)
            if match:
                start = match.start()
                # 다음 Day 섹션까지 추출
                next_day = re.search(r"## 🗓️ Day \d+|## Day \d+", 
                                    self.content[start+10:])
                end = start + next_day.start() + 10 if next_day else len(self.content)
                return self.content[start:end]
        
        return None
    
    def extract_completed_tasks(self, day_section):
        """완료된 작업 추출"""
        if not day_section:
            return []
        
        completed = []
        
        # "완료:" 섹션 찾기
        completed_match = re.search(r"\*\*완료\*\*:(.+?)(?=\*\*|###|##|\Z)", 
                                   day_section, re.DOTALL)
        
        if completed_match:
            completed_text = completed_match.group(1)
            # ✅로 시작하는 항목들 추출
            tasks = re.findall(r"- ✅ (.+)", completed_text)
            completed.extend(tasks)
        
        return completed
    
    def extract_key_outputs(self, day_section):
        """주요 산출물 추출 (작업 로그에서)"""
        if not day_section:
            return []
        
        outputs = []
        
        # "산출:" 패턴 찾기
        output_matches = re.findall(r"산출:\s*(.+?)(?=```|\n\n|작업:)", 
                                   day_section, re.DOTALL)
        
        for match in output_matches:
            lines = match.strip().split('\n')
            outputs.extend([line.strip('- ').strip() for line in lines if line.strip()])
        
        return outputs


class GitCommitter:
    """Git 커밋 자동화 클래스"""
    
    def __init__(self, repo_root):
        self.repo_root = repo_root
        
    def run_git(self, *args):
        """Git 명령어 실행"""
        cmd = ['git', '-C', str(self.repo_root)] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    
    def check_changes(self):
        """변경사항 확인"""
        stdout, _, _ = self.run_git('status', '--porcelain')
        return bool(stdout.strip())
    
    def get_current_branch(self):
        """현재 브랜치 확인"""
        stdout, _, _ = self.run_git('branch', '--show-current')
        return stdout.strip()
    
    def commit_battle_log(self, day_num, tasks):
        """전투일지 커밋"""
        today = datetime.now().strftime('%Y.%m.%d')
        
        # 커밋 메시지 생성
        if tasks:
            # 주요 작업 요약
            summary = self._generate_summary(tasks)
            message = f"docs: battle log Day {day_num} ({today})\n\n{summary}"
        else:
            message = f"docs: battle log Day {day_num} ({today})"
        
        # Git add
        log_relative = os.path.relpath(LOG_PATH, self.repo_root)
        self.run_git('add', log_relative)
        
        # Git commit
        stdout, stderr, code = self.run_git('commit', '-m', message)
        
        if code == 0:
            print(f"✅ Committed: {message.split(chr(10))[0]}")
            return True
        elif 'nothing to commit' in stdout or 'nothing to commit' in stderr:
            print("ℹ️  No changes to commit")
            return False
        else:
            print(f"❌ Commit failed: {stderr}")
            return False
    
    def commit_work_items(self, tasks, outputs):
        """작업 항목들을 개별 커밋으로"""
        committed = []
        
        for task in tasks[:3]:  # 최대 3개만 (너무 많으면 스팸)
            commit_type, message = self._parse_task_to_commit(task)
            
            if commit_type:
                # 변경사항이 있으면 커밋
                if self.check_changes():
                    stdout, stderr, code = self.run_git(
                        'commit', '--allow-empty', '-m', f"{commit_type}: {message}"
                    )
                    if code == 0:
                        committed.append(f"{commit_type}: {message}")
                        print(f"✅ Committed: {commit_type}: {message}")
        
        return committed
    
    def push(self, branch=None):
        """원격 저장소에 푸시"""
        target_branch = branch or self.get_current_branch()
        
        stdout, stderr, code = self.run_git('push', 'origin', target_branch)
        
        if code == 0:
            print(f"✅ Pushed to origin/{target_branch}")
            return True
        else:
            print(f"❌ Push failed: {stderr}")
            return False
    
    def _generate_summary(self, tasks):
        """작업 요약 생성"""
        summary_lines = []
        for i, task in enumerate(tasks[:5], 1):
            summary_lines.append(f"{i}. {task}")
        
        return "\n".join(summary_lines)
    
    def _parse_task_to_commit(self, task):
        """작업 항목을 커밋 타입과 메시지로 변환"""
        task_lower = task.lower()
        
        # 키워드 기반 분류
        if any(k in task_lower for k in ['script', 'code', '구현', 'pipeline']):
            return 'feat', task
        elif any(k in task_lower for k in ['수정', 'fix', '버그', 'debug']):
            return 'fix', task
        elif any(k in task_lower for k in ['data', '데이터', 'csv', 'process']):
            return 'data', task
        elif any(k in task_lower for k in ['분석', 'analysis', 'model', 'regression']):
            return 'analysis', task
        elif any(k in task_lower for k in ['문서', 'docs', 'workflow', 'readme']):
            return 'docs', task
        elif any(k in task_lower for k in ['리팩터', 'refactor', '구조', '정리']):
            return 'refactor', task
        else:
            return 'chore', task


def extract_day_number(day_section):
    """Day 섹션에서 Day 번호 추출"""
    if not day_section:
        return "?"
    
    match = re.search(r"Day (\d+)", day_section)
    return match.group(1) if match else "?"


def main():
    """메인 실행 함수"""
    print("🤖 전투일지 자동 커밋 시작...\n")
    
    # 1. 전투일지 파싱
    parser = BattleLogParser(LOG_PATH)
    today_section = parser.get_today_section()
    
    if not today_section:
        print("ℹ️  오늘 날짜의 전투일지 섹션을 찾을 수 없습니다.")
        return
    
    # 2. 완료 작업 추출
    completed_tasks = parser.extract_completed_tasks(today_section)
    outputs = parser.extract_key_outputs(today_section)
    day_num = extract_day_number(today_section)
    
    print(f"📋 Day {day_num} 완료 작업: {len(completed_tasks)}개")
    print(f"📦 산출물: {len(outputs)}개\n")
    
    if not completed_tasks and not outputs:
        print("ℹ️  완료된 작업이 없습니다. 전투일지만 커밋합니다.\n")
    
    # 3. Git 커밋
    committer = GitCommitter(REPO_ROOT)
    
    # 현재 브랜치 확인
    current_branch = committer.get_current_branch()
    print(f"📍 현재 브랜치: {current_branch}\n")
    
    # 전투일지 커밋
    if committer.check_changes():
        success = committer.commit_battle_log(day_num, completed_tasks)
        
        if success:
            # 4. 자동 푸시 (선택사항)
            push_now = os.environ.get('AUTO_PUSH', 'true').lower() == 'true'
            
            if push_now:
                print("\n🚀 원격 저장소에 푸시 중...")
                committer.push(current_branch)
            else:
                print("\nℹ️  자동 푸시가 비활성화되어 있습니다.")
                print(f"   수동으로 푸시하려면: git push origin {current_branch}")
        
        print("\n✅ 전투일지 자동 커밋 완료!")
        print(f"   GitHub에서 확인: https://github.com/hyunjimoon/tolzul/commits/{current_branch}")
    else:
        print("ℹ️  커밋할 변경사항이 없습니다.")


if __name__ == "__main__":
    main()
