# 🚀 터미널 단축키 설정 (Optional)

어디서든 `battle` 명령어로 즉시 커밋하기!

---

## 설정 방법

### 1. 터미널 설정 파일 열기

**Bash 사용자** (기본):
```bash
nano ~/.bashrc
```

**Zsh 사용자** (Mac 최신):
```bash
nano ~/.zshrc
```

### 2. 맨 아래에 추가

```bash
# 전투일지 자동 커밋 단축키
alias battle='cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/💌찰리스캇 러브레터 플젝/삼도수군/automation" && ./quick_commit.sh && cd -'

alias battle-watch='cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/💌찰리스캇 러브레터 플젝/삼도수군/automation" && ./watch_log.sh'
```

### 3. 저장하고 나가기

- **Ctrl + O** (저장)
- **Enter**
- **Ctrl + X** (종료)

### 4. 적용하기

**Bash**:
```bash
source ~/.bashrc
```

**Zsh**:
```bash
source ~/.zshrc
```

---

## 사용법

이제 **어디서든** 터미널에서:

```bash
battle
```

한 단어로 즉시 커밋! 🎉

또는 자동 감지 시작:

```bash
battle-watch
```

---

## 예시

```bash
# 홈 디렉토리에서
cd ~
battle
# → 자동으로 전투일지 커밋!

# 프로젝트 폴더에서
cd ~/projects/my-app
battle
# → 자동으로 전투일지 커밋!

# 어디서든!
battle
```

---

## 추가 단축키 (Optional)

```bash
# Git 상태 확인
alias bs='git status'

# 최근 커밋 보기
alias bl='git log --oneline -10'

# 전투일지 열기
alias bo='open "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/💌찰리스캇 러브레터 플젝/삼도수군/전투일지.md"'
```

---

## 전체 워크플로우 예시

```bash
# 1. 전투일지 열기
bo

# 2. 편집...

# 3. 저장 (⌘+S)

# 4. 커밋
battle

# 5. 확인
bl
```

**3초 만에 완료!** ⚡
