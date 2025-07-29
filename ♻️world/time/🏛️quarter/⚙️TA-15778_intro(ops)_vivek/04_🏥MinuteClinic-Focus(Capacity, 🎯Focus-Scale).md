# Lecture 4: PATA Case - Process Analysis and Queuing Theory

**Date:** July 25  
**Duration:** 1.5 hours  
**Instructor:** Prof. Vivek Farias  
**Assignment:** GRADED CASE WRITE-UP DUE AT 8:30 AM (TEAM)

----

[[2025-07-25|25-07-25-08]]

[[paradox of entrepreneurship]]

- product strategy in service industry (process flow diagram and process utlitization, tool: buildup diagram for predictable variability, queuing theory (unpredictable variablity )
- smoothing out process - better prediction
- teaching [[style]] - case discussion, 
	- patient 🟧checks in, wait, 🟧🟧vitals + ekg in lab, 🟧🟧🟧rn (review, writesup),🟧🟧🟧🟧 md visit (reviews, chat, write chart), 🟠 blodd work in lab,  🟠🟧check out
- staggering over lunch (2.8pt/hr; rho = 1)
- evaluation on task force recommendation

- which unpredictable variablity is contributing the most ?
- service time? if CV = 1,  can contribute 

⭐️bottleneck at RY -> build up -> translate build up to delay, 

fluid proces -> lose integrality (goal is capture first order effect)

peak delay will be higher, avg delay will be lower

not give process diagram

⭐️run this simulation, ppl are waiting for the room. 현상적으로 기다리는 건 병목과 다르다. what are the rooms in the first place? [[2025-07-25|25-07-25-09]]

room became glorified waiting room?? rooms are not meant to wait but 

why [[vivek_ferias]] likes teaching

annual leaked revneue per employed physician

---
## Learning Objectives
- Apply capacity analysis tools to service operations
- Use queuing theory to diagnose bottlenecks and wait times
- Analyze sources of variability in healthcare processes
- Develop operational improvement recommendations

## Case Studies
- **Primary Case:** [[Assignment_PATA_Massachusetts_General_Hospital_s_Pre-Admission_Testing_Area__PATA_.pdf]]
- **Supporting Case:** [[Lec4_Intermountain_Health_Care.pdf]] (SKIM)
## Key Concepts

### Process Analysis Tools
1. **Build-up Diagrams:** Visual representation of capacity vs. demand over time
2. **Queuing Theory:** Mathematical analysis of waiting lines
3. **Bottleneck Identification:** Finding constraining resources
4. **Variability Analysis:** Understanding sources and impacts of uncertainty

### Healthcare Operations Characteristics
- **Service nature:** Cannot inventory "procedures"
- **High variability:** Patient conditions, procedure times, arrival patterns
- **Multiple resources:** Physicians, nurses, rooms, equipment
- **Quality implications:** Patient safety and satisfaction
- **Regulatory environment:** Compliance and standards

### Queuing Theory Fundamentals
- **Little's Law:** L = λW (Items in system = Arrival rate × Wait time)
- **Utilization:** ρ = λ/μ (Arrival rate / Service rate)
- **Queue length:** Expected number waiting
- **Wait time:** Expected delay before service begins

## Case Analysis Framework

### PATA Background
- **Purpose:** Pre-admission testing for surgical patients
- **Patient flow:** Registration → Nursing → Physician → Departure
- **Resources:** Nurses, physicians, examination rooms
- **Performance issues:** Long patient wait times, system inefficiency

### Process Flow Analysis
The provided process flow diagram shows:
1. **Patient arrivals** at scheduled appointment times
2. **Registration process** 
3. **Nursing assessment** (vital signs, medical history)
4. **Physician evaluation** (physical exam, clearance)
5. **Administrative completion** and departure

### Given Data Analysis
- **Input rates:** Patient arrival patterns
- **Processing rates:** Time requirements for each step
- **Resource availability:** Number of nurses, physicians, rooms
- **Performance metrics:** Current wait times and utilization

## Graded Assignment Questions

### Question 1: Bottleneck Analysis
**Prompt:** Use capacity analysis tools (build-up diagrams or/and queuing) to decide if and where there is a bottleneck in the clinic. If a bottleneck does indeed exist, how long do patients wait as a result of the bottleneck?

**Analysis Framework:**
- Calculate capacity at each process step
- Compare capacity to demand (arrival rate)
- Identify the constraining resource
- Apply queuing formulas to estimate wait times
- Assume all appointment slots filled and on-time arrivals

### Question 2: Task Force Diagnosis Evaluation
**Prompt:** Evaluate the three Task Force diagnoses: not enough time between appointments, not enough rooms, not enough physicians. Are these diagnoses valid? If so, are they primary contributors to long patient wait times?

**Analysis Approach:**
- Test each hypothesis against calculated bottlenecks
- Determine if diagnosis addresses actual constraint
- Assess magnitude of impact on wait times
- Consider interaction effects between constraints

### Question 3: Variability Analysis  
**Prompt:** What factors contribute to variability in PATA process flow and what control, if any, does the clinic have to eliminate it?

**Sources of Variability:**
- **Arrival variability:** Late patients, no-shows, early arrivals
- **Service time variability:** Patient complexity, physician efficiency
- **Resource variability:** Staff availability, room availability
- **External factors:** Emergency interruptions, equipment issues

**Control Strategies:**
- **Demand-side:** Appointment scheduling, patient preparation
- **Supply-side:** Staffing policies, process standardization
- **Buffer management:** Capacity cushions, flexible resources

### Question 4: Improvement Recommendations
**Prompt:** What changes would you recommend to improve PATA?

**Recommendation Categories:**
1. **Capacity changes:** Staffing levels, resource allocation
2. **Process redesign:** Flow improvements, task reallocation  
3. **Scheduling optimization:** Appointment timing, patient mix
4. **Variability reduction:** Standardization, buffer management
5. **Information systems:** Real-time tracking, communication

## Quantitative Analysis Tools

### Build-up Diagram Construction
1. Plot demand over time (arrival pattern)
2. Plot available capacity over time
3. Identify periods where demand exceeds capacity
4. Calculate cumulative gap (queue buildup)

### Queuing Calculations
- **M/M/1 Queue:** Single server, exponential arrivals and service
- **M/M/c Queue:** Multiple servers
- **Expected wait time:** W = ρ/(μ(1-ρ)) for M/M/1
- **Expected queue length:** L = λW

### Performance Metrics
- **Average wait time:** Time from arrival to service start
- **Cycle time:** Total time in system
- **Utilization rates:** Resource busy time / Available time
- **Throughput:** Patients served per time period

## Healthcare Service Operations Context

### Unique Challenges
- **Variability amplification:** Uncertainty compounds through process steps
- **Service quality:** Patient experience and medical outcomes
- **Cost pressures:** Efficiency vs. access trade-offs
- **Regulatory compliance:** Safety and quality standards

### Improvement Strategies
- **Lean principles:** Waste elimination, flow optimization
- **Six Sigma:** Variation reduction, quality improvement  
- **Capacity pooling:** Flexible resources, cross-training
- **Technology:** EMR integration, real-time tracking

## Key Takeaways
- **Strategic Message:** Process analysis, particularly managing variability in arrivals and service times, is critical for identifying and alleviating bottlenecks in service operations to reduce customer wait times.

- **Queuing Insights:** Small increases in utilization can cause disproportionate increases in wait times.

- **Healthcare Operations:** Service operations require balancing efficiency, quality, and access in highly variable environments.

## Assignment Submission Guidelines
- **Team work:** Study groups of max 5 students
- **Due:** 8:30 AM on July 25
- **Length:** Less than 4 pages (excluding appendices)
- **Format:** 12-point font minimum
- **Calculations:** Must include clear explanations of all formulas and methods

## Preparation for Next Class
- Review inventory management concepts
- Begin thinking about demand uncertainty and safety stock
- Read inventory control fundamentals

## Recitation Support  
- **Focus:** Capacity analysis techniques and PATA case preparation
- **Quantitative methods:** Bottleneck identification and queuing calculations
- **Office hours:** Available for team questions

## Teaching Notes
- Emphasize practical application of queuing theory
- Connect theoretical concepts to healthcare realities
- Guide students through bottleneck identification process
- Stress importance of clear quantitative reasoning in recommendations
