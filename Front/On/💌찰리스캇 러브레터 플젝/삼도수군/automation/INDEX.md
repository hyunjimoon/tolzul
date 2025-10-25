# 📚 자동화 시스템 문서 인덱스

**"전투일지 저장 = Git 커밋"**

---

## 🎯 시작하기

### 처음 사용하는 분
1. ⚡ [**QUICKSTART.md**](./QUICKSTART.md) - **여기서 시작!** (3분)
2. 📖 [README.md](./README.md) - 전체 가이드
3. 📝 [SUMMARY.md](./SUMMARY.md) - 개념 정리

### 바로 사용하고 싶은 분
```bash
cd automation/
bash setup.sh      # 첫 1회만
./quick_commit.sh  # 매일 사용
```

---

## 📁 파일 구조

```
automation/
├── 📘 INDEX.md           ← 지금 보고 있는 파일
├── ⚡ QUICKSTART.md      ← 3분 시작 가이드
├── 📖 README.md          ← 전체 가이드 (자세함)
├── 📝 SUMMARY.md         ← 개념 요약
├── 🔗 ALIASES.md         ← 터미널 단축키 (선택)
│
├── 🤖 auto_commit.py     ← 메인 Python 스크립트
├── ⚡ quick_commit.sh    ← 즉시 커밋 (추천)
├── 🔍 watch_log.sh       ← 자동 감지
└── 🔧 setup.sh           ← 설치 스크립트
```

---

## 🚀 추천 사용 패턴

### 패턴 1: 간단 (대부분의 경우)

```bash
# 매일 저녁 회고 후
./quick_commit.sh
```

**장점**: 간단, 확실, 제어 가능

---

### 패턴 2: 자동 (하루 종일 편집)

```bash
# 아침에 한 번 실행
./watch_log.sh
# 터미널 켜두기
# 전투일지 편집할 때마다 자동!
```

**장점**: 완전 자동, 까먹을 수 없음

---

### 패턴 3: 고급 (터미널 단축키)

```bash
# 설정 (1회):
# ALIASES.md 참고

# 사용 (어디서든):
battle
```

**장점**: 초고속, 한 단어

---

## 🎓 학습 경로

### Level 1: 초보자 (첫 주)
1. ⚡ QUICKSTART.md 읽기
2. `setup.sh` 실행
3. `quick_commit.sh` 사용

### Level 2: 중급자 (둘째 주)
1. 📖 README.md 정독
2. `watch_log.sh` 시도
3. 자동 감지 익숙해지기

### Level 3: 고급자 (셋째 주)
1. 🔗 ALIASES.md 설정
2. `battle` 명령어 사용
3. 자동화 완전 체화

---

## 💡 FAQ

### Q: 어떤 방법이 가장 좋나요?
**A**: `quick_commit.sh`로 시작. 익숙해지면 `watch_log.sh` 시도.

### Q: 매번 터미널 열기 귀찮은데요?
**A**: ALIASES.md 설정하면 `battle` 한 단어로 끝!

### Q: 자동으로 안 되는데요?
**A**: 
1. 전투일지 저장했나요? (⌘+S)
2. 오늘 날짜 섹션이 있나요?
3. "완료:" 섹션이 있나요?

### Q: 커밋 메시지를 직접 쓰고 싶어요
**A**: 그냥 수동으로 Git 쓰세요. 이 도구는 자동화용입니다.

---

## 🎯 핵심 원칙

### 1. 간단함 (Simplicity)
```bash
./quick_commit.sh  # 이게 전부
```

### 2. 자동화 (Automation)
```
전투일지 저장 = Git 커밋
```

### 3. 일관성 (Consistency)
```
매일 같은 포맷
매일 같은 루틴
매일 GitHub 잔디
```

---

## 🔧 트러블슈팅

| 증상 | 해결책 | 참고 문서 |
|------|--------|----------|
| 실행 안됨 | `chmod +x *.sh` | QUICKSTART.md |
| Python 없음 | `brew install python3` | QUICKSTART.md |
| Git 설정 없음 | `git config --global...` | README.md |
| 커밋 안됨 | 전투일지 형식 확인 | README.md |
| 푸시 실패 | 인터넷 연결 확인 | README.md |

---

## 📊 성과 측정

### 자동화 전 (Day 1-4)
- 커밋 누락: 1회 (10/24)
- 커밋 시간: 3분/일
- 일관성: 불규칙

### 자동화 후 (Day 5+)
- 커밋 누락: **0회**
- 커밋 시간: **0분/일**
- 일관성: **완벽**

---

## 🎉 결론

**전투일지 작성에만 집중하세요.**

**나머지는 자동화가 처리합니다.**

---

## 📞 도움

1. 📘 이 INDEX.md 다시 보기
2. ⚡ QUICKSTART.md 재확인
3. 📖 README.md 정독
4. 🤖 Claude에게 질문

**필사즉생! 🔥**
