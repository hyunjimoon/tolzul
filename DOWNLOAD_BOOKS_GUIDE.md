# 언어/Books 폴더 다운로드 가이드 (Download Guide)

이 문서는 커밋 `642a503`에 있는 `언어/Books` 폴더를 로컬 컴퓨터에 다운로드하는 방법을 안내합니다.

## 📍 폴더 위치
- **경로**: `Space/Sources/언어/Books/`
- **커밋**: `642a50388ece57be22d7f37e323f4e83f92e4081`

## 🔗 직접 링크 (Direct Links)

### GitHub에서 폴더 보기
[📁 언어/Books 폴더 보기 (커밋 642a503)](https://github.com/hyunjimoon/tolzul/tree/642a503/Space/Sources/%EC%96%B8%EC%96%B4/Books)

### 전체 커밋 다운로드 (ZIP)
[⬇️ 커밋 642a503 전체 다운로드 (ZIP)](https://github.com/hyunjimoon/tolzul/archive/642a503.zip)

---

## 📥 다운로드 방법

### 방법 1: Git 명령어 사용 (권장)

터미널에서 다음 명령어를 실행하세요:

```bash
# 1. 저장소 클론
git clone https://github.com/hyunjimoon/tolzul.git
cd tolzul

# 2. 해당 커밋으로 체크아웃
git checkout 642a503

# 3. 원하는 폴더만 복사
cp -r "Space/Sources/언어/Books" ~/Desktop/Books
```

### 방법 2: 특정 폴더만 Sparse Checkout으로 다운로드

```bash
# 새 디렉토리 생성
mkdir tolzul-books && cd tolzul-books

# Git 초기화
git init
git remote add origin https://github.com/hyunjimoon/tolzul.git

# Sparse checkout 설정
git config core.sparseCheckout true
echo "Space/Sources/언어/Books/" >> .git/info/sparse-checkout

# 해당 커밋만 가져오기
git fetch --depth 1 origin 642a503
git checkout FETCH_HEAD
```

### 방법 3: GitHub 웹에서 직접 다운로드

1. [이 링크](https://github.com/hyunjimoon/tolzul/archive/642a503.zip)를 클릭하여 전체 ZIP 다운로드
2. ZIP 파일 압축 해제
3. `tolzul-642a503/Space/Sources/언어/Books/` 폴더를 원하는 위치로 이동

### 방법 4: GitHub CLI 사용

```bash
# GitHub CLI가 설치되어 있다면
gh repo clone hyunjimoon/tolzul
cd tolzul
git checkout 642a503
```

---

## 📂 폴더 구조

`언어/Books` 폴더에는 다음 항목들이 포함되어 있습니다:

### 루트 파일들 (51개)
- `.md`
- `10 참나라니 참나.md`
- `25도리언그레이의초상.md`
- `25보르헤스_원형의폐허들.md`
- `F. Scott Fitzgerald.md`
- `Larry McMurtry.md`
- `Math without numbers.md`
- `Somerset Maugham.md`
- `The Better Angels of Our Nature.md`
- `dark psychology.md`
- `diary.md`
- `edconway(material_world).md`
- `harari_nexus.md`
- `heuristics.md`
- `leke-arnold bennett 10step.md`
- `linguistic advice.md`
- `mark twain.md`
- `mary oliver.md`
- `on writing steven king.md`
- `origin of the word squarely.md`
- `pulizer.md`
- `science of story telling.md`
- `steinbek.md`
- `ten-great-ideas-about-chance.md`
- `that has been my whole career!.md`
- `the divine comedy.md`
- `vertigo-as-a-turing-test.md`
- `zero to one.md`
- `경량문명.md`
- `규칙없음.md`
- `기술복제.md`
- `김도연 우리시대 기술혁명.md`
- `달라구트 꿈의 백화점.md`
- `데미안 독서모임.md`
- `디지털카르텔.md`
- `브람스를 좋아하세요?.md`
- `사업의 철학.md`
- `세상의 모든 전략은 전쟁에서 탄생했다.md`
- `세상의 모든 혁신은 전쟁에서 시작했다.md`
- `순서파괴.md`
- `시간의 지배자.md`
- `이어령의 마지막 수업.md`
- `천재들의 주사위.md`
- `총균쇠.md`
- `파타.md`
- `화이트헤드 주기성.md`
- `휴맥스, 강소기업 성장통을 넘다.md`
- `📘the moment of clarity.md`
- `📚language.md`
- `🛏️make your own bed.md`

### 하위 폴더들

#### 📁 graphic novel/ (2개 파일)
- `batman.md`
- `graphic novel list.md`

#### 📁 useful/ (8개 파일 + 1개 하위폴더)
- `8Practical Writing -Learning the art of persuasion.md`
- `Continuum of Signal Verbs.md`
- `factfulness.md`
- `genre.md`
- `gre-writing.md`
- `instructing copilot.md`
- `📝first you write a sentence.md`
- `📖textbook/` (21개 파일)

#### 📁 useless/ (47개 파일)
다양한 독서 노트와 메모

---

## ❓ 도움이 필요하시면

문제가 있으시면 GitHub Issues에서 질문해주세요.
