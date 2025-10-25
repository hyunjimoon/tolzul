# 🤖 전투일지 자동 커밋 시스템

**"전투일지 저장 = Git 커밋"**

전투일지를 작성하고 저장하면 자동으로 Git에 커밋되고 GitHub에 푸시됩니다.

---

## 🎯 무엇이 자동화되나요?

### Before 자동화
```
1. 전투일지 작성 (10분)
2. 전투일지 저장
3. 터미널 열기 ⏰ 까먹기 쉬움
4. git add 전투일지.md
5. git commit -m "..."
6. git push
```

### After 자동화
```
1. 전투일지 작성 (10분)
2. 전투일지 저장
3. ✨ 끝! (나머지는 자동)
```

---

## 🚀 사용 방법 (3가지)

### 방법 1: 즉시 커밋 (추천) ⚡️

전투일지 작성 후:

```bash
# 터미널에서 실행
cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/💌찰리스캇 러브레터 플젝/삼도수군/automation"
./quick_commit.sh
```

**언제 사용**: 매일 저녁 회고 작성 후

---

### 방법 2: 자동 감지 (백그라운드) 🔄

전투일지를 편집할 때마다 자동으로 커밋:

```bash
# 터미널에서 실행 (한 번만)
cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/💌찰리스캇 러브레터 플젝/삼도수군/automation"
./watch_log.sh
```

그리고 터미널 창을 켜두세요. 이제:
- 전투일지 편집 → 저장 → 3초 후 자동 커밋!

**언제 사용**: 하루 종일 전투일지를 여러 번 업데이트할 때

---

### 방법 3: 수동 실행 (Python) 🐍

직접 Python 스크립트 실행:

```bash
cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/💌찰리스캇 러브레터 플젝/삼도수군/automation"
python3 auto_commit.py
```

---

## 📋 첫 설정 (1회만)

### 1. 실행 권한 부여

```bash
cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/💌찰리스캇 러브레터 플젝/삼도수군/automation"
chmod +x *.sh
```

### 2. 테스트 실행

```bash
./quick_commit.sh
```

아래처럼 나오면 성공:
```
🤖 전투일지 자동 커밋 시작...

📋 Day 5 완료 작업: 3개
📦 산출물: 2개

📍 현재 브랜치: develop

✅ Committed: docs: battle log Day 5 (2025.10.25)

🚀 원격 저장소에 푸시 중...
✅ Pushed to origin/develop

✅ 전투일지 자동 커밋 완료!
   GitHub에서 확인: https://github.com/hyunjimoon/tolzul/commits/develop
```

---

## 🎨 자동화가 생성하는 커밋 메시지

전투일지 내용을 분석해서 적절한 커밋 메시지를 자동 생성합니다:

### 예시 1: 기본 커밋
```
docs: battle log Day 5 (2025.10.25)

1. W0 commitment email 발송
2. Script 02 디버깅 진행 중
3. 전투일지 Day 1-4 업데이트
```

### 예시 2: 작업 타입 인식
전투일지에 이렇게 쓰면:
```
**완료**:
- ✅ Script 01 완성 및 실행
- ✅ 651MB company data 처리 성공
- ✅ Workflow 문서화
```

자동으로 이런 커밋들이 생성됩니다:
```
feat: Script 01 완성 및 실행
data: 651MB company data 처리 성공
docs: Workflow 문서화
```

---

## ⚙️ 설정 옵션

### 자동 푸시 끄기/켜기

기본적으로 커밋 후 자동으로 `git push`합니다.

**자동 푸시 끄기**:
```bash
export AUTO_PUSH=false
./quick_commit.sh
```

**자동 푸시 켜기** (기본값):
```bash
export AUTO_PUSH=true
./quick_commit.sh
```

---

## 🛠️ 문제 해결

### "Python not found" 에러

```bash
# Python 3 확인
python3 --version

# 없으면 설치
brew install python3
```

### "Git not configured" 에러

```bash
# Git 설정 확인
git config user.name
git config user.email

# 없으면 설정
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### "Permission denied" 에러

```bash
# 실행 권한 다시 부여
chmod +x quick_commit.sh
chmod +x watch_log.sh
```

---

## 💡 추천 워크플로우

### 매일 루틴

```
오전 (작업 시작):
  → watch_log.sh 실행 (터미널 켜두기)
  
하루 종일:
  → 전투일지 작성
  → 저장 (⌘S)
  → 🤖 자동 커밋!
  
저녁 (회고):
  → 전투일지 "🌙 저녁 회고" 작성
  → 저장
  → 🤖 자동 커밋!
  → watch_log.sh 종료 (Ctrl+C)
```

### 일주일 루틴

```
금요일 (Week 회고):
  → 전투일지 작성
  → ./quick_commit.sh
  → GitHub에서 weekly commits 확인
  → Charlie/Scott에게 링크 전송
```

---

## 📊 자동화 효과

| 지표 | 자동화 전 | 자동화 후 |
|------|----------|----------|
| 일일 시간 절약 | - | **3분** |
| 주간 시간 절약 | - | **21분** |
| 3주 시간 절약 | - | **63분 (1시간)** |
| 커밋 누락 | 자주 (10/24) | **0회** |
| GitHub 잔디 | 불규칙 | **매일** |
| Advisor visibility | 수동 | **자동** |

---

## 🎯 핵심 요약

1. **전투일지 저장 = Git 커밋** (더 이상 신경 안 써도 됨)
2. **매일 GitHub 잔디** (공백 날짜 불가능)
3. **자동 커밋 메시지** (일관된 포맷)
4. **시간 절약** (3주에 1시간)
5. **Accountability** (Charlie/Scott에게 자동 증명)

---

## 📞 도움이 필요하면

1. 이 README 다시 읽기
2. 에러 메시지 복사해서 Claude에게 물어보기
3. `git log`로 커밋 확인하기

**필사즉생! 🔥**
