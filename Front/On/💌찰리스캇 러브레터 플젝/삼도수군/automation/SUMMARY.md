# 🤖 자동화 시스템 요약

## 📦 설치된 파일들

```
automation/
├── auto_commit.py      # 메인 스크립트
├── quick_commit.sh     # 즉시 커밋 (추천)
├── watch_log.sh        # 자동 감지
├── setup.sh            # 설치 스크립트
├── README.md           # 전체 가이드
└── QUICKSTART.md       # 3분 시작 가이드
```

---

## 🎯 핵심 개념

### Before 자동화
```
전투일지 작성 → 저장 → 터미널 → git add → git commit → git push
                              ↑
                         여기서 자주 까먹음!
```

### After 자동화
```
전투일지 작성 → 저장 → 끝! ✨
                 ↓
            (자동으로 Git 커밋)
```

---

## 🚀 사용법 (간단)

### 옵션 1: 수동 실행 (매일 저녁)
```bash
cd automation/
./quick_commit.sh
```

### 옵션 2: 자동 감지 (백그라운드)
```bash
cd automation/
./watch_log.sh
# 터미널 켜두기
# 전투일지 편집할 때마다 자동 커밋!
```

---

## 🔍 동작 원리

### 1. 전투일지 파싱
- 오늘 날짜의 "Day X" 섹션 찾기
- "완료:" 섹션에서 체크된 항목 추출
- "산출:" 섹션에서 파일명 추출

### 2. 커밋 메시지 생성
```python
# 자동으로 이런 메시지 생성:
"docs: battle log Day 5 (2025.10.25)

1. W0 commitment email 발송
2. Script 02 디버깅
3. 전투일지 업데이트"
```

### 3. Git 작업
```bash
git add 전투일지.md
git commit -m "..."
git push origin develop
```

---

## 💡 언제 사용할까?

| 상황 | 추천 방법 | 이유 |
|------|----------|------|
| 매일 저녁 회고 후 | `quick_commit.sh` | 간단하고 확실함 |
| 하루 종일 편집 | `watch_log.sh` | 자동 저장 |
| 여러 변경 후 한번에 | `quick_commit.sh` | 수동 제어 |
| 까먹을까 걱정 | `watch_log.sh` | 자동화 |

---

## 📊 자동화 이점 (정량화)

### 시간 절약
- 매일 3분 × 21일 = **63분 (1시간)**
- 커밋 메시지 고민 시간 = **0분**

### 품질 향상
- 커밋 누락 (10/24 같은): **0회**
- GitHub 잔디: **21/21일 (100%)**
- 일관된 커밋 포맷: **자동**

### 심리적 부담 감소
- "커밋 해야지" 기억할 필요: **없음**
- "메시지 뭐라 쓸까" 고민: **없음**
- "오늘 커밋했나" 확인: **필요없음**

---

## 🎓 학습 효과

### Charlie/Scott에게
- **매일 진행상황 자동 증명**
- 일관된 포맷으로 쉽게 추적
- GitHub 링크로 즉시 확인 가능

### 본인에게
- 작업 기록 자동 보존
- 사고 과정 타임라인 생성
- 논문 쓸 때 참고 자료

---

## 🔧 고급 설정

### 자동 푸시 끄기
```bash
export AUTO_PUSH=false
./quick_commit.sh
```

### 특정 브랜치에 커밋
```bash
git checkout feature/my-branch
./quick_commit.sh
```

### 커밋 메시지 확인만
```bash
# auto_commit.py 수정:
# self.run_git('commit', ...) → print(message)
```

---

## 🐛 트러블슈팅

### 증상: 아무 일도 안 일어남
**원인**: 전투일지에 오늘 날짜 섹션이 없음
**해결**: "## 🗓️ Day X - 2025.10.XX (요일)" 형식 확인

### 증상: "No changes to commit"
**원인**: 전투일지가 수정되지 않음
**해결**: 파일을 저장했는지 확인 (⌘+S)

### 증상: Permission denied
**원인**: 실행 권한 없음
**해결**: `chmod +x *.sh`

---

## 🎯 Best Practices

1. **매일 저녁 회고 후 실행** (`quick_commit.sh`)
2. **"완료:" 섹션에 ✅ 체크 정확히**
3. **산출물은 "산출:" 아래에 명시**
4. **GitHub 링크 확인하는 습관**

---

## 📞 지원

문제가 있으면:
1. `README.md` 다시 읽기
2. `QUICKSTART.md` 확인
3. 에러 메시지 복사해서 Claude에게
4. `git log` 로 커밋 내역 확인

**필사즉생! 🔥**
