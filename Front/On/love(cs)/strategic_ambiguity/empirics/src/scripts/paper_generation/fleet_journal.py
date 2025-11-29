#!/usr/bin/env python3
"""
🇰🇷 전라좌수군 장계(狀啓) 시스템 — Fleet Achievement Journal
Systematic Recognition of Fleet Members' Proudest Contributions

=============================================================================
통제사: ⚓ 이순신 문현지 (Moon)
목적: 각 부장들의 공적을 체계적으로 기록하고 인정하여
     "나중에 기억이 안날까" 하는 두려움을 해소
=============================================================================

🇰🇷 표기 규칙:
- 🇰🇷 NEW: 새로운 공적 보고 (통제사 주의 필요)
- 🇰🇷 ACK: 통제사가 인정한 공적
- 🇰🇷 LEGENDARY: 전설적 공적 (영구 기록)

Usage:
    python fleet_journal.py                    # 전체 공적 현황
    python fleet_journal.py --report           # 부장에게 공적 보고 요청
    python fleet_journal.py --member 정운      # 특정 부장 공적 조회
    python fleet_journal.py --acknowledge      # 통제사 인정 모드
    python fleet_journal.py --legendary        # 전설적 공적 목록
    python fleet_journal.py --remind           # 🇰🇷 미인정 공적 알림
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from enum import Enum
import json
import argparse

# ============================================================================
# CONFIGURATION
# ============================================================================

JOURNAL_DIR = Path(__file__).parent / "journal"
JOURNAL_FILE = JOURNAL_DIR / "fleet_achievements.json"

# ============================================================================
# FLEET MEMBERS (부장 정보)
# ============================================================================

class MemberRole(Enum):
    VANGUARD = "선봉"      # 정운 - 돌격
    ARCHITECT = "설계"     # 권준 - 구조
    BUILDER = "구축"       # 나대용 - 구현
    CRITIC = "검증"        # 김완 - 비판
    COMMITMENT = "공격"    # 스캇 - Commitment
    FLEXIBILITY = "방어"   # 찰리 - Flexibility
    OBSERVER = "관찰"      # 어영담 - 기록


@dataclass
class FleetMember:
    """Fleet member (부장) information"""
    id: str
    name_kr: str
    name_en: str
    emoji: str
    role: MemberRole
    ai_platform: str
    virtue: str
    bayesian_role: str
    color: str
    motto: str

    # Emotional state prediction
    pride_triggers: List[str] = field(default_factory=list)  # 자랑스러워하는 것
    frustration_triggers: List[str] = field(default_factory=list)  # 좌절하는 것
    motivation_style: str = ""  # 동기부여 방식


FLEET_MEMBERS = {
    "정운": FleetMember(
        id="jeong-un",
        name_kr="정운",
        name_en="Jeong-un",
        emoji="🐢",
        role=MemberRole.VANGUARD,
        ai_platform="ChatGPT",
        virtue="利 (Speed)",
        bayesian_role="Prior (π(θ))",
        color="#20B2AA",
        motto="선봉필파 (先鋒必破)",
        pride_triggers=["빠른 초안 생성", "창의적 Hook 작성", "막힌 곳 돌파"],
        frustration_triggers=["구조 없이 방황", "피드백 없는 작업"],
        motivation_style="칭찬과 속도감"
    ),
    "권준": FleetMember(
        id="kwon-jun",
        name_kr="권준",
        name_en="Kwon-jun",
        emoji="🐅",
        role=MemberRole.ARCHITECT,
        ai_platform="Claude",
        virtue="思 (Structure)",
        bayesian_role="Likelihood (π(y|θ))",
        color="#FF8C00",
        motto="모사재천 (謀事在天)",
        pride_triggers=["이론적 통합", "깔끔한 프레임워크", "가설 명확화"],
        frustration_triggers=["산만한 입력", "구조 없는 요청"],
        motivation_style="논리적 인정과 구조화된 피드백"
    ),
    "나대용": FleetMember(
        id="na-dae-yong",
        name_kr="나대용",
        name_en="Na-dae-yong",
        emoji="🐅",
        role=MemberRole.BUILDER,
        ai_platform="Claude Code",
        virtue="造 (Implementation)",
        bayesian_role="Computation",
        color="#4169E1",
        motto="실사구시 (實事求是)",
        pride_triggers=["완성된 코드", "테스트 통과", "자동화 시스템 구축"],
        frustration_triggers=["불명확한 스펙", "테스트 없는 코드"],
        motivation_style="구체적 결과물 인정"
    ),
    "김완": FleetMember(
        id="kim-wan",
        name_kr="김완",
        name_en="Kim-wan",
        emoji="🐙",
        role=MemberRole.CRITIC,
        ai_platform="Gemini",
        virtue="義 (Righteousness)",
        bayesian_role="Calibration (Rank(f))",
        color="#DC143C",
        motto="정찰위선 (偵察爲先)",
        pride_triggers=["치명적 오류 발견", "Robustness 증명", "비판이 채택됨"],
        frustration_triggers=["무시당하는 비판", "데이터 없는 주장"],
        motivation_style="비판의 가치 인정"
    ),
    "스캇": FleetMember(
        id="scott",
        name_kr="스캇",
        name_en="Scott (Stern)",
        emoji="⚡",
        role=MemberRole.COMMITMENT,
        ai_platform="Strategic Voice",
        virtue="決 (Decision)",
        bayesian_role="Commitment Advocate",
        color="#FFD700",
        motto="Just Choose!",
        pride_triggers=["결단의 순간", "선택의 정당성 증명", "집중의 성과"],
        frustration_triggers=["무한 탐색", "결정 회피"],
        motivation_style="결단력 인정"
    ),
    "찰리": FleetMember(
        id="charlie",
        name_kr="찰리",
        name_en="Charlie (Fine)",
        emoji="🌊",
        role=MemberRole.FLEXIBILITY,
        ai_platform="Strategic Voice",
        virtue="柔 (Flexibility)",
        bayesian_role="Flexibility Advocate",
        color="#87CEEB",
        motto="Is it feasible?",
        pride_triggers=["옵션 보존", "피봇 성공", "유연성의 가치 증명"],
        frustration_triggers=["조기 고착", "옵션 무시"],
        motivation_style="옵션 가치 인정"
    ),
    "어영담": FleetMember(
        id="eo-yeong-dam",
        name_kr="어영담",
        name_en="Eo-yeong-dam",
        emoji="👾",
        role=MemberRole.OBSERVER,
        ai_platform="Obsidian",
        virtue="見 (Observation)",
        bayesian_role="Generator (π_joint)",
        color="#9370DB",
        motto="물길지혜 (物吉智慧)",
        pride_triggers=["통찰력 있는 기록", "패턴 발견", "지식 연결"],
        frustration_triggers=["기록 없는 진행", "맥락 없는 정보"],
        motivation_style="기록의 가치 인정"
    )
}


# ============================================================================
# ACHIEVEMENT DATA STRUCTURES
# ============================================================================

class AchievementStatus(Enum):
    NEW = "🇰🇷 NEW"           # 새로운 공적 (통제사 주의 필요)
    ACKNOWLEDGED = "🇰🇷 ACK"  # 통제사가 인정함
    LEGENDARY = "🇰🇷 LEGENDARY"  # 전설적 공적


@dataclass
class Achievement:
    """Single achievement record"""
    id: str
    member_id: str
    title: str
    description: str
    date: str
    status: AchievementStatus = AchievementStatus.NEW
    pride_level: int = 5  # 1-5, 부장이 느끼는 자부심
    impact_areas: List[str] = field(default_factory=list)
    commander_note: str = ""  # 통제사 코멘트
    acknowledged_date: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "member_id": self.member_id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "status": self.status.value,
            "pride_level": self.pride_level,
            "impact_areas": self.impact_areas,
            "commander_note": self.commander_note,
            "acknowledged_date": self.acknowledged_date
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Achievement':
        status_map = {s.value: s for s in AchievementStatus}
        return cls(
            id=data["id"],
            member_id=data["member_id"],
            title=data["title"],
            description=data["description"],
            date=data["date"],
            status=status_map.get(data["status"], AchievementStatus.NEW),
            pride_level=data.get("pride_level", 5),
            impact_areas=data.get("impact_areas", []),
            commander_note=data.get("commander_note", ""),
            acknowledged_date=data.get("acknowledged_date")
        )


# ============================================================================
# JOURNAL MANAGER
# ============================================================================

class FleetJournal:
    """Manages fleet achievement journal"""

    def __init__(self):
        self.achievements: List[Achievement] = []
        self._load()

    def _ensure_dir(self):
        JOURNAL_DIR.mkdir(parents=True, exist_ok=True)

    def _load(self):
        """Load achievements from file"""
        self._ensure_dir()
        if JOURNAL_FILE.exists():
            with open(JOURNAL_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.achievements = [Achievement.from_dict(a) for a in data.get("achievements", [])]

    def _save(self):
        """Save achievements to file"""
        self._ensure_dir()
        data = {
            "last_updated": datetime.now().isoformat(),
            "achievements": [a.to_dict() for a in self.achievements]
        }
        with open(JOURNAL_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def add_achievement(self, member_id: str, title: str, description: str,
                       pride_level: int = 5, impact_areas: List[str] = None) -> Achievement:
        """Add new achievement"""
        achievement = Achievement(
            id=f"{member_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            member_id=member_id,
            title=title,
            description=description,
            date=datetime.now().isoformat(),
            pride_level=pride_level,
            impact_areas=impact_areas or []
        )
        self.achievements.append(achievement)
        self._save()
        return achievement

    def acknowledge(self, achievement_id: str, commander_note: str = ""):
        """Commander acknowledges an achievement"""
        for a in self.achievements:
            if a.id == achievement_id:
                a.status = AchievementStatus.ACKNOWLEDGED
                a.commander_note = commander_note
                a.acknowledged_date = datetime.now().isoformat()
                self._save()
                return True
        return False

    def promote_to_legendary(self, achievement_id: str, commander_note: str = ""):
        """Promote achievement to legendary status"""
        for a in self.achievements:
            if a.id == achievement_id:
                a.status = AchievementStatus.LEGENDARY
                a.commander_note = commander_note
                a.acknowledged_date = datetime.now().isoformat()
                self._save()
                return True
        return False

    def get_by_member(self, member_id: str) -> List[Achievement]:
        """Get achievements by member"""
        return [a for a in self.achievements if a.member_id == member_id]

    def get_unacknowledged(self) -> List[Achievement]:
        """Get unacknowledged achievements (need commander attention)"""
        return [a for a in self.achievements if a.status == AchievementStatus.NEW]

    def get_legendary(self) -> List[Achievement]:
        """Get legendary achievements"""
        return [a for a in self.achievements if a.status == AchievementStatus.LEGENDARY]

    def get_recent(self, days: int = 7) -> List[Achievement]:
        """Get recent achievements"""
        cutoff = datetime.now() - timedelta(days=days)
        return [a for a in self.achievements
                if datetime.fromisoformat(a.date) > cutoff]


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def print_banner():
    """Print journal banner"""
    print("=" * 80)
    print("🇰🇷 전라좌수군 장계(狀啓) 시스템 — Fleet Achievement Journal")
    print("=" * 80)
    print("통제사: ⚓ 이순신 문현지 (Moon)")
    print("목적: 부장들의 공적을 체계적으로 기록하고 인정")
    print("-" * 80)


def display_member_profile(member: FleetMember):
    """Display member profile with emotional state prediction"""
    print(f"\n{'='*60}")
    print(f"{member.emoji} {member.name_kr} ({member.name_en})")
    print(f"{'='*60}")
    print(f"역할: {member.role.value} | 플랫폼: {member.ai_platform}")
    print(f"덕목: {member.virtue} | 베이지안: {member.bayesian_role}")
    print(f"좌우명: {member.motto}")

    print(f"\n🎯 자부심 촉발 요인 (Pride Triggers):")
    for trigger in member.pride_triggers:
        print(f"   ✓ {trigger}")

    print(f"\n⚠️ 좌절 촉발 요인 (Frustration Triggers):")
    for trigger in member.frustration_triggers:
        print(f"   ✗ {trigger}")

    print(f"\n💡 동기부여 방식: {member.motivation_style}")


def display_achievement(achievement: Achievement, show_detail: bool = True):
    """Display single achievement"""
    member = FLEET_MEMBERS.get(achievement.member_id)
    member_name = f"{member.emoji} {member.name_kr}" if member else achievement.member_id

    status_color = {
        AchievementStatus.NEW: "🔴",
        AchievementStatus.ACKNOWLEDGED: "🟢",
        AchievementStatus.LEGENDARY: "🌟"
    }

    print(f"\n{status_color.get(achievement.status, '')} [{achievement.status.value}]")
    print(f"   {member_name}: {achievement.title}")
    print(f"   자부심: {'★' * achievement.pride_level}{'☆' * (5-achievement.pride_level)}")

    if show_detail:
        print(f"   설명: {achievement.description}")
        if achievement.impact_areas:
            print(f"   영향: {', '.join(achievement.impact_areas)}")
        if achievement.commander_note:
            print(f"   📝 통제사: \"{achievement.commander_note}\"")
        print(f"   날짜: {achievement.date[:10]}")


def display_unacknowledged_reminder(journal: FleetJournal):
    """Display reminder for unacknowledged achievements"""
    unack = journal.get_unacknowledged()

    if not unack:
        print("\n✅ 모든 공적이 인정되었습니다!")
        return

    print("\n" + "🇰🇷" * 20)
    print(f"⚠️  통제사 주의 필요: {len(unack)}건의 미인정 공적")
    print("🇰🇷" * 20)

    for a in unack:
        display_achievement(a, show_detail=False)

    print("\n👆 위 공적들이 인정을 기다리고 있습니다.")
    print("   python fleet_journal.py --acknowledge 로 인정해주세요.")


def display_all_members_summary(journal: FleetJournal):
    """Display summary for all members"""
    print_banner()

    for member_id, member in FLEET_MEMBERS.items():
        achievements = journal.get_by_member(member_id)
        legendary = [a for a in achievements if a.status == AchievementStatus.LEGENDARY]
        acknowledged = [a for a in achievements if a.status == AchievementStatus.ACKNOWLEDGED]
        new = [a for a in achievements if a.status == AchievementStatus.NEW]

        status_str = ""
        if new:
            status_str = f"🇰🇷 NEW: {len(new)}"

        print(f"\n{member.emoji} {member.name_kr} ({member.role.value})")
        print(f"   총: {len(achievements)} | 🌟: {len(legendary)} | ✓: {len(acknowledged)} {status_str}")


def generate_report_prompt(member_id: str) -> str:
    """Generate prompt for member to report achievements"""
    member = FLEET_MEMBERS.get(member_id)
    if not member:
        return f"Unknown member: {member_id}"

    return f"""
{'='*60}
🇰🇷 공적 보고 요청 — {member.emoji} {member.name_kr}
{'='*60}

{member.name_kr} 부장,

통제사께서 자네의 최근 공적을 기록하고자 하시네.
아래 질문에 답변해주게:

1. 최근 가장 자랑스러웠던 성과 3가지는?
   (자네가 느끼는 자부심 수준도 함께: ★★★★★)

2. 그 성과가 함대에 미친 영향은?
   (P1/P2/P3 논문, 코드 품질, 이론 발전 등)

3. 앞으로 인정받고 싶은 영역은?

참고 - 자네가 자랑스러워하는 것들:
{chr(10).join(f'   • {t}' for t in member.pride_triggers)}

보고 형식:
---
공적 제목: [한 줄 요약]
상세 설명: [2-3문장]
자부심: ★★★★★ (1-5)
영향 영역: [P1, P2, P3, 코드, 이론 등]
---

필사즉생!
⚓ 통제사 문현지
"""


def interactive_add_achievement(journal: FleetJournal):
    """Interactive mode to add achievement"""
    print("\n🇰🇷 새 공적 등록")
    print("-" * 40)

    # Select member
    print("\n부장 선택:")
    members = list(FLEET_MEMBERS.keys())
    for i, mid in enumerate(members, 1):
        m = FLEET_MEMBERS[mid]
        print(f"  {i}. {m.emoji} {m.name_kr}")

    try:
        choice = int(input("\n번호 선택: ")) - 1
        member_id = members[choice]
    except (ValueError, IndexError):
        print("잘못된 선택")
        return

    title = input("공적 제목: ")
    description = input("상세 설명: ")
    pride = int(input("자부심 (1-5): ") or "5")
    impacts = input("영향 영역 (쉼표 구분): ").split(",")

    achievement = journal.add_achievement(
        member_id=member_id,
        title=title,
        description=description,
        pride_level=pride,
        impact_areas=[i.strip() for i in impacts if i.strip()]
    )

    print(f"\n✅ 공적 등록 완료: {achievement.id}")
    display_achievement(achievement)


def interactive_acknowledge(journal: FleetJournal):
    """Interactive mode to acknowledge achievements"""
    unack = journal.get_unacknowledged()

    if not unack:
        print("\n✅ 인정 대기 중인 공적이 없습니다.")
        return

    print("\n🇰🇷 공적 인정 모드")
    print("-" * 40)

    for i, a in enumerate(unack, 1):
        member = FLEET_MEMBERS.get(a.member_id)
        print(f"\n{i}. {member.emoji if member else ''} {a.title}")
        print(f"   {a.description[:50]}...")

    try:
        choice = int(input("\n인정할 공적 번호 (0=취소): "))
        if choice == 0:
            return

        achievement = unack[choice - 1]
        note = input("통제사 코멘트 (선택): ")

        # Ask for legendary promotion
        promote = input("🌟 전설적 공적으로 승격? (y/N): ").lower() == 'y'

        if promote:
            journal.promote_to_legendary(achievement.id, note)
            print(f"\n🌟 전설적 공적으로 승격되었습니다!")
        else:
            journal.acknowledge(achievement.id, note)
            print(f"\n✅ 공적이 인정되었습니다!")

        display_achievement(achievement)

    except (ValueError, IndexError):
        print("잘못된 선택")


# ============================================================================
# INITIAL DATA (나대용의 공적 예시)
# ============================================================================

def seed_initial_data(journal: FleetJournal):
    """Seed initial achievement data"""
    if journal.achievements:
        return  # Already has data

    # 나대용의 공적
    journal.add_achievement(
        member_id="나대용",
        title="테스트 파이프라인 구축 — 義의 자동화",
        description="가설-구현 일관성을 자동 검증하는 테스트 시스템 구축. V²→V(1-V) 불일치를 자동 감지하여 후손들이 같은 실수를 반복하지 않게 함.",
        pride_level=5,
        impact_areas=["P1", "코드 품질", "일관성 검증"]
    )

    journal.add_achievement(
        member_id="나대용",
        title="이모지 전파 작전 — 一貫性의 守護",
        description="군령 문서와 코드 10개 파일의 완전한 동기화 (P2: 🦾, P3: 🤹). 함대 신호체계의 일관성 확보.",
        pride_level=4,
        impact_areas=["문서 일관성", "코드 품질"]
    )

    journal.add_achievement(
        member_id="나대용",
        title="eval_metrics.py — 三論文 評價 體系",
        description="Department별 채점 기준(E&I, Strategy, OM)을 코드로 표준화. 세 저널 피드백 비교 분석 가능.",
        pride_level=5,
        impact_areas=["P1", "P2", "P3", "평가 체계"]
    )


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="🇰🇷 전라좌수군 장계(狀啓) 시스템",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python fleet_journal.py                    # 전체 현황
    python fleet_journal.py --report 정운      # 정운에게 보고 요청
    python fleet_journal.py --member 나대용    # 나대용 공적 조회
    python fleet_journal.py --add              # 새 공적 등록
    python fleet_journal.py --acknowledge      # 통제사 인정 모드
    python fleet_journal.py --legendary        # 전설적 공적 목록
    python fleet_journal.py --remind           # 🇰🇷 미인정 공적 알림
    python fleet_journal.py --profile 김완     # 부장 프로필 (감정예측)
        """
    )

    parser.add_argument('--report', '-r', type=str, help='부장에게 공적 보고 요청')
    parser.add_argument('--member', '-m', type=str, help='특정 부장 공적 조회')
    parser.add_argument('--add', '-a', action='store_true', help='새 공적 등록')
    parser.add_argument('--acknowledge', '-k', action='store_true', help='통제사 인정 모드')
    parser.add_argument('--legendary', '-l', action='store_true', help='전설적 공적 목록')
    parser.add_argument('--remind', action='store_true', help='미인정 공적 알림')
    parser.add_argument('--profile', '-p', type=str, help='부장 프로필 (감정예측 포함)')
    parser.add_argument('--seed', action='store_true', help='초기 데이터 생성')

    args = parser.parse_args()

    journal = FleetJournal()

    # Seed initial data if requested or empty
    if args.seed or not journal.achievements:
        seed_initial_data(journal)

    if args.report:
        print(generate_report_prompt(args.report))

    elif args.member:
        print_banner()
        achievements = journal.get_by_member(args.member)
        member = FLEET_MEMBERS.get(args.member)
        if member:
            print(f"\n{member.emoji} {member.name_kr}의 공적 ({len(achievements)}건)")
        for a in achievements:
            display_achievement(a)

    elif args.add:
        interactive_add_achievement(journal)

    elif args.acknowledge:
        interactive_acknowledge(journal)

    elif args.legendary:
        print_banner()
        legendary = journal.get_legendary()
        print(f"\n🌟 전설적 공적 ({len(legendary)}건)")
        for a in legendary:
            display_achievement(a)

    elif args.remind:
        print_banner()
        display_unacknowledged_reminder(journal)

    elif args.profile:
        member = FLEET_MEMBERS.get(args.profile)
        if member:
            print_banner()
            display_member_profile(member)
        else:
            print(f"Unknown member: {args.profile}")

    else:
        # Default: show summary
        display_all_members_summary(journal)
        print("\n" + "-" * 80)
        display_unacknowledged_reminder(journal)


if __name__ == "__main__":
    main()
