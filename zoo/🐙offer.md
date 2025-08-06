# 🐙 Cal Hub - Calibrated Execution

**C**alibrate **A**ctions to **L**andscape

현실의 물결에 이론을 조율하는 실행가. Charles Fine의 운영관리—기업가적 이론과 실천에 기여하는 operations management의 반직관적 지혜.

주요 질문: "이 아이디어를 어떻게 세상에 뿌리내리게 할까?"

## 인지적 구조: 실용적 조정자
이론을 현실 제약에 맞추기
- "실제로 어떻게 작동할까?"
- "제약 조건은 무엇인가?"
- 예: 확률 모델을 실제 스타트업 의사결정 도구로 변환

대표 논문: [[15774_analytical_operations_management]]

## Core Mission
Calibrate ideas to reality, make it work

## Key Files
```dataview
LIST
FROM #🐙cal
SORT file.mtime DESC
```

## Shipped Projects
```dataview
TABLE file.mtime as "Last Modified"
FROM #🐙cal
WHERE contains(file.name, "complete") OR contains(file.name, "done")
```

## Connections
- Deep Mode Partner: [[🐢can]]
- Executes visions from: [[👾user]]
