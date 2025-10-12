# Final Exam: 15.778 Introduction to Operations Management

**Date:** Monday, August 18  
**Time:** 8:30 AM - 11:30 AM  
**Duration:** 3 hours  
**Format:** In-class, individual exam

## Exam Format and Rules

### Materials Allowed
- **Printed Materials:** Lecture notes, review sheets, personal notes
- **Locally Stored:** Any materials saved on your device
- **Calculators:** Standard calculators permitted
- **NO Internet:** No access to online resources during exam

### Exam Structure
- **Quantitative Problems:** Application of models and formulas
- **Case Applications:** Analysis using course frameworks
- **Short Answer:** Conceptual understanding questions
- **Problem Solving:** Multi-step operational challenges

## Topics Covered

### Core Quantitative Tools

#### Capacity Analysis and Queuing Theory
**Key Concepts:**
- Bottleneck identification and analysis
- Build-up diagrams for capacity planning
- Basic queuing models (M/M/1, M/M/c)
- Utilization, wait times, and queue lengths
- Little's Law: L = λW

**Typical Problem Types:**
- Calculate bottleneck capacity in multi-step processes
- Determine optimal staffing levels for service operations
- Analyze wait times and service levels in queuing systems
- Build-up analysis for capacity vs. demand matching

**Example Applications:**
- PATA clinic capacity analysis
- JetBlue de-icing bottleneck
- Service operation staffing decisions

#### Inventory Management Models
**Key Concepts:**
- Economic Order Quantity (EOQ) model
- Newsvendor model for single-period decisions
- Safety stock and service level calculations
- (R,Q) inventory policies
- Risk pooling benefits quantification

**Formulas to Know:**
- **EOQ:** Q* = √(2DK/h)
- **Newsvendor:** F(Q*) = (p-c)/(p-s)
- **Safety Stock:** SS = z_α × σ_L
- **Risk Pooling:** σ_pooled = √(Σσ_i² + 2ΣΣρ_ij σ_i σ_j)

**Typical Problem Types:**
- Calculate optimal order quantities and reorder points
- Determine safety stock levels for target service levels
- Analyze benefits of inventory pooling across locations
- Compare centralized vs. decentralized inventory strategies

**Example Applications:**
- Yedioth magazine distribution optimization
- Zara inventory management strategy
- Multi-location risk pooling analysis

#### Revenue Management
**Key Concepts:**
- Dynamic pricing optimization
- Capacity allocation across customer segments
- Overbooking models and service trade-offs
- Price elasticity and demand functions

**Typical Problem Types:**
- Calculate optimal prices for revenue maximization
- Determine booking limits and protection levels
- Analyze overbooking strategies and costs
- Evaluate dynamic pricing policies

**Example Applications:**
- Airline seat allocation and pricing
- Hotel room revenue management
- Subscription pricing optimization

### Strategic Concepts

#### Process Analysis and Design
**Framework Applications:**
- Process mapping and flow analysis
- Performance metric calculation and interpretation
- Bottleneck identification and improvement strategies
- Service level vs. efficiency trade-offs

#### Supply Chain Design
**Strategic Decisions:**
- Centralization vs. decentralization trade-offs
- Network design for cost and service optimization
- Risk management and resilience strategies
- Information sharing and coordination

#### Customer Choice and Market Analysis
**Analytical Approaches:**
- Customer lifetime value (CLV) calculation
- Market segmentation and targeting
- Product assortment optimization
- Choice modeling applications

## Problem-Solving Approach

### Step-by-Step Method
1. **Read Carefully:** Understand the problem context and requirements
2. **Identify the Model:** Which framework or formula applies?
3. **Define Variables:** Clearly state what each symbol represents
4. **Set Up Equations:** Write out the relevant formulas
5. **Calculate Results:** Show all work and calculations
6. **Interpret:** Explain what the results mean in business terms
7. **Recommend:** Provide actionable recommendations when asked

### Common Mistakes to Avoid
- **Units Confusion:** Ensure time periods, costs, and quantities are consistent
- **Formula Errors:** Double-check which formula applies to the situation
- **Unrealistic Results:** Sanity-check answers for reasonableness
- **Missing Interpretation:** Always explain what numerical results mean
- **Incomplete Analysis:** Address all parts of multi-part questions

## Study Strategy

### Review Session Attendance
- **Date:** August 15, 4:00 PM - 5:30 PM (Cohort A) / 2:30 PM - 4:00 PM (Cohort B)
- **Focus:** Problem-solving techniques and formula review
- **Q&A:** Clarification on challenging concepts

### Practice Problems
1. **Lecture Examples:** Review all quantitative examples from class
2. **Case Calculations:** Practice key analyses from PATA and Yedioth
3. **Simulation Insights:** Apply concepts from Littlefield experience
4. **Formula Sheet:** Create comprehensive reference of key formulas

### Conceptual Review
- **Trade-off Analysis:** Understand fundamental operational trade-offs
- **Strategic Frameworks:** Know when to apply different models
- **Real-World Applications:** Connect formulas to business situations
- **Integration:** Understand how different topics connect

## Sample Question Types

### Capacity Analysis Example
"A clinic has 3 nurses and 2 doctors. Patients arrive at rate λ = 20/hour. Nursing takes 6 minutes per patient, doctor consultation takes 12 minutes per patient. What is the bottleneck and expected wait time?"

**Solution Approach:**
1. Calculate capacity at each resource
2. Compare to arrival rate
3. Identify bottleneck
4. Apply queuing formula for wait time

### Inventory Management Example
"A retailer faces normally distributed demand with μ = 100, σ = 30 per week. Lead time is 2 weeks. Ordering cost = $50, holding cost = $2/unit/year, stockout cost = $10/unit. Calculate optimal (R,Q) policy for 95% service level."

**Solution Approach:**
1. Calculate EOQ for order quantity
2. Determine lead time demand distribution
3. Find safety stock for 95% service level
4. Calculate reorder point

### Revenue Management Example
"An airline has 100 seats. Business travelers pay $500 and arrive with λ_B = 0.8 per day. Leisure travelers pay $200 and arrive with λ_L = 2.0 per day. Flight is in 50 days. How many seats to protect for business travelers?"

**Solution Approach:**
1. Model demand over booking period
2. Calculate expected revenues for different allocations
3. Find optimal protection level
4. Consider probability distributions

## Key Formulas Reference

### Queuing Theory
- **Utilization:** ρ = λ/μ
- **Expected Wait Time (M/M/1):** W = ρ/(μ(1-ρ))
- **Expected Queue Length:** L = λW
- **Little's Law:** L = λW

### Inventory Management
- **EOQ:** Q* = √(2DK/h)
- **Total Cost:** TC = (D/Q)K + (Q/2)h + hSS
- **Newsvendor Critical Ratio:** CR = Cu/(Cu + Co)
- **Safety Stock:** SS = z_α × σ_L
- **Service Level:** P(stockout) = 1 - F(R)

### Revenue Management
- **Revenue Function:** R(p) = p × E[min(D(p), C)]
- **Optimal Price:** MR = MC (marginal revenue = marginal cost)
- **Protection Level:** Reserve capacity for high-value segment

### Risk Pooling
- **Variance Reduction:** Var(ΣX_i) = ΣVar(X_i) + 2ΣΣCov(X_i,X_j)
- **Standard Deviation:** σ_pooled = √(Σσ_i² + 2ΣΣρ_ij σ_i σ_j)
- **Perfect Correlation:** No pooling benefit
- **Zero Correlation:** Maximum pooling benefit

## Time Management

### Exam Pacing (3 hours = 180 minutes)
- **Reading and Planning:** 15 minutes
- **Problem Solving:** 150 minutes (distribute based on point values)
- **Review and Check:** 15 minutes

### Per Problem Strategy
- **Quick Read:** Understand what's being asked
- **Time Allocation:** Spend time proportional to point value
- **Show Work:** Partial credit for correct approach
- **Move On:** Don't get stuck on one difficult problem

## Final Preparation Tips

### Day Before Exam
- **Review Formula Sheet:** Ensure familiarity with key equations
- **Practice Problems:** Work through sample calculations
- **Rest Well:** Get adequate sleep for optimal performance
- **Organize Materials:** Prepare allowed reference materials

### Day of Exam
- **Arrive Early:** Allow time to settle in and organize materials
- **Read Instructions:** Understand exam format and requirements
- **Start Strong:** Begin with problems you feel most confident about
- **Manage Time:** Monitor progress and adjust pace as needed
- **Check Work:** Review calculations and interpretations if time permits

## Success Strategies
- **Practice Quantitative Problems:** The more you practice, the faster and more accurate you'll become
- **Understand Concepts:** Memorizing formulas isn't enough; understand when and why to use them
- **Connect to Cases:** Link quantitative tools to real business situations from course cases
- **Show Your Work:** Even if the final answer is wrong, you can earn partial credit for correct methodology
- **Stay Calm:** Manage test anxiety through preparation and confident problem-solving approach

## Post-Exam
- **Reflect on Learning:** Consider how course concepts will apply in your career
- **Course Evaluation:** Provide feedback to help improve the course for future students
- **Continued Learning:** Identify areas for further study in operations management

## Teaching Assistant Support
- **Office Hours:** Available leading up to exam for questions
- **Review Session:** Attend scheduled review session for final preparation
- **Formula Clarification:** Reach out with questions about specific calculations
- **Study Groups:** Coordinate with classmates for collaborative preparation

Good luck on your final exam! Remember that the goal is to demonstrate your understanding of operations management concepts and your ability to apply quantitative tools to solve real business problems.
