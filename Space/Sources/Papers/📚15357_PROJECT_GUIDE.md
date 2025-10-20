# 📚 15.357 Knowledge Base Organization Guide

## 🎯 Project Overview

We're transforming your 15.357 class materials into a structured knowledge base with:
- **100+ individual paper files** (📜 prefix)
- **1 control tower map** (🗺️ prefix) 
- **Integration** with existing [[1 Innovation]] field structure

## 📁 File Structure

```
tolzul/
├── Space/
│   ├── Sources/
│   │   └── Papers/
│   │       ├── 📜jones01_intro(econ_growth).md ✅ CREATED
│   │       ├── 📜arrow62_welfare(invention).md ✅ CREATED
│   │       ├── 📜azoulay14_matthew(effect).md ✅ CREATED
│   │       ├── 📜TEMPLATE_paper.md ✅ CREATED
│   │       ├── 🗺️15357_course_map.base ✅ CREATED
│   │       └── [~100 more papers to create]
│   └── Dots/
│       └── 창업학계/
│           └── Fields/
│               └── 1 Innovation.md (existing, don't overwrite)
```

## 🏗️ What I've Created So Far

### ✅ Example Paper Files (3)
1. **📜jones01_intro(econ_growth).md** - Module 1 example
2. **📜arrow62_welfare(invention).md** - Module 2 example
3. **📜azoulay14_matthew(effect).md** - Module 3 example

### ✅ Template File
**📜TEMPLATE_paper.md** - Use this for remaining papers

### ✅ Control Tower Map
**🗺️15357_course_map.base** - Master structure in .base syntax

## 📋 How to Complete the Project

### Step 1: Extract URLs from PDF

From your 🐢amoon(innov).pdf, extract the marginnote3app:// URLs for each paper.

Example format from PDF:
```
marginnote3app://note/8B0B89F7-321D-4EB5-9D53-A30DD308F67A
```

### Step 2: Create Paper Files

For each paper in the syllabus, use the template:

#### Module 1: Ideas, Innovation, Economic Growth
- [ ] 📜jones01_intro(econ_growth).md ✅ DONE
- [ ] 📜varian04_review(mokyr).md
- [ ] 📜nelson62_link(science_invention).md
- [ ] 📜romer18_progress.md

#### Module 2: Nature of Ideas and Innovation  
- [ ] 📜arrow62_welfare(invention).md ✅ DONE
- [ ] 📜jones99_growth(scale).md
- [ ] 📜jones09_burden(knowledge).md
- [ ] 📜wuchty07_teams.md
- [ ] 📜jones10_age(invention).md
- [ ] 📜bresnahan95_gpt.md
- [ ] 📜bloom20_ideas(harder).md

#### Module 3: Open Science
- [ ] 📜aghion08_academic(freedom).md
- [ ] 📜azoulay14_matthew(effect).md ✅ DONE
- [ ] 📜azoulay19_funeral(science).md
- [ ] 📜bikard18_made(academia).md
- [ ] 📜dasgupta94_new(economics).md
- [ ] 📜fleming04_science(map).md
- [ ] 📜merton57_priority.md
- [ ] 📜merton68_matthew.md
- [ ] 📜murray16_mice(academics).md
- [ ] 📜stern04_pay(scientists).md
- [ ] 📜myers20_elasticity(science).md
- [ ] 📜furman11_shoulders(giants).md

#### Module 4: Supply of Innovators
- [ ] 📜bell19_inventor(america).md
- [ ] 📜shu15_finance(careers).md
- [ ] 📜borjas12_soviet(collapse).md
- [ ] 📜moser14_emigres.md
- [ ] 📜deming20_earnings(stem).md
- [ ] 📜azoulay21_yellow(berets).md
- [ ] 📜agarwal20_invisible(geniuses).md
- [ ] 📜ahmadpoor19_teams.md
- [ ] 📜biasi22_education(innovation).md

#### Module 5: US Patent System
- [ ] 📜fox89_shark(protector).md
- [ ] 📜hall01_patent(paradox).md
- [ ] 📜feng20_trolls.md
- [ ] 📜merges99_patents(breakfast).md
- [ ] 📜derassenfosse18_notice(failure).md
- [ ] 📜hemphill11_generics.md

#### Module 6: Innovation & Climate Change
- [ ] [TBA - see syllabus]

#### Module 7: Measuring Innovation
- [ ] 📜griliches79_issues.md
- [ ] 📜kuhn20_citations(reexamined).md
- [ ] 📜ahmadpoor17_dual(frontier).md
- [ ] 📜arts21_nlp.md
- [ ] 📜higham21_quality.md
- [ ] 📜li15_peer(review).md

#### Module 8: Incentives - Contracts
- [ ] 📜aghion94_management.md
- [ ] 📜azoulay11_incentives(creativity).md
- [ ] 📜lerner10_contracts.md
- [ ] 📜manso11_motivating.md

#### Module 9: Incentives - Market Rewards
- [ ] 📜azoulay21_grant(funding).md
- [ ] 📜brunt12_prizes.md
- [ ] 📜budish16_patents(research).md
- [ ] 📜budish15_underinvest.md
- [ ] 📜gallini02_ip(incentives).md
- [ ] 📜lemley05_probabilistic(patents).md
- [ ] 📜moser13_patents(history).md
- [ ] 📜sampat19_patents(follow-on).md
- [ ] 📜kogan17_value.md
- [ ] 📜scotchmer91_shoulders(giants).md
- [ ] 📜wright83_invention(incentives).md

#### Module 10: [Guest Lecture - Heidi Williams]
- [ ] [TBA]

#### Module 11: Returns to R&D
- [ ] 📜jones21_social(returns).md
- [ ] 📜bloom13_spillovers.md
- [ ] 📜iaria18_collapse.md
- [ ] 📜azoulay19_nih(patents).md
- [ ] 📜howell17_grants.md
- [ ] 📜myers22_doe(spillovers).md

#### Module 12: Measuring Entrepreneurship
- [ ] 📜decker14_role.md
- [ ] 📜glaeser15_urban(growth).md
- [ ] 📜guzman20_state.md
- [ ] 📜haltiwanger13_creates(jobs).md
- [ ] 📜samila11_vc.md
- [ ] 📜moretti21_clusters.md

### Step 3: Fill in Content

For each paper file:

1. **Copy template** to new file with proper name
2. **Update YAML frontmatter**:
   ```yaml
   author_ids: [from syllabus]
   year: [from syllabus]
   module: "[from list above]"
   url: "[from your PDF]"
   ```

3. **Add content from two sources**:
   - **scott23🛠️_econ_idea_innov_ent.pdf** - For detailed notes, critical insights
   - **23_15357.md** - For quick reference table

4. **Key sections to include**:
   - Summary (2-3 sentences)
   - Research question
   - Key concepts
   - Main results
   - Critical insights (from class notes)
   - Methodology
   - Connections to other papers
   - Application to course framework

### Step 4: Update Control Tower

Once you have many paper files created, enhance the control tower map:

1. **Open** 🗺️15357_course_map.base
2. **Add** specific connections between papers
3. **Fill in** any missing papers in the .base structure
4. **Link** to [[1 Innovation]] field themes

## 🔗 Integration with Existing System

### Don't Overwrite These Files:
- ✅ [[1 Innovation]].md - Add to it, don't replace
- ✅ [[📜gans20_choose(tech)]].md - Already exists, good example

### Do Connect To:
- [[1 Innovation]] field themes
- [[Papers]] collection
- [[Fields]] collection
- [[23_15357]] class notes

## 💡 Pro Tips

### From Your Examples:

1. **Use excalidraw diagrams** when helpful (like in gans20 file)
2. **Add dated entries** for your evolving understanding
3. **Include table summaries** for complex papers
4. **Cross-reference liberally** using [[wikilinks]]

### From Course Notes:

1. **Bold key concepts** for scannability  
2. **Use > blockquotes** for critical insights
3. **Add emojis** for quick visual scanning (🧍‍♀️ individual, 🌏 environment, 🧭 process, 🗺️ framework)
4. **Include formulas** in LaTeX when relevant

### From Pierre's Philosophy:

1. Focus on **identification strategy** 
2. Highlight **data assembly approach**
3. Note **internal vs external validity**
4. Emphasize **within-unit comparisons**

## 🎓 Conceptual Framework

Every paper should connect to the ideas production function:

```
A' = f(L_A, K_A, A; Z_A, δ)
```

Ask for each paper:
- Which component does it address?
- What does it tell us about the production function?
- How does it relate to the core questions?

## 🚀 Quick Start Workflow

For each paper:

1. **Find it** in your PDF mind map
2. **Copy URL** from marginnote link
3. **Copy template** → rename with paper naming convention
4. **Fill YAML** (authors, year, module, URL)
5. **Add summary** from your two source documents
6. **Extract critical insights** from scott23🛠️ PDF
7. **Connect** to other papers and course framework
8. **Save** and move to next paper

## 📊 Progress Tracking

Total papers: ~110
- ✅ Complete: 3
- 🏗️ In progress: 0  
- 📝 To do: ~107

**Estimated time**: 20-30 minutes per paper × 107 = ~40-50 hours

**Suggestion**: Do 3-5 papers per day = done in 3-4 weeks

## ❓ Questions?

If you need help:
1. Look at the 3 example files I created
2. Check the template
3. Refer to the control tower map for structure
4. Follow the patterns in your existing [[📜gans20_choose(tech)]] file

---

You've got this! 화이팅! 💪

The hardest part (structure design) is done. Now it's systematic execution.
