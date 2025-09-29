

| 모델                                                                     | Founder Success Prior Mean | Founder Success Prior Precision (value) | World Success Posterior     | Value given Success  (value) | 특징                                                        |
| ---------------------------------------------------------------------- | -------------------------- | --------------------------------------- | --------------------------- | ---------------------------- | --------------------------------------------------------- |
| Gans 2023, 2025<br><br>\cite{chen2024programs} <br>(bandit literature) | △                          | x (0)                                   | x                           | x (V)                        | passive founder learning ground truth success probability |
| \cite{archibald2002should }                                            | .                          | .                                       | △(objective)                | X (1)                        | startup maximize success probability (variable)           |
| **M1**                                                                 | o                          | x (0)                                   | △ (prior becomes posterior) | X (1)                        | • 성공확률 = 상수<br>• 학습 없음<br>• 정태적 모델                        |
| **M2**                                                                 | o                          | x (1)                                   | △ (Posterior)               | X (1)                        | • 성공확률 = 확률변수<br>• 베이지안 학습<br>• φ는 변하지만 가치 고정             |
| **M2'**                                                                | o                          | o                                       | △ (Posterior)               | X (V)                        | • 가치변수 모두 내생화<br>• 완전 동적 모델<br>• τ 최적화 가능                 |

- o: Decision Variable
- △: variable but not decision (state)
- x: fixed, static, exogenous

[[tom_griffith]]
