# Lecture 3: Capacity Analysis 2 - Unpredictable Variability (Uber)

**Date:** July 24  
**Duration:** 1.5 hours  
**Instructor:** Prof. Vivek Farias

# manual note
uber uncertainty is harder than jetblue (predictable)

increase load from 58 flights to 75 flights


|            | baseline | expansion w/o earhardt | expansion w earhardt |
| ---------- | -------- | ---------------------- | -------------------- |
| throughput | 2.5      | 3.25                   |                      |
|            |          |                        |                      |
icing, delay more than doubles (1.7hrs to 3.6hrs)

should they be investing extra deicing (from brand perspective ), cons: other companies should also deice and we're running on tight margin

we should be looking at

sevend second macdonlad's market share 

i know the cost, need to know the upside ; 
instead of looking at the upside, look at downside of not doing (source of upside and downside?? )

mechanism is delay - crew times out (time of customers)

some idea raised, delay loose the customer (life time value)

bureau of labor statistics ($37) horrible lower dollar
investment of 2.14 * 78 * 100 * 23* 37 = $14m

⭐️customer surplus (value generating for customer) -> how much value can we extract from ?

as jetblue has pricing power from route types and timing, 50% can be 

better product -> price more aggressively

goal: nonlinear effect of demand mean on dealy and how think about capacity investment frontier (lowering delay increases )

Q. take value from the mess what you created??
where the market is delay of 3.5hrs?
relative to what the standards might be (typically 3.5hr delay and saving is giving incremental value; expectations are built in)

instead of cost, investment returning value 

increased the delay for customers. impact??
uber 8->24 min
lyft 8->24 min
uber cancelation from 8% to 28% VS lyft from 6.4% to 30%


process utilitization 

⭐️FORCED IDELNESS: i can only work on it only if there's demand

variability is from 

somebody in my 

in any service, BOTH sides (queue and server) are variable is picking somebody up at A and 

you can't inventory your work 

🙋‍♀️what can't be inventoried in entreprenuership?

increase in price would make utilization goes down. rho increase
lambda/ (N mu)

share but doubling up

create two tiers
- managing rho (couple servies)

don't need to increase utilitization too much to lower delay
how much should i change prices (should i do surges??) NO

tiny change in utilitization, decrease 
W = 1/lambda * rho^sqrt(N)/(1-rho) * (Ca^2 + C_s^2) /2

|                             | burger                    | uber          |
| --------------------------- | ------------------------- | ------------- |
| rho utiliziation            |                           | 1. pooling    |
| Ca                          |                           | 2. scheduling |
| Cs (variability of service) | standardization, robotics | traffic       |
time is money and variability and utilizations are key drivers with highly nonlinear impacts on delay

⚒️tools: process flow, buildup , queing (unpredictabel )



---

## Learning Objectives
- Understand capacity management for unpredictable demand patterns
- Analyze dynamic pricing as a demand-supply balancing mechanism
- Evaluate two-sided market dynamics and platform operations
- Apply economic principles to operational decision-making

## Case Studies
- **Primary Case:** [[Lec3_The_Effects_of_Uber_s_Surge_Pricing__A_Case_Study.pdf]] (SKIM)

## Optional Readings
- [WCVB Article: Did Uber Price Gouge During Winter Storms?](https://www.wcvb.com/article/did-uber-price-gouge-passengers-during-winter-storms/20649129#)
  - **Key Points:**
    - Public backlash against surge pricing during emergencies
    - Regulatory concerns about price gouging
    - Consumer perception vs. economic efficiency arguments
    - Questions about corporate social responsibility during crises

## Key Concepts

### Unpredictable Variability Characteristics
- **Random demand spikes:** Weather events, emergencies, special events
- **Supply volatility:** Driver availability fluctuations
- **Information asymmetry:** Real-time demand/supply imbalances
- **Network effects:** Geographic concentration of demand

### Two-Sided Market Dynamics
- **Platform role:** Connecting riders (demand) and drivers (supply)
- **Network externalities:** Value increases with network size
- **Chicken-and-egg problem:** Need both sides for market function
- **Platform governance:** Setting rules and incentives

### Dynamic Pricing Theory
- **Price as signal:** Information mechanism for market participants
- **Demand elasticity:** Price sensitivity of customers
- **Supply elasticity:** Driver response to price incentives
- **Market clearing:** Price adjustment to balance supply and demand

## Case Analysis Framework

### Uber's Business Model
- **Platform strategy:** Asset-light, network-based business
- **Value proposition:** 
  - For riders: Convenience, reliability, transparency
  - For drivers: Flexible income opportunity
- **Operational characteristics:** Real-time matching, dynamic pricing

### Surge Pricing Mechanism
- **Algorithm:** Automatic price multiplication based on demand/supply ratio
- **Purpose:** 
  1. **Demand throttling:** Reduce quantity demanded
  2. **Supply activation:** Incentivize more drivers to come online
  3. **Market clearing:** Achieve equilibrium faster

### Effectiveness Analysis
According to the case study, surge pricing delivers:
- **Higher completion rates:** More rides successfully matched
- **Lower wait times:** Faster service despite high demand
- **Improved reliability:** More predictable service availability
- **Driver utilization:** Better income opportunities during peak periods

## Discussion Questions for Class

1. **Market Dynamics:** How does Uber's platform create value for both riders and drivers? What are the key operational challenges?

2. **Surge Pricing Logic:** Why does dynamic pricing improve system performance? What are the mechanisms through which it works?

3. **Alternative Approaches:** What would happen if Uber used:
   - Fixed pricing during all periods
   - First-come-first-served queuing
   - Non-monetary rationing mechanisms

4. **Stakeholder Perspectives:** How do different stakeholders view surge pricing?
   - **Riders:** Fairness vs. availability trade-off
   - **Drivers:** Income opportunity vs. predictability
   - **Regulators:** Consumer protection vs. market efficiency
   - **Uber:** Revenue optimization vs. reputation management

## Quantitative Analysis

### Supply-Demand Matching
- **Demand function:** Q_d = f(Price, Weather, Events, Time)
- **Supply function:** Q_s = g(Price, Driver_availability, Location)
- **Equilibrium condition:** Q_d = Q_s
- **Surge multiplier:** Price adjustment mechanism

### Performance Metrics
- **Completion rate:** Successful matches / Total requests
- **Wait time:** Time from request to pickup
- **Utilization rate:** Driver active time / Total online time
- **Geographic coverage:** Service availability across areas

## Broader Strategic Implications

### Platform Competition
- **Network effects:** Winner-take-all dynamics
- **Multi-homing:** Users participating in multiple platforms
- **Differentiation strategies:** Service quality vs. price competition

### Regulatory Challenges
- **Price regulation:** Caps on surge pricing
- **Labor classification:** Employee vs. contractor status
- **Market entry barriers:** Licensing and regulatory approval

### Operational Excellence
- **Technology infrastructure:** Real-time processing capabilities
- **Algorithm optimization:** Continuous improvement of matching
- **Data analytics:** Demand forecasting and supply planning

## 🔺 The Six Questions Framework

```
        1. Capabilities?          2. Customer?
              🟢                      🟣
       Platform technology      Riders + Drivers
       Network algorithms       Two-sided market
                \                    /
                 \                  /
                  \                /
        5. Coordinate? ←→ 6. Compel?
                  /                \
                 /                  \
                /                    \
              🟠                      🔴
       Market efficiency        Reliable matches
       Asset-light scale        Transparent pricing
```

### Uber Analysis
1. **🟢 Capabilities:** Real-time matching algorithms, mobile platform, data analytics
2. **🟣 Customer:** Urban riders (convenience) + Drivers (flexible income)
3. **🟠 Goals:** Maximize matches, minimize wait times, grow network
4. **🔴 Offering:** On-demand rides with price transparency and reliability
5. **Coordinate:** Technology enables massive scale without owning vehicles
6. **Compel:** Better availability than taxis, income flexibility for drivers

### Dynamic Pricing Mechanism
- **Problem:** Unpredictable demand spikes (weather, events)
- **Solution:** Surge pricing as market signal
- **Effect:** 8 min → 24 min wait WITHOUT surge
- **Result:** Higher completion rates, faster service WITH surge
- Shows price as operational tool, not just revenue generator

## Key Takeaways
- **Strategic Message:** Dynamic pricing can be a powerful tool to balance supply and demand in a two-sided market, improving overall system efficiency (e.g., higher completion rates, lower wait times).

- **Market Design:** Effective platform operations require sophisticated mechanisms to coordinate multiple stakeholders with different objectives.

- **Technology Enablement:** Real-time data processing and algorithmic decision-making enable new operational capabilities.

## Controversies and Debates

### Ethical Considerations
- **Price gouging:** Is surge pricing exploitation during emergencies?
- **Accessibility:** Does dynamic pricing exclude low-income users?
- **Transparency:** Are pricing algorithms sufficiently clear to users?

### Economic Efficiency vs. Social Welfare
- **Pareto efficiency:** Does surge pricing improve overall welfare?
- **Distributional effects:** Who benefits and who loses?
- **Public good aspects:** Transportation as essential service

## Preparation for Next Class
- Review queuing theory and process analysis
- Prepare [[Assignment_PATA_Massachusetts_General_Hospital_s_Pre-Admission_Testing_Area__PATA_.pdf]]
- Focus on bottleneck identification and wait time analysis

## Teaching Notes
- Contrast predictable vs. unpredictable variability management
- Emphasize the role of pricing as an operational tool
- Discuss the broader implications of platform-based business models
- Connect economic theory to operational practice
- Address student concerns about surge pricing ethics while maintaining analytical objectivity
