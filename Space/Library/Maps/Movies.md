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
rank: 3
mapState:
  - 🟩
cssclasses: []
modified:
  - 2025-11-01T21:35:00-04:00
tags:
  - map
---
~ [[Sources]]

> [!kindling] [[Space/Library/Maps/Books]] | **[[Space/Library/Maps/Movies]]** | [[Series]] | [[Space/Library/Maps/Courses]] | [[Space/Library/Maps/Papers]] 

**Movies = 영화/영상 아카이브**

영화, 드라마, 이미지, YouTube 컨텐츠를 수집합니다.

---

# 🎬 Movie - 영화

극장 및 스트리밍 영화 컬렉션

![[movies.base#movies-all]]

---

# 📺 Drama - 드라마/시리즈

TV 드라마 및 시리즈 컬렉션

![[movies.base#drama-all]]

---

# 🎨 Image - 이미지/시각예술

사진, 그래픽 노블, 시각 작품

![[movies.base#image-all]]

---

# 🎥 YouTube - 유튜브 컨텐츠

유튜브 채널 및 영상 컬렉션

![[movies.base#youtube-all]]

---

# ⭐ 평점 높은 작품들

평점 4점 이상의 작품들을 모아봅니다.

![[movies.base#movies-high-rated]]

---

# 📊 전체 작품 목록

```dataview
TABLE WITHOUT ID
	year as Year,
	file.link as Title,
	join(list(by)) as Creator,
	rating as Rating,
	choice(contains(file.path, "Movies/movie"), "🎬 Movie",
	choice(contains(file.path, "Movies/drama"), "📺 Drama",
	choice(contains(file.path, "Movies/image"), "🎨 Image",
	choice(contains(file.path, "Movies/youtube"), "🎥 YouTube",
	"📹 Other")))) as Type
WHERE
	file.folder = "Space/Sources/Movies" OR
	contains(file.path, "Movies/movie") OR
	contains(file.path, "Movies/drama") OR
	contains(file.path, "Movies/image") OR
	contains(file.path, "Movies/youtube")
SORT rating desc, year desc
LIMIT 30
```

---

# 💡 영상 노트 작성 가이드

각 작품 노트에 아래와 같은 메타데이터를 추가하세요:

## Movie (영화)
```yaml
---
collection:
  - "[[Movies]]"
by: "[[감독명]]"
year: 2024
rating: 5
movieType: "Drama"
image: "https://example.com/poster.jpg"
created: 2024-01-01
---
```

## Drama (드라마)
```yaml
---
collection:
  - "[[Movies]]"
by: "[[제작자/연출]]"
year: 2024
rating: 5
dramaType: "시대극"
seasons: 1
episodes: 16
image: "https://example.com/poster.jpg"
created: 2024-01-01
---
```

## Image (이미지)
```yaml
---
collection:
  - "[[Movies]]"
by: "[[작가명]]"
year: 2024
rating: 5
imageType: "Photography"
image: "path/to/image.jpg"
created: 2024-01-01
---
```

## YouTube (유튜브)
```yaml
---
collection:
  - "[[Movies]]"
by: "[[채널명]]"
year: 2024
rating: 5
youtubeType: "교양"
url: "https://youtube.com/watch?v=..."
created: 2024-01-01
---
```

---

← [[Sources]]
