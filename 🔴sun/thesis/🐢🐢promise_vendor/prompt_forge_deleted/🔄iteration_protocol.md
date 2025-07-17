# 🔄 Prompt Iteration Protocol

## Iteration Cycle Structure

### Phase 1: Deploy Master Prompt
1. Copy current master prompt from `💡master_prompt_template.md`
2. Fill in specific task details
3. Deploy simultaneously to:
   - Claude (via Claude.ai)
   - ChatGPT (via OpenAI)
   - Gemini (via Google AI)

### Phase 2: Cross-Platform Evaluation

Create evaluation matrix for each response:

| Criterion | Claude | ChatGPT | Gemini | Gap Identified |
|-----------|--------|---------|---------|----------------|
| **Consecution** (invisible thread) | [1-5] | [1-5] | [1-5] | |
| **Verb Vitality** | [ratio] | [ratio] | [ratio] | |
| **Gift Economy** (brevity/value) | [1-5] | [1-5] | [1-5] | |
| **Plain Vessel** (clarity) | [1-5] | [1-5] | [1-5] | |
| **Rhythm Variance** | [std dev] | [std dev] | [std dev] | |

### Phase 3: Identify Three Holes

Based on cross-platform analysis, identify gaps where ALL three platforms struggled:

1. **Hole #1**: [Description]
   - Evidence from outputs
   - Root cause hypothesis
   - Prompt revision needed

2. **Hole #2**: [Description]
   - Evidence from outputs
   - Root cause hypothesis
   - Prompt revision needed

3. **Hole #3**: [Description]
   - Evidence from outputs
   - Root cause hypothesis
   - Prompt revision needed

### Phase 4: Refine Master Prompt

Update `💡master_prompt_template.md` addressing identified holes:
- Clarify ambiguous instructions
- Add missing constraints
- Provide better examples
- Adjust voice calibration

## Tracking Template

### Iteration #[X] - [DATE]

**Task Tested**: [Specific entrepreneurial concept/scenario]

**Deployed Prompt**:
```
[Paste exact prompt used]
```

**Platform Responses Summary**:
- Claude: [Key strengths/weaknesses]
- ChatGPT: [Key strengths/weaknesses]  
- Gemini: [Key strengths/weaknesses]

**Three Holes Identified**:
1. [Hole description + fix]
2. [Hole description + fix]
3. [Hole description + fix]

**Master Prompt Updates**:
- [List specific changes made]

**Next Test Focus**: [What aspect to stress-test next iteration]

---

## Meta-Learning Log

Track patterns across iterations:
- Which platforms consistently excel at which aspects?
- What types of prompts create maximum divergence?
- Where do all three converge (suggesting prompt clarity)?
- What Moran principles are hardest to implement via prompt?
