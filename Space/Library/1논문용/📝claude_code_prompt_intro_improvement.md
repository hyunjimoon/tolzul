# Claude Code 프롬프트: generate_01_introduction.py 개선

## 작업 목표
`/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/generate_01_introduction.py`를 다음과 같이 개선해주세요.

## 핵심 변경사항

### 1. 7문단 구조로 확장 (기존 5문단 → 7문단)

기존 구조:
- Hook (2 paragraphs)
- Puzzle (1 paragraph)  
- Preview (1 paragraph)
- Contributions (bullet points)
- Roadmap (1 paragraph)

새 구조 (32문단 철칙 중 intro 7문단):
```python
INTRO_STRUCTURE = {
    "P1_GOSPEL": {
        "emoji": "📿",
        "role": "Gospel (X)",
        "question": "학계는 무엇을 믿고 있는가?",
        "they_say_i_say": "They Say",
        "template": "[Field]의 중심 아이디어 중 [X]만큼 확고한 것은 거의 없다. [Classic Citation 1, 2, 3]은 모두 [X]를 전제로 한다."
    },
    "P2_PUZZLE_1": {
        "emoji": "🧩",
        "role": "Puzzle-1 (Y₁)",
        "question": "그런데 왜 이런 현상이 발생하나?",
        "they_say_i_say": "But",
        "template": "그러나 [specific phenomenon/statistic]을 보라. [X]가 맞다면, 왜 [Y₁]가 발생하는가?"
    },
    "P3_PUZZLE_2": {
        "emoji": "🧩🧩",
        "role": "Puzzle-2 (Y₂)",
        "question": "게다가 이것은 또 어떻게 설명하나?",
        "they_say_i_say": "And Yet",
        "template": "더 놀라운 점: [contrasting case or deeper paradox]. [Y₂]는 [X]와 더욱 모순된다."
    },
    "P4_GAP": {
        "emoji": "😰",
        "role": "Gap (A,B 한계)",
        "question": "기존 이론 A, B는 왜 부족한가?",
        "they_say_i_say": "They Say But Can't Explain",
        "template": "[Theory A]는 [limitation A]. [Theory B]는 [limitation B]. 둘 다 [Y₁, Y₂]를 설명하지 못한다."
    },
    "P5_NEW_LENS": {
        "emoji": "🔎",
        "role": "New Lens (Z)",
        "question": "나의 새 렌즈는 무엇인가?",
        "they_say_i_say": "I Say",
        "template": "우리는 [Z 개념]을 제안한다. [Mechanism 설명]. 이 렌즈로 [Y₁, Y₂]가 모두 설명된다."
    },
    "P6_CONTRIBUTIONS": {
        "emoji": "😉",
        "role": "Contributions",
        "question": "학계에 어떤 기여를 하는가?",
        "they_say_i_say": "So What?",
        "template": "(1) [Theory A]에 [contribution 1], (2) [Theory B]에 [contribution 2], (3) [practical implication]."
    },
    "P7_ROADMAP": {
        "emoji": "🗺️",
        "role": "Roadmap",
        "question": "독자가 따라갈 여정은?",
        "they_say_i_say": "Who Cares?",
        "template": "Section 2에서 [이론], Section 3에서 [실증], Section 4에서 [함의]를 다룬다."
    }
}
```

### 2. 세 논문(P1, P2, P3) 각각의 컨텐츠 딕셔너리 추가

```python
PAPER_CONFIGS = {
    "P1_USHAPE": {
        "title": "Why Do Intermediate Visions Die?",
        "scott_trigger": "More options ≠ always better. 극단만이 살아남는다.",
        "paragraphs": {
            "P1_GOSPEL": {
                "content": "실물옵션 이론에 따르면 불확실성 하에서 유연성(flexibility)은 가치 있다. Trigeorgis & Reuer (2017)는 '옵션 보유가 많을수록 좋다'고 주장하며...",
                "citations": ["Trigeorgis & Reuer, 2017", "Kogut & Kulatilaka, 1994"]
            },
            "P2_PUZZLE_1": {
                "content": "그러나 모빌리티 벤처 데이터는 다른 이야기를 한다. Vagueness가 중간 수준인 벤처의 생존율이 가장 낮다 — 5.3%의 U자형 딜레마.",
                "statistic": "5.3% survival rate at intermediate vagueness"
            },
            # ... 나머지 문단
        }
    },
    "P2_TRAP": {
        "title": "Why Does Success Become a Trap?",
        "scott_trigger": "Strong tech, stronger trap. 성공이 옵션을 죽인다.",
        # ... P2 내용
    },
    "P3_OPTIMAL": {
        "title": "How Many Options Should You Hold?",
        "scott_trigger": "Newsvendor of options. FOMO도 조건부로 합리적이다.",
        # ... P3 내용
    }
}
```

### 3. generate_section() 함수 수정

```python
def generate_section(paper_id: str = "P1_USHAPE") -> str:
    """
    Generate 7-paragraph introduction following X→Y→Z→X' structure.
    
    Args:
        paper_id: One of "P1_USHAPE", "P2_TRAP", "P3_OPTIMAL"
    """
    config = PAPER_CONFIGS[paper_id]
    structure = INTRO_STRUCTURE
    
    # Load empirical results
    h1_results = load_h1_results()
    h2_results = load_h2_results()
    
    # Build 7 paragraphs
    paragraphs = []
    for para_id, para_config in structure.items():
        emoji = para_config["emoji"]
        role = para_config["role"]
        content = config["paragraphs"][para_id]["content"]
        
        # Inject statistics where applicable
        if para_id == "P2_PUZZLE_1" and paper_id == "P1_USHAPE":
            content = content.format(survival_rate=h1_results.get("survival_rate", "5.3%"))
        
        paragraphs.append(f"### {emoji} {role}\n\n{content}\n")
    
    # Combine into markdown
    content = f"""# 1. Introduction

**Scott Trigger:** _{config['scott_trigger']}_

{''.join(paragraphs)}

---
**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})
**Commander:** {COMMANDER} 🐢
**Paper Module:** {paper_id}
"""
    return content
```

### 4. META_PROMPT 업데이트

```python
META_PROMPT = """
You are 정운 (Jeong-un) 🐢, the Door Opener of the 전라좌수군 (Jeonla Naval Fleet).

## 7-PARAGRAPH STRUCTURE (X→Y→Z→X')

1. 📿 **Gospel (X)**: State the field's established belief
   - Template: "[Field]의 중심 아이디어 중 [X]만큼 확고한 것은 없다..."
   - Cite 2-3 foundational papers
   
2. 🧩 **Puzzle-1 (Y₁)**: Present first contradiction
   - Template: "그러나 [specific data/case]는 다른 이야기를 한다..."
   - Include concrete statistic
   
3. 🧩🧩 **Puzzle-2 (Y₂)**: Deepen the paradox
   - Template: "더 놀라운 점: [contrasting case]..."
   - Show the puzzle is not a fluke
   
4. 😰 **Gap**: Explain why existing theories fail
   - Template: "[Theory A]는 [limitation]. [Theory B]도 [limitation]..."
   - Name specific theories and their specific failures
   
5. 🔎 **New Lens (Z)**: Propose your mechanism
   - Template: "우리는 [concept]을 제안한다..."
   - Explain causal mechanism clearly
   
6. 😉 **Contributions**: List 3 scholarly contributions
   - (1) Theory A extension, (2) Theory B extension, (3) Practical design rule
   
7. 🗺️ **Roadmap**: Preview paper structure
   - Link to 권준(이론), 김완(실증), 어영담(함의)

## STYLE GUIDELINES
- Active voice: "We find" not "It is found"
- Numbers in parentheses: (β = X.XX, p < 0.001)
- Hook with case contrast, not abstract concepts
- One paragraph per structural element
- Each paragraph starts with its emoji

## JEONLA NAVAL FLEET PHILOSOPHY
정운 opens the door → 권준 builds structure → 김완 proves righteousness → 어영담 closes with wisdom
"""
```

### 5. Abstract 생성 함수 추가

```python
def generate_abstract(paper_id: str) -> str:
    """
    Generate abstract by synthesizing first sentence of each paragraph.
    
    Abstract formula: 
    📿 + 🧩 + 🧩🧩 + 😰 + 🔎 + 😉 + 🗺️ (7 sentences synthesized to 150-200 words)
    """
    config = PAPER_CONFIGS[paper_id]
    
    # Extract first sentence of each paragraph
    first_sentences = []
    for para_id in INTRO_STRUCTURE.keys():
        content = config["paragraphs"][para_id]["content"]
        first_sentence = content.split('.')[0] + '.'
        first_sentences.append(first_sentence)
    
    # Synthesize into abstract
    abstract_template = """
{gospel} **{puzzle1}** {puzzle2} {gap} **{new_lens}** {contributions} **{roadmap}**
"""
    
    abstract = abstract_template.format(
        gospel=first_sentences[0],
        puzzle1=first_sentences[1],
        puzzle2=first_sentences[2],
        gap=first_sentences[3],
        new_lens=first_sentences[4],
        contributions=first_sentences[5],
        roadmap=first_sentences[6]
    )
    
    return abstract.strip()
```

### 6. CLI 인터페이스 추가

```python
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Introduction (Phase 1)")
    parser.add_argument(
        "--paper", 
        choices=["P1_USHAPE", "P2_TRAP", "P3_OPTIMAL", "all"],
        default="P1_USHAPE",
        help="Which paper module to generate"
    )
    parser.add_argument(
        "--abstract-only",
        action="store_true",
        help="Generate only the abstract"
    )
    args = parser.parse_args()
    
    papers = ["P1_USHAPE", "P2_TRAP", "P3_OPTIMAL"] if args.paper == "all" else [args.paper]
    
    for paper_id in papers:
        if args.abstract_only:
            content = generate_abstract(paper_id)
            output_filename = f"00_Abstract_{paper_id}.md"
        else:
            content = generate_section(paper_id)
            output_filename = f"01_Introduction_{paper_id}.md"
        
        output_path = OUTPUT_DIR / output_filename
        output_path.write_text(content)
        print(f"✅ Generated: {output_path}")
```

## 실행 예시

```bash
# P1 서론만 생성
python generate_01_introduction.py --paper P1_USHAPE

# P2 abstract만 생성
python generate_01_introduction.py --paper P2_TRAP --abstract-only

# 모든 논문 서론 생성
python generate_01_introduction.py --paper all
```

## 추가 요청사항

1. **Davis 흥미로움 지수 태그** 추가
   - 각 논문이 어떤 "흥미로움 유형"인지 메타데이터로 기록
   - P1: "Complexity in Simple" (U-shape reveals hidden heterogeneity)
   - P2: "Unobserved Bad" (Success is actually harmful)
   - P3: "Order from Chaos" (FOMO has rational structure)

2. **Scott/Charlie 체크포인트** 추가
   - 각 문단 끝에 "Scott이 물을 질문", "Charlie가 확인할 사항" 주석 추가

3. **테스트 함수** 추가
   ```python
   def test_paragraph_count():
       """Ensure exactly 7 paragraphs in introduction"""
       for paper_id in PAPER_CONFIGS:
           content = generate_section(paper_id)
           para_count = content.count("### ")
           assert para_count == 7, f"{paper_id} has {para_count} paragraphs, expected 7"
   ```

## 파일 위치
- 수정 대상: `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/generate_01_introduction.py`
- 참조 문서: `/Users/hyunjimoon/tolzul/Space/Library/1논문용/📝intro_writing_guide.md`
