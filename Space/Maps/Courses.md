---
collection:
  - "[[Collections]]"
  - "[[Maps]]"
related:
  - "[[Books]]"
  - "[[Papers]]"
created: 2022-01-01
rank: 1.5
mapState:
  - 🟩
성장:
  - 2025-10-19T00:03:45-04:00
---
~ [[Sources]]

> [!kindling] [[Books]] | [[Movies]] | [[Series]] | **[[Courses]]** | [[Papers]]

이 노트는 `Sources/Courses` 폴더의 모든 강의를 수집하고 포스터와 함께 시각적으로 표시합니다.

---

# 🔥 현재 수강중인 강의 (Card View)

지금 진행중인 강의들을 포스터와 함께 표시합니다.

![[courses.base#courses-current]]

---

# 📚 전체 강의 포스터 보기 (Card View)

모든 강의를 포스터 이미지와 함께 시각적으로 표시합니다.

![[courses.base#courses-all-cards]]

---

# 🔬 Battlefield별 강의

## 👾 Cognition

![[courses.base#courses-cognition]]

## 🐢 Innovation

![[courses.base#courses-innovation]]

## 🐙 Operations

![[courses.base#courses-operations]]

## 🐅 CompBayes

![[courses.base#courses-compbayes]]

---

# 👨‍🏫 교수/강사별 강의 (Table View)

강사별로 그룹핑된 강의 목록입니다.

![[courses.base#courses-by-instructor]]

---

# 📊 카테고리별 강의 분류

![[courses.base#courses-by-category]]

---

# 📅 연도별 강의 (Table View)

연도별로 그룹핑된 강의 목록입니다.

![[courses.base#courses-by-year]]

---

# ✅ 수강 완료한 강의 (Card View)

![[courses.base#courses-completed]]

---

# 🌟 최근 업데이트된 강의

![[courses.base#courses-recent]]

---

# 📋 전체 강의 목록 (Table View)

상세 정보가 포함된 전체 강의 목록입니다.

![[courses.base#courses-all]]

---

# 💡 강의 노트 작성 가이드

각 강의 노트에 아래와 같은 메타데이터를 추가하세요:

```yaml
---
collection:
  - "[[Courses]]"
by: "[[교수명]]"
year: 2024
yearXP: 2024
semester: "Fall 2024"
courseCategory: "Cognition"
courseStatus: "진행중"
institution: "MIT"
courseCode: "9.66"
image: "https://example.com/course-poster.jpg"
created: 2024-01-01
---
```

## 포스터 이미지 추가 방법

### 방법 1: 온라인 이미지 URL
1. 강의 포스터 이미지를 온라인에 업로드
2. 이미지 URL 복사
3. `image` 속성에 URL 추가

### 방법 2: 로컬 이미지
1. 포스터 이미지를 Obsidian vault에 저장
2. `image` 속성에 파일명 입력: `"course_poster.jpg"`

### 방법 3: 강의 웹사이트 스크린샷
1. 강의 웹사이트 또는 실라버스 페이지 스크린샷
2. 이미지 저장 후 위 방법 1 또는 2 사용

## 속성 설명

- **yearXP**: 수강 연도 (경험한 연도)
- **year**: 강의가 개설된 연도
- **semester**: `"Fall 2024"`, `"Spring 2025"`, `"IAP 2025"` 등
- **courseStatus**: 
  - `진행중`: 현재 수강중
  - `완료`: 수강 완료
  - `계획`: 수강 예정
  - `청강`: 청강만 함
- **courseCategory**: `Cognition`, `Innovation`, `Operations`, `CompBayes` 등
- **institution**: `MIT`, `Harvard`, `Sloan` 등
- **courseCode**: `9.66`, `15.357` 등
- **by**: 교수/강사명 (wikilink 형식: `[[교수명]]`)
- **image**: 강의 포스터 이미지 URL 또는 로컬 파일명

## 🎯 추천 이미지 소스

1. **강의 웹사이트**: 공식 강의 페이지의 헤더 이미지
2. **실라버스**: 실라버스 첫 페이지 스크린샷
3. **강의 자료**: 대표 슬라이드나 다이어그램
4. **커스텀 디자인**: Canva 등으로 직접 디자인
5. **관련 이미지**: 강의 주제를 대표하는 이미지

---

← [[Sources]]
