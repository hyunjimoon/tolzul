---
tags:
  - charlie
  - scott
---
2025-05-05
![[📜Terwiesch09_innov_tourn 2025-05-05-9.svg]]
%%[[📜Terwiesch09_innov_tourn 2025-05-05-9|🖋 Edit in Excalidraw]]%%




2025-04-27
## Step 1: Mapping Segway Tasks to (S, A) Language

### Three Entrepreneurial States (S):

- **S₁: Prototype Stage (Initial State)** – "Prototype completed?"
- **S₂: Design and Supply Chain Stage (Intermediate State)** – "Ready for mass production?"
- **S₃: Market Validation Stage (Advanced State)** – "Market acceptance validated?"
    

### Three Entrepreneurial Actions (A):

- **A₁: Collaborate (Operational action)** – "Work with partners, team building, management setup"
- **A₂: Capitalize (Resource action)** – "Patent filing, Lobbying (legal readiness)"
- **A₃: Segment (Market testing action)** – "Demos, Customer Surveys, Sales Forecasts"
    

|Original Segway Task|Mapped State/Action|
|---|---|
|Prototype (A)|**S₁ → S₂** (state transition)|
|Design (B)|**S₂** (action required)|
|Supply Chain (C)|**S₂** (action required)|
|Lobby (D)|**A₂**|
|Patents (E)|**A₂**|
|Management (F)|**A₁**|
|Demos (G)|**A₃**|
|Survey (H)|**A₃**|
|Forecast (I)|**A₃**|

---

## Step 2: Intuitive Meaning of "Make sure actions make sense given your current state (D A S = 0)"

The intuitive logic is:
- Don't start detailed "Supply Chain" tasks (Action A₁: Collaborate) before your "Prototype" (State S₁) is confirmed.
- Don't extensively "Lobby" (Action A₂: Capitalize) until basic "Prototype" (State S₁) and "Design" (State S₂) are established.
- Don't run "Market surveys" or "Forecast" (Action A₃: Segment) until you have a functional "Prototype."
In other words, each action should logically follow from your current state.

---

## Step 3: Example Matrix Sizes and Structure

Suppose we define:

- **States (S)**: 3 × 1 vector [S₁, S₂, S₃]
    
- **Actions (A)**: 3 × 1 vector [A₁ (Collaborate), A₂ (Capitalize), A₃ (Segment)]
    
- **Dynamic Consistency Matrix (D)**: 3 × 3 × 3 tensor  
    (for simplicity, let's flatten to 3×3 for illustration, assuming we verify immediate consistency between state-action pairs)
    

Then, the consistency constraint looks like:

D⋅A⋅S=0D \cdot A \cdot S = 0

For clarity, let's consider it as D⋅(A⊗S)D \cdot (A \otimes S), flattened as a 3×9 matrix (D) multiplied by a 9×1 vector (A⊗S):

### Explicit Example (Segway):

Let:

- **S** = [Prototype ready? (yes=1,no=0), Design ready? (1,0), Market validated? (1,0)]
    
- **A** = [Collaborate?, Capitalize?, Segment?]
    

We have states/actions pairs as combinations, for example:

|Pair|Meaning|Validity (0=valid)|
|---|---|---|
|S₁=0, A₃=1|Prototype not ready, but performing market surveys|Invalid|
|S₂=0, A₁=1|Design not done, but setting up management/supply chain|Invalid|
|S₁=1, A₃=1|Prototype done, running market validation (Demos)|Valid|

---

### Numerical Example (Simplified):

Suppose currently we have states:

- Prototype = Done (S₁=1), Design = Not done (S₂=0), Market validation = Not done (S₃=0)
    

Thus, **S = [1, 0, 0]ᵀ**.

Now, say we attempt these actions simultaneously:

- Collaborate (A₁=1), Capitalize (A₂=1), Segment (A₃=1)  
    **A = [1, 1, 1]ᵀ** (attempting all at once)
    

The flattened combination vector **(A⊗S)** (size 9×1):
$$
A⊗S=[A1S1A1S2A1S3A2S1A2S2A2S3A3S1A3S2A3S3]=[1×11×01×01×11×01×01×11×01×0]=[100100100]A \otimes S = \begin{bmatrix} A₁S₁ \\ A₁S₂ \\ A₁S₃ \\ A₂S₁ \\ A₂S₂ \\ A₂S₃ \\ A₃S₁ \\ A₃S₂ \\ A₃S₃ \end{bmatrix} = \begin{bmatrix} 1 \times 1 \\ 1 \times 0 \\ 1 \times 0 \\ 1 \times 1 \\ 1 \times 0 \\ 1 \times 0 \\ 1 \times 1 \\ 1 \times 0 \\ 1 \times 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}
$$
The constraint matrix **D** (3×9) encodes valid/invalid combos (example):
$$
D=[000000000011011011011011011]D = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 1 \end{bmatrix}
$$
- Row1 (Prototype ready): all zeros (Prototype doesn't restrict actions here)
    
- Row2 (Design ready): restrict actions unless design done
    
- Row3 (Market validated): restrict actions unless market validated
    

Then checking consistency:
$$
D⋅(A⊗S)=[000000000011011011011011011][100100100]=[000]D \cdot (A \otimes S) = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
$$
Since the result is all zeros, our action-state combination is consistent. If, for instance, you tried "market validation" without "prototype done," you'd get a non-zero, flagging inconsistency:

- E.g., if S₁=0 (Prototype not done), and A₃=1 (Market validation action), you'd have inconsistency:
    

D(A⊗S)≠0D(A\otimes S)\neq0

This example clearly illustrates the meaning of:

DAS=0D A S = 0

ensuring logical coherence between states and actions.

---

## Intuition (10-year-old):

"You shouldn't try to do a market demo if you haven't even built your invention yet!"

This numerical illustration gives you a tangible sense of how the matrix structure ensures your entrepreneurial decisions (A) always make sense given the current state (S).


[[Terwiesch_Ulrich09_InnovTournaments.pdf]]

using [contents cld](https://claude.ai/chat/92583e3a-4eab-4bee-b5ea-8c4caa5d491e) ![[📜Terwiesch09_innov_tourn 2025-04-24-7.svg]]
%%[[📜Terwiesch09_innov_tourn 2025-04-24-7.md|🖋 Edit in Excalidraw]]%%


