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
  - 2025-10-21T10:17:19-04:00
---
~ [[Sources]]

> [!kindling] [[Books]] | [[Movies]] | [[Series]] | [[Courses]] | **[[Papers]]**

이 노트는 연구 논문들을 수집하고 포스터와 함께 시각적으로 표시합니다.

---

# 📜 Research Database

> *"First fall in love with your advisor, then find your research question"*

---

# 🖼️ 논문 포스터 갤러리

논문 포스터를 시각적으로 한눈에 볼 수 있습니다.

![[papers-all.base]]

> [!tip] 포스터 표시 방법
> `papers-all.base` 파일에서 다음 설정을 확인하세요:
> 
> **테이블 뷰에서 이미지 표시:**
> 1. `papers-all.base` 파일 열기
> 2. Properties → `image` 컬럼 추가
> 3. 이미지가 자동으로 embed되어 표시됩니다
> 
> **카드 뷰로 포스터 갤러리 만들기:**
> 1. `papers-all.base`에서 "Add view" 클릭
> 2. View 이름: "Gallery" 또는 "Posters"
> 3. Layout을 "Cards"로 변경
> 4. Image property를 "cover"로 설정 → `image` 선택
> 5. Card size와 aspect ratio 조정
> 
> 이제 base 내에서 "Gallery" 탭을 클릭하면 포스터 중심의 카드 뷰를 볼 수 있습니다!

---

# ⭐ 중요 논문 (Rank 5)

Rank 5 논문들을 포스터와 함께 표시합니다.

![[papers-foundational.base]]


## 🌟 Recently Read

![[papers-recent.base]]

---

## 🔬 By Field

### 👾 Cognition
![[papers-cog.base]]

### 🐢 Innovation  
![[papers-inv.base]]

### 🐙 Operations
![[papers-ops.base]]

### 🐅 CompBayes
![[papers-cba.base]]

---

## 🎯 By Mentor

### Charlie's School
![[papers-charlie.base]]

### Andrew's School
![[papers-andrew.base]]

### Scott's School
![[papers-scott.base]]

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

## Base에서 이미지 표시 설정

### papers-all.base 설정
1. **테이블 뷰**: Properties에서 `image` 컬럼을 추가하면 이미지가 자동으로 표시됩니다
2. **카드 뷰**: 새 뷰를 추가하고 Layout을 "Cards"로, Image property를 `image`로 설정

### 분야별/멘토별 base 설정
각 `papers-*.base` 파일에도 동일하게:
- **View 1 (Cards)**: 포스터 중심의 갤러리 뷰
- **View 2 (Table)**: 상세 정보가 포함된 테이블 뷰

이렇게 하면 각 섹션에서 탭을 전환하며 포스터 갤러리와 상세 테이블을 모두 볼 수 있습니다.

---

← [[Sources]]
