---
성장:
  - 2025-10-19T00:31:22-04:00
---
# 🚀 Courses 카드뷰 설정 - 빠른 시작 가이드

## ✅ 완료된 작업
1. ✅ `/Space/Maps/courses.base` - 카드뷰 및 테이블뷰 정의 완료
2. ✅ `/Space/Maps/Courses.md` - Books 스타일의 Map 페이지 완성
3. ✅ `TEMPLATE_course.md` - 강의 노트 템플릿 생성

## 📋 다음 단계 (여러분이 해야 할 일)

### Step 1: 기존 강의 파일에 메타데이터 추가

각 강의 파일 (예: `11.412.md`, `5w.md` 등)의 **맨 위에** 다음 메타데이터를 추가하세요:

```yaml
---
collection:
  - "[[Courses]]"
by: "[[교수명]]"
year: 2024
yearXP: 2024
semester: "Fall 2024"
courseCategory: "Operations"
courseStatus: "완료"
institution: "MIT"
courseCode: "11.412"
image: ""
created: 2024-01-01
---
```

### Step 2: 강의 포스터 이미지 준비

**옵션 A: 빠른 시작 (이미지 없이)**
- `image: ""` 로 두면 텍스트만 표시됩니다
- 나중에 이미지를 추가할 수 있습니다

**옵션 B: 로컬 이미지 사용**
1. 강의 포스터 이미지를 준비 (스크린샷, 디자인 등)
2. Obsidian vault의 `Assets` 또는 `Images` 폴더에 저장
3. `image: "course_poster.jpg"` 형식으로 파일명 입력

**옵션 C: 온라인 이미지 사용**
1. 이미지를 온라인 (Google Drive, Imgur 등)에 업로드
2. 직접 링크 URL 복사
3. `image: "https://..."` 형식으로 URL 입력

### Step 3: 속성 값 매핑 가이드

**courseCategory** (Battlefield와 동일하게):
- `Cognition` - 인지과학 관련
- `Innovation` - 혁신/창업 관련  
- `Operations` - 운영관리 관련
- `CompBayes` - 계산/베이지안 관련
- `General` - 기타

**courseStatus**:
- `진행중` - 현재 수강중
- `완료` - 수강 완료
- `계획` - 수강 예정
- `청강` - 청강만 함

**semester**:
- `Fall 2024`
- `Spring 2025`
- `IAP 2025` (January Activities Period)
- `Summer 2024`

**institution**:
- `MIT`
- `Harvard`
- `Sloan` (MIT Sloan)
- `Brain and Cognitive Sciences` (MIT BCS)

### Step 4: 기존 파일 업데이트 예시

**Before (11.412.md):**
```markdown
- when to know ppl don't act in certain way
- neuroeconomics (brain imaging scan)
...
```

**After (11.412.md):**
```yaml
---
collection:
  - "[[Courses]]"
by: "[[Professor Name]]"
year: 2024
yearXP: 2024
semester: "Fall 2024"
courseCategory: "Cognition"
courseStatus: "완료"
institution: "MIT"
courseCode: "11.412"
image: ""
created: 2024-09-01
---

# 11.412 Course Title

## Notes
- when to know ppl don't act in certain way
- neuroeconomics (brain imaging scan)
...
```

## 🎨 이미지 제작 팁

### 1. Canva 사용 (추천)
- 사이즈: 1200x630px (소셜 미디어 표준)
- 강의 제목 + 교수명 + 학기 포함
- 대학 로고 또는 관련 아이콘 추가

### 2. 실라버스 스크린샷
- 실라버스 PDF의 첫 페이지 캡처
- 해상도 조정 (너무 크지 않게)

### 3. 강의 웹사이트
- 공식 강의 페이지 스크린샷
- 헤더 이미지 다운로드

## 🔄 우선순위별 업데이트 전략

### Priority 1: 현재 진행중인 강의
- `courseStatus: "진행중"` 설정
- 이미지 추가 (가장 자주 볼 것이므로)
- 카테고리와 메타데이터 정확히 입력

### Priority 2: 중요한 완료 강의
- 자주 참조하는 강의 위주
- 이미지는 옵션

### Priority 3: 나머지 강의
- 기본 메타데이터만 추가
- 이미지는 필요시 나중에

## 💡 Pro Tips

1. **일괄 업데이트**: 비슷한 유형의 강의들을 한 번에 업데이트
2. **템플릿 활용**: `TEMPLATE_course.md`를 복사해서 새 강의 노트 작성
3. **연결 강화**: `by` 필드에 교수 wikilink 사용으로 네트워크 구축
4. **태그 활용**: 필요시 추가 태그 사용 가능

## 📊 예상 결과

모든 강의에 메타데이터 추가 후 Courses.md에서:
- 🔥 현재 수강중인 강의가 최상단에 카드로 표시
- 📚 전체 강의를 포스터와 함께 시각적으로 탐색
- 🔬 Battlefield별로 필터링된 뷰
- 👨‍🏫 교수별로 그룹핑된 테이블
- 📅 연도별 타임라인

## ❓ 자주 묻는 질문

**Q: 모든 강의에 이미지를 추가해야 하나요?**
A: 아니요! 이미지 없이도 작동합니다. 중요한 강의부터 추가하세요.

**Q: 하위 폴더의 강의들도 자동으로 포함되나요?**
A: 네, `file.folder.contains("Sources/Courses")`로 하위 폴더도 검색됩니다.

**Q: 기존 내용을 변경해야 하나요?**
A: 아니요, 맨 위에 메타데이터만 추가하면 됩니다.

---

## 🎯 시작하기

1. `TEMPLATE_course.md` 열기
2. 메타데이터 구조 확인
3. 강의 하나를 선택해서 업데이트
4. `Courses.md` 열어서 결과 확인
5. 나머지 강의들 순차적으로 업데이트

**Happy organizing! 🚀**
