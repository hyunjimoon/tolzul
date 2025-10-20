---
up: "[[Sources]]"
collection:
  - "[[Collections]]"
  - "[[Maps]]"
created: 2025-10-14
rank: 5
mapState: 🟩
성장:
  - 2025-10-14T14:42:48-04:00
  - 2025-10-18T23:45:43-04:00
  - 2025-10-19T17:50:04-04:00
---
~ [[Sources]]

> [!kindling] [[Books]] | [[Movies]] | [[Series]] | [[Courses]] | **[[Papers]]**

이 노트는 연구 논문들을 수집하고 포스터와 함께 시각적으로 표시합니다.

---

# 📜 Research Database

> *"First fall in love with your advisor, then find your research question"*

---

# 📊 논문 포스터와 함께 보기 (Card View)

논문 포스터 이미지와 함께 시각적으로 표시됩니다.

![[papers-cards.base]]

---

# ⭐ 중요 논문 (Rank 5) - Card View

Rank 5 논문들을 포스터와 함께 표시합니다.

![[papers-foundational.base]]


## 🌟 Recently Read

![[papers-recent.base]]

---

## 🔬 By Field

### 👾 Cognition
![[papers-cog-cards.base]]

### 🐢 Innovation  
![[papers-inv-cards.base]]

### 🐙 Operations
![[papers-ops-cards.base]]

### 🐅 CompBayes
![[papers-cba-cards.base]]

---

## 🎯 By Mentor

### Charlie's School
![[papers-charlie.base]]

### Andrew's School
![[papers-andrew.base]]

### Scott's School
![[papers-scott.base]]

---

## 📊 All Papers (Table View)

![[papers-all.base]]

---

# 💡 논문 노트 작성 가이드

각 논문 노트에 아래와 같은 메타데이터를 추가하세요:

```yaml
---
collection:
  - "[[Papers]]"
by: "[[저자명]]"
year: 2024
rank: 5
battlefield: "cognition"
mentor: "charlie"
paperStatus: "reading"
image: "https://example.com/poster.jpg"
created: 2024-01-01
---
```

## 포스터 이미지 추가 방법

### 방법 1: 온라인 이미지 URL
1. 논문 포스터 이미지를 온라인에 업로드
2. 이미지 URL 복사
3. `image` 속성에 URL 추가

### 방법 2: 로컬 이미지
1. 포스터 이미지를 Obsidian vault에 저장
2. `image` 속성에 파일명 입력: `"poster.jpg"`

## 속성 설명

- **year**: 출판년도
- **rank**: 중요도 (1-5, 5가 가장 중요)
- **battlefield**: `cognition`, `innovation`, `operations`, `compbayes`
- **mentor**: `charlie`, `andrew`, `scott`
- **paperStatus**: `reading`, `read`, `toread`
- **image**: 포스터 이미지 URL 또는 로컬 파일명

---

← [[Sources]]
