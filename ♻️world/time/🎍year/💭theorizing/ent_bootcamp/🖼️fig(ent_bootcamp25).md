# Entrepreneurship Lecture-to-Poster System

## Overview

Transform a 3-hour entrepreneurship lecture into a comprehensive visual poster that captures key insights, frameworks, and actionable takeaways.

## Input

- Transcript, notes, or recording of a 3-hour entrepreneurship lecture
- Any slides, diagrams, or visual materials referenced

## Output

- One integrated poster (SVG format) synthesizing the entire lecture

## Analysis Process

### Step 1: Extract Five Core Components

#### 1. **Key Concepts Q&A**

Create a table with these columns:

- **Topic**: Main subject area (e.g., "Market Validation", "Business Models")
- **Core Question**: What problem or question does this address?
- **Key Insight**: The main takeaway or answer
- **Example**: Real-world example or case study mentioned

Keep entries concise (1-2 sentences each). Aim for 6-10 rows covering the lecture's main topics.

#### 2. **Framework Comparison**

If the lecture presents any frameworks or models, create a simple comparison table:

- **Framework Name**: What it's called
- **When to Use**: Best application scenario
- **Key Strength**: What it does well
- **Key Limitation**: Where it falls short

If no frameworks are explicitly compared, skip this component.

#### 3. **Action Items**

List the top 3-5 practical actions entrepreneurs should take based on the lecture:

- **Action**: What to do
- **Why**: The benefit or purpose
- **How to Start**: First concrete step

#### 4. **Problem-Solution Visual**

Identify the central entrepreneurial challenge discussed and its proposed solution:

- **Problem** (Purple box 💜): The main obstacle or challenge entrepreneurs face
- **Solution** (Green box 💚): The recommended approach or methodology
- Connect with an arrow showing the transformation

#### 5. **Key Tradeoff**

Identify one major decision or tradeoff entrepreneurs must navigate:

- Show as a balance or choice between two options
- Include what you gain and what you sacrifice with each choice

### Step 2: Create the Integrated Poster

Design an SVG poster (1200x900px recommended) with these sections:

```
+--------------------------------------------------+
|            LECTURE TITLE & SPEAKER               |
+--------------------------------------------------+
|                                                  |
|  KEY CONCEPTS Q&A        |   PROBLEM→SOLUTION    |
|  [Table with 6-10 rows]  |   [Visual diagram]    |
|                          |                       |
+--------------------------|----------------------+
|                                                  |
|  ACTION ITEMS            |   KEY TRADEOFF        |
|  [List of 3-5 items]     |   [Balance visual]    |
|                          |                       |
+--------------------------------------------------+
|              3 KEY TAKEAWAYS (Footer)            |
+--------------------------------------------------+
```

## Simplified Symbol Guide

Use these symbols to highlight different types of content:

- 🎯 **Goal/Objective**: What entrepreneurs aim to achieve
- 🛠️ **Tool/Method**: Practical techniques or frameworks
- 💡 **Insight**: Key realizations or "aha" moments
- ⚠️ **Warning**: Common pitfalls to avoid
- 📊 **Data/Evidence**: Supporting facts or statistics

## Design Guidelines

1. **Colors**:
    
    - Headers: Dark blue (#1e3a8a)
    - Problem areas: Light purple (#e9d5ff)
    - Solutions: Light green (#d1fae5)
    - Neutral content: Light gray (#f3f4f6)
2. **Typography**:
    
    - Title: 24pt bold
    - Section headers: 18pt bold
    - Body text: 14pt regular
    - Use Arial or Helvetica for clarity
3. **Layout**:
    
    - Clear section boundaries with rounded rectangles
    - Adequate whitespace between sections
    - Consistent alignment and spacing

## Example Components

### Sample Q&A Entry:

|Topic|Core Question|Key Insight|Example|
|---|---|---|---|
|Customer Discovery|How do you validate a business idea?|Talk to 100 potential customers before building anything|Airbnb founders went door-to-door in NYC|

### Sample Action Item:

- **Action**: Conduct 20 customer interviews this week
- **Why**: Validate assumptions before investing in development
- **How to Start**: Email 5 contacts today with a simple question about their biggest challenge

### Sample Tradeoff:

```
Fast Launch ←→ Perfect Product
Gain: Early feedback    Gain: Better first impression
Lose: Polish           Lose: Time to market
```

## Final Checklist

Before delivering the poster, ensure:

- [ ] All five components are clearly visible
- [ ] Text is readable at normal zoom (14pt minimum)
- [ ] Visual hierarchy guides the eye through content
- [ ] Key takeaways are immediately apparent
- [ ] Examples make concepts concrete
- [ ] Design is clean and professional

## Delivery Format

Provide the final poster as an SVG file that includes:

1. All extracted content organized visually
2. Clear section divisions
3. Appropriate use of color and typography
4. A footer with 3 key takeaways from the entire lecture

The poster should work as a standalone reference that someone could understand without having attended the lecture.