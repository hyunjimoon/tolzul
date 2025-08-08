# Lecture 11: Value Chain Resilience - Supply Chain Risk Management

**Date:** August 7  
**Duration:** 1.5 hours  
**Instructor:** Prof. Vivek Farias

----
# manual note
[[1_🐢acculturate-evaluate/zoo/daily/2025-08-07|25-08-07-08]]

resilience: 
- proactive: where does risk lie?? TTR, TTS, PI; TTS< TTS
- proactive: invest in production and product flexibility where it matters
- reactive: sense irregularities, leverage the investments in flexibility. culture

economic losses (328), insured losses (137); mademade losses (10b)

why is increasing?
- fraction of what's insured vs not is static; climate; 
- economic growth (normalized inflation)
- risks interact
- complexity in goods and services


think about the product, demand better things; complex, nature 

increasing econ act, env, global 
culture e.g. toyota (don't need buffer to remove the stone)
zodwa - mutual inclusive; design product

underestimate negative tail risk and overestimate positive tail risk

ford has four tier supply chain, 
50 manufacturing plants, 55k ; 6m vehicles

time to survive exceed time to recovery then order by probability of impact


A has 250, B has 200, C has 150,100; 
1 gets 150, 2 gets 150, 

as a function of time to recovery, what's the potential impact -> ⭐️assume recovery

### Supply Chain Impact Summary Table

| **Aspect**                     | **Details**                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Products**                   | - Product 1: Requires 1 red + 1 green component, demand = 150 units/week, margin = 3/unit.<br>−Product2:Requires1redcomponent,demand=200units/week,margin=3/unit.<br>- Product 2: Requires 1 red component, demand = 200 units/week, margin = 3/unit.<br>−Product2:Requires1redcomponent,demand=200units/week,margin=1/unit.- Product 3: Requires 1 green component, demand = 200 units/week, margin = $1/unit. |
| **Suppliers**                  | - **Supplier A:** Produces 250 green components/week.- **Supplier B:** Produces 200 red components/week.- **Supplier C:** Produces 150 red + 100 green components/week.                                                                                                                                                                                                                                         |
| **Normal Allocation**          | - **Supplier A:** 150 green to Product 1, 100 green to Product 3.- **Supplier B:** 150 red to Product 1, 50 red to Product 2.- **Supplier C:** 100 red to Product 2, 100 green to Product 3.                                                                                                                                                                                                                    |
| **Safety Stock**               | - Each supplier holds one week of safety stock: Supplier A: 250 green parts. Supplier B: 200 red parts. Supplier C: 150 red + 100 green parts.                                                                                                                                                                                                                                                                  |
| **Scenario: Supplier C Fails** | - Product 2 loses 150 red units.- Product 3 loses 100 green units.                                                                                                                                                                                                                                                                                                                                              |
| **Short-Term Mitigation**      | - **Product 2**: Supplier B compensates with safety stock (150 red/week).<br>- **Product 3**: Supplier A compensates with safety stock (100 green/week).                                                                                                                                                                                                                                                        |
| **Safety Stock Duration**      | - **Product 2**: Supplier B’s safety stock lasts **1.33 weeks** (200 ÷ 150).<br>- **Product 3**: Supplier A’s safety stock lasts **2.5 weeks** (250 ÷ 100).                                                                                                                                                                                                                                                     |
| **Long-Term Impact**           | - After 1.33 weeks: **Product 2 loses 150 units/week** (150/weekloss).<br>−After2.5weeks:∗∗Product3loses100units/week∗∗(150/week loss).<br>- After 2.5 weeks: **Product 3 loses 100 units/week** (150/weekloss).<br>−After2.5weeks:∗∗Product3loses100units/week∗∗(100/week loss).- Total loss after 2.5 weeks: **$250/week**.                                                                                   |
| **Graph Description**          | - Loss impact starts at **week 1.33** with a slope of **150/week∗∗.<br>−At∗∗week2.5∗∗,slopeincreasesto∗∗150/week**.<br>- At **week 2.5**, slope increases to **150/week∗∗.<br>−At∗∗week2.5∗∗,slopeincreasesto∗∗250/week** due to additional losses from Product 3.                                                                                                                                              |

This table summarizes the supply chain structure, mitigation strategies, and the financial impact of Supplier C's failure over time.



who are we spending lots of money on (supplies on different parts; engine, road); high spend for supplier ⭐️HIGH IMPACT, NO MONEY⭐️

ppl who spend lots of money are the one who values this. 

using data from 2015, value supplier based on risk (as opposed to how much money)

find alternative supplier and vertically integrate (buy)

⭐️Using 2015 data, suppliers were evaluated based on **risk and impact**, not spending. This revealed that **low-cost suppliers**, like semiconductor makers, can have a **high supply chain impact**, highlighting overlooked vulnerabilities.⭐️

change product design so that it lowers dependency
dual sourcing

TTS < TTR is a problem; invest in flexibility where it matters

understanding impact as time to recovery, 

---
## Learning Objectives
- Understand supply chain risk types and their impacts
- Analyze resilience strategies and their effectiveness
- Evaluate proactive vs. reactive risk management approaches
- Apply risk management frameworks to real-world scenarios

## Case Studies
- **Primary Case:** [[Lec11_Nokias_Supply_Chain_Management.pdf]]

## Required Readings
- **HBR Article:** [From Superstorms to Factory Fires: Managing Unpredictable Supply-Chain Disruptions](https://hbr.org/2014/01/from-superstorms-to-factory-fires-managing-unpredictable-supply-chain-disruptions)

### HBR Article Key Points:
Traditional methods of managing supply chain risk require estimations of how likely a disruption is to occur. For fairly common risks—poor supplier performance, forecast errors, transportation breakdowns—the traditional methods work quite well. But it's a different story for rare, high-impact events such as megadisasters, pandemics, and political upheavals. These risks are hard to quantify using traditional models, and as a result, many companies do not adequately prepare for them, which can have calamitous consequences when catastrophes do strike. A new model allows managers to quantify the impact of a supply chain disruption on a company's operational and financial performance, rather than focusing on the cause or likelihood of the disruption.

**Key Insights:**
- **Traditional Risk Management:** Works well for predictable, common risks
- **Black Swan Events:** Rare, high-impact events are harder to quantify
- **New Approach:** Focus on impact rather than probability
- **Risk Agnostic:** Mitigation strategies effective regardless of disruption cause

## Key Concepts

### Types of Supply Chain Risks

#### Predictable Risks
- **Supplier Performance:** Quality issues, delivery delays
- **Demand Variability:** Forecast errors, seasonal fluctuations
- **Transportation:** Route disruptions, carrier problems
- **Operational:** Equipment failures, capacity constraints

#### Unpredictable Risks (Black Swan Events)
- **Natural Disasters:** Earthquakes, tsunamis, hurricanes
- **Pandemics:** Global health crises (COVID-19 example)
- **Political Upheaval:** Wars, trade disputes, regulations
- **Cyber Attacks:** IT system disruptions, data breaches
- **Terrorism:** Security threats, facility attacks

### Risk Management Frameworks

#### Traditional Approach
1. **Risk Identification:** Catalog potential disruptions
2. **Probability Assessment:** Estimate likelihood of occurrence
3. **Impact Analysis:** Quantify potential damage
4. **Risk Prioritization:** Focus on high probability × high impact
5. **Mitigation Planning:** Develop specific countermeasures

#### New Impact-Based Approach
1. **Impact Assessment:** Focus on operational/financial consequences
2. **Vulnerability Analysis:** Identify critical nodes and links
3. **Resilience Building:** Develop general preparedness capabilities
4. **Response Planning:** Create flexible, adaptable procedures
5. **Continuous Monitoring:** Real-time risk sensing

### Resilience Strategies

#### Redundancy
- **Supplier Diversification:** Multiple sources for critical components
- **Geographic Distribution:** Spread facilities across regions
- **Inventory Buffers:** Safety stock for critical items
- **Capacity Reserves:** Extra production/distribution capacity

#### Flexibility
- **Supplier Switching:** Ability to change sources quickly
- **Production Flexibility:** Multi-product facilities
- **Transportation Options:** Multiple shipping modes/routes
- **Demand Management:** Price/promotion levers

#### Visibility
- **Supply Chain Mapping:** Know your suppliers' suppliers
- **Real-Time Monitoring:** Track key metrics continuously
- **Early Warning Systems:** Detect problems before they escalate
- **Information Sharing:** Collaborate with partners

#### Collaboration
- **Supplier Partnerships:** Joint risk management planning
- **Industry Cooperation:** Share threat intelligence
- **Government Relations:** Coordinate on infrastructure
- **Customer Communication:** Manage expectations during disruptions

## Nokia vs. Ericsson Case Analysis

### Background: The Phillips Fire
- **Date:** March 2000
- **Location:** Phillips semiconductor plant in Albuquerque, New Mexico
- **Impact:** Critical component supplier for mobile phone industry
- **Affected Companies:** Nokia and Ericsson (among others)

### Nokia's Response Strategy
**Proactive Approach:**
- **Supply Chain Visibility:** Knew their suppliers' suppliers
- **Early Detection:** Identified the problem quickly
- **Rapid Response:** Mobilized alternative sources immediately
- **Supplier Collaboration:** Worked with Phillips on recovery
- **Design Flexibility:** Modified products to use alternative components

**Key Actions:**
1. **Immediate Assessment:** Evaluated impact within hours
2. **Alternative Sourcing:** Activated backup suppliers
3. **Supply Chain Redesign:** Modified component specifications
4. **Capacity Allocation:** Secured priority production slots
5. **Communication:** Coordinated across organization

### Ericsson's Response
**Reactive Approach:**
- **Limited Visibility:** Unaware of supply chain depth
- **Slow Recognition:** Took weeks to understand impact
- **Constrained Options:** Few alternative suppliers identified
- **Design Rigidity:** Products locked into specific components
- **Communication Gaps:** Poor internal coordination

**Consequences:**
- **Production Delays:** Significant lost production
- **Market Share Loss:** Competitors captured sales
- **Financial Impact:** Major revenue and profit losses
- **Strategic Damage:** Mobile phone market position weakened

## Discussion Questions for Class

### Main Question: Nokia's Differentiator
**Prompt:** What was the key differentiator for Nokia in dealing with the Phillips fire?

**Analysis Framework:**
- **Preparation:** Proactive vs. reactive planning
- **Visibility:** Supply chain knowledge and monitoring
- **Relationships:** Supplier partnership strength
- **Flexibility:** Ability to adapt and respond
- **Organization:** Internal coordination capabilities

**Nokia's Advantages:**
1. **Supply Chain Mapping:** Comprehensive understanding of supplier networks
2. **Risk Awareness:** Regular assessment of vulnerabilities
3. **Supplier Relationships:** Strong partnerships enabling collaboration
4. **Design Flexibility:** Products adaptable to component changes
5. **Organizational Agility:** Fast decision-making and execution

## Strategic Implications

### Competitive Advantage through Resilience
- **Risk as Strategy:** Resilience becomes competitive differentiator
- **Investment Justification:** Cost of resilience vs. cost of disruption
- **Capability Building:** Develop organizational risk management skills
- **Supplier Management:** Resilience as supplier selection criterion

### Modern Risk Landscape
- **Increased Complexity:** Global supply chains create more vulnerabilities
- **Speed of Disruption:** Events spread faster in connected world
- **Systemic Risks:** Single points of failure affect multiple industries
- **Technology Dependence:** Cyber risks become more critical

### COVID-19 Lessons
- **Global Interdependence:** Pandemic affects all supply chains
- **Essential vs. Non-Essential:** Different risk profiles
- **Government Intervention:** Policy responses create new risks
- **Demand Shifts:** Massive changes in consumption patterns

## Risk Management Tools

### Supply Chain Mapping
- **Tier 1 Suppliers:** Direct suppliers
- **Tier 2 Suppliers:** Suppliers' suppliers
- **Tier N Suppliers:** Extended network visibility
- **Critical Path Analysis:** Identify bottlenecks and single points of failure

### Scenario Planning
- **Stress Testing:** Model various disruption scenarios
- **Business Continuity Planning:** Procedures for different disruptions
- **War Gaming:** Simulate crisis response
- **Recovery Planning:** Steps to restore normal operations

### Key Performance Indicators
- **Time to Detection:** How quickly risks are identified
- **Time to Response:** Speed of initial reaction
- **Recovery Time:** Duration to restore normal operations
- **Financial Impact:** Revenue/profit effects of disruptions

## Implementation Strategies

### Building Resilient Organizations
1. **Leadership Commitment:** Senior management support for resilience
2. **Cross-Functional Teams:** Break down organizational silos
3. **Culture Development:** Promote risk awareness and preparedness
4. **Training Programs:** Build crisis management capabilities
5. **Regular Exercises:** Practice response procedures

### Technology Enablement
- **IoT Sensors:** Real-time monitoring of operations
- **AI/ML Analytics:** Predictive risk identification
- **Blockchain:** Supply chain transparency and traceability
- **Cloud Computing:** Flexible IT infrastructure

### Supplier Development
- **Risk Assessments:** Evaluate supplier vulnerabilities
- **Capability Building:** Help suppliers improve resilience
- **Joint Planning:** Collaborative risk management
- **Performance Monitoring:** Track supplier risk metrics

## Key Takeaways
- **Strategic Message:** Supply chain visibility and proactive risk management are key competitive advantages; a firm's ability to quickly detect a disruption and mobilize alternative resources is crucial.

- **Preparedness Paradox:** The best time to prepare for a crisis is when you don't have one.

- **Visibility Value:** Knowing your supply chain deeply enables faster, more effective responses.

- **Resilience Investment:** Building resilient capabilities requires investment but provides competitive advantage.

## Preparation for Next Class
- Review revenue management concepts
- Consider dynamic pricing and capacity allocation
- Prepare for discussion of hotel/airline pricing strategies

## Class Discussion Focus
- Compare Nokia and Ericsson responses
- Identify key resilience capabilities
- Discuss modern supply chain risks (cyber, pandemic, trade wars)
- Evaluate cost-benefit of resilience investments

## Teaching Notes
- Emphasize proactive vs. reactive approaches
- Use current examples (COVID-19, cyber attacks, trade wars)
- Connect to previous capacity and network design concepts
- Highlight the strategic importance of operational capabilities
