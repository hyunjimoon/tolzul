# 🐢 Dig Hub - Deep Analysis

**D**issect **I**n **G**ranularity

깊이 파고드는 방법론적 탐구자. Moshe Ben-Akiva의 이산선택분석—내재된 매개변수를 해부하고 중첩을 검증하는 scale parameter의 정교함.

주요 질문: "이 현상의 숨겨진 구조는 무엇인가?"

## 인지적 구조: 현미경적 분석가  
층층이 해부하고 구조 찾기
- "이것의 구성요소는?"
- "어떻게 작동하는가?"
- 예: BP|DE → BPD|E로 진화하는 프레임워크의 미세 구조 분석

대표 논문: [[Test_Quantities_Shape_Sensitivity_BayesianCalibration]]

## Core Mission
Dissect complex systems, unearth hidden parameters

## Key Files
```dataview
LIST
FROM #🐢dig
SORT file.mtime DESC
LIMIT 10
```
- [[📜🐢]]
## Recent Dissections
```dataview
TABLE file.ctime as "Created", length(file.outlinks) as "Connections"
FROM #🐢dig
WHERE file.ctime > date(today) - dur(7 days)
```

## Connections
- Deep Mode Partner: [[🐙offer]]
- Grounds the vision of: [[🐅 Gen Hub]]
