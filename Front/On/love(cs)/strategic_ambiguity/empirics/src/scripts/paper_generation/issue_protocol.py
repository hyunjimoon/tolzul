#!/usr/bin/env python3
"""
🇰🇷 전라좌수군 Issue Protocol — Autonomous Agent Integration
=============================================================

이 모듈은 13척 함대의 Agent들이 자율적으로 Issue를 관리할 수 있게 합니다.

Usage:
    # Python에서
    from issue_protocol import IssueTracker
    tracker = IssueTracker()
    tracker.flag_issue("Jeong-T", "chap2_U_theory.md", "New citation", "Add Dorfman ref")
    
    # CLI에서
    python issue_protocol.py flag --agent Jeong-T --target chap2_U_theory.md --title "Citation" --claim "Add ref"
    python issue_protocol.py transition --id 020 --agent Kwon-T --stage BUILD
    python issue_protocol.py status
"""

import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Literal
from dataclasses import dataclass, field, asdict
from enum import Enum

# ============================================================================
# CONFIGURATION
# ============================================================================

ISSUE_FILE = Path(__file__).parent / "issue_queue.json"

# ============================================================================
# ENUMS & DATA STRUCTURES
# ============================================================================

class Stage(Enum):
    FLAG = "FLAG"
    REVIEW = "REVIEW"
    BUILD = "BUILD"
    MERGE = "MERGE"
    MERGED = "MERGED"

class Priority(Enum):
    RED = "red"       # Critical: 이론/구조 (24h SLA)
    YELLOW = "yellow" # Important: 표현/톤 (48h SLA)
    GREEN = "green"   # Pending: 통제사 결정 대기
    BLUE = "blue"     # Enhancement: Phase 2

# Stage Icons for Dashboard
STAGE_ICONS = {
    "FLAG": "🏴",
    "REVIEW": "📐",
    "BUILD": "🔨",
    "MERGE": "⚓",
    "MERGED": "✅"
}

# Valid Stage Transitions
VALID_TRANSITIONS = {
    "FLAG": ["REVIEW"],
    "REVIEW": ["BUILD", "FLAG"],      # Can reject back to FLAG
    "BUILD": ["MERGE", "REVIEW"],     # Can reject back to REVIEW
    "MERGE": ["MERGED", "BUILD"],     # Can reject back to BUILD
    "MERGED": []                       # Terminal state
}

# Agent Responsibilities
AGENT_STAGE_OWNERSHIP = {
    "FLAG": ["Jeong-T", "Jeong-E", "Jeong-I", "Jeong-D"],
    "REVIEW": ["Kwon-T", "Kwon-E", "Kwon-I", "Kwon-D"],
    "BUILD": ["Na-T", "Na-E", "Na-I", "Na-D"],
    "MERGE": ["Kim-V", "Kim-U", "Kim-C", "Kim-N"]
}

# ============================================================================
# ISSUE DATA CLASS
# ============================================================================

@dataclass
class HistoryEntry:
    stage: str
    owner: str
    note: str
    timestamp: str

@dataclass
class Issue:
    id: str
    target: str
    target_code: str
    title: str
    stage: str
    owner: str
    priority: str
    claim: str
    created_at: str = ""
    updated_at: str = ""
    history: List[Dict] = field(default_factory=list)
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "target": self.target,
            "target_code": self.target_code,
            "title": self.title,
            "stage": self.stage,
            "owner": self.owner,
            "priority": self.priority,
            "claim": self.claim,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "history": self.history
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Issue':
        return cls(
            id=data.get("id", ""),
            target=data.get("target", ""),
            target_code=data.get("target_code", ""),
            title=data.get("title", ""),
            stage=data.get("stage", "FLAG"),
            owner=data.get("owner", ""),
            priority=data.get("priority", "yellow"),
            claim=data.get("claim", ""),
            created_at=data.get("created_at", ""),
            updated_at=data.get("updated_at", ""),
            history=data.get("history", [])
        )

# ============================================================================
# ISSUE TRACKER CLASS
# ============================================================================

class IssueTracker:
    """
    전라좌수군 Issue Tracker
    
    각 Agent가 자율적으로 Issue를 생성, 전환, 조회할 수 있습니다.
    """
    
    def __init__(self, issue_file: Path = ISSUE_FILE):
        self.issue_file = issue_file
        self.issues: List[Issue] = []
        self._load()
    
    def _load(self):
        """Load issues from JSON file"""
        if self.issue_file.exists():
            with open(self.issue_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.issues = [Issue.from_dict(i) for i in data.get("issues", [])]
    
    def _save(self):
        """Save issues to JSON file"""
        data = {"issues": [i.to_dict() for i in self.issues]}
        with open(self.issue_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def _next_id(self) -> str:
        """Generate next issue ID"""
        if not self.issues:
            return "001"
        max_id = max(int(i.id) for i in self.issues)
        return str(max_id + 1).zfill(3)
    
    def _parse_target_code(self, target: str) -> str:
        """
        Parse target file to target code
        e.g., chap2_U_theory.md -> U-T
        """
        parts = target.replace(".md", "").split("_")
        if len(parts) >= 3:
            paper = parts[1]  # U, C, N
            section = parts[2]  # introduction, theory, empirics, discussion
            section_map = {
                "introduction": "I",
                "theory": "T",
                "empirics": "E",
                "discussion": "D",
                "abstract": "Abs"
            }
            section_code = section_map.get(section.lower(), section[0].upper())
            return f"{paper}-{section_code}"
        return "?"
    
    # =========================================================================
    # AGENT ACTIONS
    # =========================================================================
    
    def flag_issue(
        self,
        agent: str,
        target: str,
        title: str,
        claim: str,
        priority: str = "yellow"
    ) -> Issue:
        """
        🏴 FLAG: 정운이 새 이슈를 발견하고 등록
        
        Args:
            agent: 발견한 Agent (e.g., "Jeong-T")
            target: 대상 파일 (e.g., "chap2_U_theory.md")
            title: 이슈 제목 (10자 이내 권장)
            claim: 핵심 주장 (50자 이내)
            priority: red|yellow|green|blue
        
        Returns:
            생성된 Issue 객체
        """
        now = datetime.now().isoformat()
        
        issue = Issue(
            id=self._next_id(),
            target=target,
            target_code=self._parse_target_code(target),
            title=title,
            stage="FLAG",
            owner=agent,
            priority=priority,
            claim=claim,
            created_at=now,
            updated_at=now,
            history=[{
                "stage": "FLAG",
                "owner": agent,
                "note": "Issue flagged",
                "timestamp": now
            }]
        )
        
        self.issues.append(issue)
        self._save()
        
        print(f"🏴 Issue #{issue.id} flagged by {agent}: {title}")
        return issue
    
    def transition(
        self,
        issue_id: str,
        agent: str,
        to_stage: str,
        note: str = ""
    ) -> bool:
        """
        Stage 전환 (FLAG → REVIEW → BUILD → MERGE → MERGED)
        
        Args:
            issue_id: 이슈 ID (e.g., "020")
            agent: 전환하는 Agent (e.g., "Kwon-T")
            to_stage: 목표 Stage
            note: 전환 사유
        
        Returns:
            성공 여부
        """
        for issue in self.issues:
            if issue.id == issue_id:
                current = issue.stage
                
                # Validate transition
                if to_stage not in VALID_TRANSITIONS.get(current, []):
                    print(f"❌ Invalid transition: {current} → {to_stage}")
                    print(f"   Valid transitions from {current}: {VALID_TRANSITIONS[current]}")
                    return False
                
                # Check rejection requires note
                if to_stage in ["FLAG", "REVIEW"] and current != "FLAG" and not note:
                    print(f"⚠️ Rejection to {to_stage} requires a note/reason")
                    return False
                
                # Update issue
                now = datetime.now().isoformat()
                issue.stage = to_stage
                issue.owner = agent
                issue.updated_at = now
                issue.history.append({
                    "stage": to_stage,
                    "owner": agent,
                    "note": note or f"Transitioned to {to_stage}",
                    "timestamp": now
                })
                
                self._save()
                
                icon = STAGE_ICONS.get(to_stage, "?")
                print(f"{icon} Issue #{issue_id}: {current} → {to_stage} by {agent}")
                return True
        
        print(f"❌ Issue #{issue_id} not found")
        return False
    
    def review_pass(self, issue_id: str, agent: str, spec: str = "") -> bool:
        """📐 REVIEW PASS: 권준이 검토 통과 → BUILD로 전환"""
        return self.transition(issue_id, agent, "BUILD", f"REVIEW PASS: {spec}")
    
    def review_fail(self, issue_id: str, agent: str, reason: str) -> bool:
        """📐 REVIEW FAIL: 권준이 검토 실패 → FLAG로 반려"""
        return self.transition(issue_id, agent, "FLAG", f"REVIEW FAIL: {reason}")
    
    def build_complete(self, issue_id: str, agent: str, summary: str = "") -> bool:
        """🔨 BUILD COMPLETE: 나대용이 구현 완료 → MERGE로 전환"""
        return self.transition(issue_id, agent, "MERGE", f"BUILD COMPLETE: {summary}")
    
    def build_reject(self, issue_id: str, agent: str, reason: str) -> bool:
        """🔨 BUILD REJECT: 나대용이 스펙 문제 → REVIEW로 반려"""
        return self.transition(issue_id, agent, "REVIEW", f"BUILD REJECT: {reason}")
    
    def merge_approve(self, issue_id: str, agent: str, note: str = "") -> bool:
        """⚓ MERGE APPROVE: 김완이 검증 통과 → MERGED"""
        return self.transition(issue_id, agent, "MERGED", f"MERGE APPROVED: {note}")
    
    def merge_reject(self, issue_id: str, agent: str, reason: str, to_stage: str = "BUILD") -> bool:
        """⚓ MERGE REJECT: 김완이 검증 실패 → BUILD 또는 FLAG로 반려"""
        return self.transition(issue_id, agent, to_stage, f"MERGE REJECTED: {reason}")
    
    # =========================================================================
    # QUERY METHODS
    # =========================================================================
    
    def get_issue(self, issue_id: str) -> Optional[Issue]:
        """특정 이슈 조회"""
        for issue in self.issues:
            if issue.id == issue_id:
                return issue
        return None
    
    def get_by_stage(self, stage: str) -> List[Issue]:
        """특정 Stage의 모든 이슈"""
        return [i for i in self.issues if i.stage == stage]
    
    def get_by_owner(self, owner: str) -> List[Issue]:
        """특정 Agent의 모든 이슈"""
        return [i for i in self.issues if i.owner == owner]
    
    def get_by_priority(self, priority: str) -> List[Issue]:
        """특정 Priority의 모든 이슈"""
        return [i for i in self.issues if i.priority == priority]
    
    def get_by_target(self, target_code: str) -> List[Issue]:
        """특정 Target Code의 모든 이슈 (e.g., U-T)"""
        return [i for i in self.issues if i.target_code == target_code]
    
    def get_active(self) -> List[Issue]:
        """활성 이슈 (MERGED 제외)"""
        return [i for i in self.issues if i.stage != "MERGED"]
    
    def get_pending_for_agent(self, agent_prefix: str) -> List[Issue]:
        """
        특정 Agent 유형에게 대기 중인 이슈
        e.g., "Jeong" → FLAG 상태의 모든 이슈
        e.g., "Kwon" → REVIEW 상태의 모든 이슈
        """
        stage_map = {
            "Jeong": "FLAG",
            "Kwon": "REVIEW", 
            "Na": "BUILD",
            "Kim": "MERGE"
        }
        target_stage = stage_map.get(agent_prefix)
        if target_stage:
            return self.get_by_stage(target_stage)
        return []
    
    # =========================================================================
    # REPORTING
    # =========================================================================
    
    def status_report(self) -> str:
        """전체 현황 보고"""
        lines = [
            "=" * 60,
            "🇰🇷 전라좌수군 Issue Registry 현황",
            "=" * 60,
            ""
        ]
        
        # By Stage
        lines.append("📊 Stage별 현황:")
        for stage in ["FLAG", "REVIEW", "BUILD", "MERGE", "MERGED"]:
            issues = self.get_by_stage(stage)
            icon = STAGE_ICONS.get(stage, "?")
            ids = ", ".join([f"#{i.id}" for i in issues])
            lines.append(f"  {icon} {stage}: {len(issues)}건 [{ids}]")
        
        lines.append("")
        
        # By Priority
        lines.append("🚨 Priority별 현황:")
        priority_icons = {"red": "🔴", "yellow": "🟡", "green": "🟢", "blue": "🔵"}
        for priority in ["red", "yellow", "green", "blue"]:
            issues = self.get_by_priority(priority)
            icon = priority_icons.get(priority, "?")
            lines.append(f"  {icon} {priority}: {len(issues)}건")
        
        lines.append("")
        
        # Active Issues
        active = self.get_active()
        lines.append(f"📋 활성 이슈: {len(active)}건")
        for issue in active:
            icon = STAGE_ICONS.get(issue.stage, "?")
            lines.append(f"  {icon} #{issue.id} [{issue.target_code}] {issue.title} ({issue.owner})")
        
        return "\n".join(lines)
    
    def issue_detail(self, issue_id: str) -> str:
        """특정 이슈 상세 정보"""
        issue = self.get_issue(issue_id)
        if not issue:
            return f"❌ Issue #{issue_id} not found"
        
        icon = STAGE_ICONS.get(issue.stage, "?")
        priority_icons = {"red": "🔴", "yellow": "🟡", "green": "🟢", "blue": "🔵"}
        p_icon = priority_icons.get(issue.priority, "?")
        
        lines = [
            f"{icon} Issue #{issue.id}: {issue.title}",
            "-" * 40,
            f"Target: {issue.target} ({issue.target_code})",
            f"Stage: {issue.stage}",
            f"Owner: {issue.owner}",
            f"Priority: {p_icon} {issue.priority}",
            f"Claim: {issue.claim}",
            "",
            "History:"
        ]
        
        for h in issue.history:
            h_icon = STAGE_ICONS.get(h["stage"], "?")
            lines.append(f"  {h_icon} {h['stage']} by {h['owner']}: {h['note']}")
        
        return "\n".join(lines)


# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="🇰🇷 전라좌수군 Issue Tracker CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # 새 이슈 FLAG
    python issue_protocol.py flag --agent Jeong-T --target chap2_U_theory.md \\
        --title "Citation" --claim "Add Dorfman ref" --priority blue

    # Stage 전환
    python issue_protocol.py transition --id 020 --agent Kwon-T --stage BUILD --note "Spec ready"

    # 현황 보고
    python issue_protocol.py status

    # 이슈 상세
    python issue_protocol.py detail --id 020

    # Agent별 대기 이슈
    python issue_protocol.py pending --agent Kwon
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # FLAG command
    flag_parser = subparsers.add_parser("flag", help="새 이슈 FLAG")
    flag_parser.add_argument("--agent", required=True, help="Agent (e.g., Jeong-T)")
    flag_parser.add_argument("--target", required=True, help="Target file")
    flag_parser.add_argument("--title", required=True, help="Issue title")
    flag_parser.add_argument("--claim", required=True, help="Core claim")
    flag_parser.add_argument("--priority", default="yellow", help="red|yellow|green|blue")
    
    # TRANSITION command
    trans_parser = subparsers.add_parser("transition", help="Stage 전환")
    trans_parser.add_argument("--id", required=True, help="Issue ID")
    trans_parser.add_argument("--agent", required=True, help="Agent")
    trans_parser.add_argument("--stage", required=True, help="Target stage")
    trans_parser.add_argument("--note", default="", help="Transition note")
    
    # STATUS command
    subparsers.add_parser("status", help="전체 현황 보고")
    
    # DETAIL command
    detail_parser = subparsers.add_parser("detail", help="이슈 상세")
    detail_parser.add_argument("--id", required=True, help="Issue ID")
    
    # PENDING command
    pending_parser = subparsers.add_parser("pending", help="Agent 대기 이슈")
    pending_parser.add_argument("--agent", required=True, help="Agent prefix (Jeong|Kwon|Na|Kim)")
    
    args = parser.parse_args()
    tracker = IssueTracker()
    
    if args.command == "flag":
        tracker.flag_issue(args.agent, args.target, args.title, args.claim, args.priority)
    
    elif args.command == "transition":
        tracker.transition(args.id, args.agent, args.stage, args.note)
    
    elif args.command == "status":
        print(tracker.status_report())
    
    elif args.command == "detail":
        print(tracker.issue_detail(args.id))
    
    elif args.command == "pending":
        issues = tracker.get_pending_for_agent(args.agent)
        if issues:
            print(f"📋 {args.agent} 대기 이슈 ({len(issues)}건):")
            for i in issues:
                icon = STAGE_ICONS.get(i.stage, "?")
                print(f"  {icon} #{i.id} [{i.target_code}] {i.title}")
        else:
            print(f"✅ {args.agent} 대기 이슈 없음")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
