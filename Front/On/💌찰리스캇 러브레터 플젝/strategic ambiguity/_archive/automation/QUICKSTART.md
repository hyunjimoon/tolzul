# ⚡ 빠른 시작 가이드

**3분 안에 자동화 시작하기**

---

## 1️⃣ 터미널 열기

**Applications → Terminal** 또는 **Spotlight (⌘+Space) → "Terminal"**

---

## 2️⃣ 자동화 폴더로 이동

터미널에 다음을 복사-붙여넣기:

```bash
cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/💌찰리스캇 러브레터 플젝/삼도수군/automation"
```

Enter 키 누르기.

---

## 3️⃣ 설치 실행 (첫 1회만)

```bash
bash setup.sh
```

아래처럼 나오면 성공:
```
✅ 설치 완료!
```

---

## 4️⃣ 이제 사용하기

### 매일 저녁 회고 후:

```bash
./quick_commit.sh
```

### 하루 종일 켜두기:

```bash
./watch_log.sh
```

---

## 🎉 완료!

이제 전투일지 저장하면 자동으로 GitHub에 커밋됩니다!

---

## 🆘 문제가 생기면?

### "Permission denied" 에러

```bash
chmod +x *.sh
./quick_commit.sh
```

### "Python not found" 에러

```bash
brew install python3
```

### "Git not configured" 에러

```bash
git config --global user.name "Hyunji Moon"
git config --global user.email "your@email.com"
```

---

## 📚 더 알고 싶다면

→ `README.md` 파일 참고
