---
up:
  - "[[Sources]]"
collection:
  - "[[Space/Library/Maps/Collections]]"
  - "[[Space/Library/Maps/Maps]]"
related:
  - "[[Space/Library/Maps/Books]]"
  - "[[Space/Library/Maps/Movies]]"
  - "[[Series]]"
created: 2022-01-01
rank: 1
mapState:
  - 🟩
cssclasses: []
modified:
  - 2025-10-18T23:23:24-04:00
  - 2025-10-21T09:51:40-04:00
tags:
  - map
---
~ [[Sources]] 

> [!kindling] **[[Space/Library/Maps/Books]]** | [[Space/Library/Maps/Movies]] | [[Series]] | [[Space/Library/Maps/Courses]] | [[Space/Library/Maps/Papers]] 

이 노트는 `Sources/언어/Books` 폴더의 모든 책을 수집합니다.

---

# 📚 책 표지와 함께 보기 (Card View)

책 표지 이미지와 함께 시각적으로 표시됩니다.

![[books.base#books-cards]]

---

# ⭐ 평점 높은 책 (Card View)

평점 4점 이상의 책들을 표지와 함께 표시합니다.

![[books.base#books-high-rated-cards]]

---

# 📊 표지 이미지가 포함된 테이블 (Dataview)

```dataview
TABLE WITHOUT ID
	year as Year,
	"![|60](" + image + ")" as Cover,
	file.link as Title,
	join(list(by)) as Author,
	yearXP as YearXP,
	rating as Rating
WHERE
	file.folder = "Space/Sources/언어/Books" and
	file.name != ".md"
SORT rating desc, year asc
```

---

# 📖 평점순 책 목록 (Table View)

![[books.base#books-by-rating]]

---

# 🗂️ 카테고리별 책 분류

![[books.base#books-by-category]]

---

# 🔥 읽는중인 책들

![[books.base#books-reading]]

---

# 💡 책 노트 작성 가이드

각 책 노트에 아래와 같은 메타데이터를 추가하세요:

```yaml
---
collection:
  - "[[Books]]"
by: "[[저자명]]"
year: 2024
yearXP: 2024
rating: 5
bookCategory: "비즈니스"
bookStatus: "완독"
image: "http://books.google.com/books/content?id=XXXXX"
created: 2024-01-01
---
```

## 이미지 추가 방법

### 방법 1: Google Books API (추천)
1. Google Books에서 책 검색
2. 책 표지 이미지 URL 복사
3. `image` 속성에 URL 추가

### 방법 2: 로컬 이미지
1. 책 표지 이미지를 Obsidian vault에 저장
2. `image` 속성에 파일명 입력: `"cover.jpg"`

## 속성 설명

- **year**: 출판년도
- **yearXP**: 읽은 연도
- **rating**: 평점 (1-5)
- **bookStatus**: `읽는중`, `완독`, `읽을 예정`
- **bookCategory**: 책 카테고리
- **image**: 책 표지 이미지 URL 또는 로컬 파일명
