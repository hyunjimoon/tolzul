---
up:
  - "[[Home]]"
related: []
created: 2025-01-11
tags:
  - map
  - index
version: "1.0"
---

> [!map]+ # 🗺️ Maps
> 
> **지도의 지도**  
> _모든 길은 여기서 시작한다_
> 
> ```dataview
> TABLE WITHOUT ID
>   file.link as "지도",
>   created as "생성일"
> WHERE
>   contains(in, this.file.link) and
>   !contains(file.name, "Template")
> SORT file.name asc
> LIMIT 222
> ```

---

## 🧭 핵심 지도

### 전장 지도 (4대 전장)

- [[군인]] - 사천→한산→명량→노량 흐름
- [[학자]] - 베이지안 창업 연구
- [[이슬]] - 교육과 협력

### 시스템 지도

- [[지과낙관바람 지도]] - 3박자 베이지안 순환
- [[지과낙관바람 법칙]] - 실천 규칙

---

## 📖 Ideaverse 참고

Ideaverse Lite 1.5의 지도 시스템을 참고하여 구축.

Maps의 역할:
- **Navigation**: 어디로 갈지 안내
- **Connection**: 노트들을 연결
- **Overview**: 전체를 조망

---

*"지도를 보고, 길을 찾고, 여행을 떠나라"*
