---
modified:
  - 2025-11-23T15:13:03-05:00
---
| 방법                     | 장점     | 단점                 | 사용 예시          |
| :--------------------- | :----- | :----------------- | :------------- |
| mtime (파일 수정시간)        | 빠름, 간단 | 내용 같아도 touch하면 무효화 | Make, CMake    |
| Content Hash (MD5/SHA) | 정확함    | 큰 파일은 느림           | Git, Docker    |
| Dependency Graph       | 강력함    | 구현 복잡              | Bazel, Webpack |
| Version Metadata       | 유연함    | 수동 관리 필요           | DVC, MLflow    |