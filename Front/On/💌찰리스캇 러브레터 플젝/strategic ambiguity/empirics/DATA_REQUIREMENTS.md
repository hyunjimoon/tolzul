# Real Data Requirements for AV vs 3DP Analysis

## Current Situation: Synthetic Test Data

The pipeline is currently using **synthetic/test data** with only 5 companies:
- JB Education (Primary & Secondary Schools)
- Zana (Entrepreneur mentoring platform)  
- Pollo Regio (Restaurant chain)
- Pequeno Mexico Operating Company
- Yogurtland Franchising

**These are NOT real AV or 3DP companies** - they're placeholder data to test the pipeline.

---

## What Real Data You Need to Find

### 1. Company Data (Company*.dat files)

**Source:** Pitchbook database  
**Format:** Pipe-delimited (|) .dat files  
**File naming:** `Company*.dat` (e.g., `Company2024.dat`, `Company_AV_3DP.dat`)  

**Required Columns (minimum):**
```
CompanyID           - Unique identifier (e.g., "100001-08")
CompanyName         - Company name (e.g., "Waymo", "Carbon", "Desktop Metal")
Description         - Text description of what company does
Keywords            - Comma-separated keywords/tags
TotalRaised         - Total funding raised (USD)
Employees           - Number of employees
YearFounded         - Year founded
Website             - Company website
HQLocation          - Headquarters location
BusinessStatus      - Status (e.g., "Generating Revenue", "Defunct")
```

**Full Schema:** 94 columns (see Company2021_deal2023.dat for complete list)

**What to Look For:**
- **Autonomous Vehicle companies:** Waymo, Cruise, Aurora, Argo AI, Zoox, Pony.ai, TuSimple, Plus, Gatik, Nuro, Motional, etc.
- **3D Printing companies:** Carbon, Desktop Metal, Markforged, Formlabs, Stratasys, 3D Systems, Velo3D, Divergent, Relativity Space, etc.
- **Time period:** Companies founded or funded during your study period (2021-2025)

### 2. Deal Data (Deal*.dat files) - CURRENTLY MISSING!

**Source:** Pitchbook database  
**Format:** Pipe-delimited (|) .dat files  
**File naming:** `Deal*.dat` (e.g., `Deal2023.dat`, `Deal2024.dat`)  

**Required Columns (minimum):**
```
DealID              - Unique deal identifier
CompanyID           - Links to CompanyID in Company file
DealDate            - Date of funding round
DealSize            - Amount raised in USD
DealType            - Type (e.g., "Series A", "Series B", "Venture Round")
PostValuation       - Post-money valuation
Investors           - List of investors
LeadInvestors       - Lead investors
```

**What to Look For:**
- **Series A rounds:** 2021-01-01 to 2022-10-31
- **Series B rounds:** 2023-05-01 to 2025-10-31
- Focus on AV and 3DP companies during these periods

---

## Example: Real AV Company Data Structure

Here's what a real Waymo entry would look like:

```csv
CompanyID|CompanyName|Description|Keywords|TotalRaised|Employees|YearFounded|...
123456-78|Waymo|Developer of autonomous driving technology. The company creates self-driving cars using sensors and software to perceive and navigate the world without human intervention.|autonomous vehicle,self-driving,lidar,perception,sensor fusion,automotive ai|5500000000|2500|2009|...
```

**Key Description Terms for AV:**
- "autonomous vehicle", "self-driving", "autonomous driving"
- "lidar", "radar", "sensor fusion", "perception"
- "adas", "advanced driver assistance"
- "robotaxi", "autonomous trucking"

## Example: Real 3DP Company Data Structure

Here's what a real Carbon entry would look like:

```csv
CompanyID|CompanyName|Description|Keywords|TotalRaised|Employees|YearFounded|...
234567-89|Carbon|Developer of 3D printing technology. The company provides digital light synthesis additive manufacturing technology for rapid prototyping and production.|3d printing,additive manufacturing,digital light synthesis,rapid prototyping,stereolithography|680000000|550|2013|...
```

**Key Description Terms for 3DP:**
- "3d print", "additive manufacturing"
- "stereolithography", "SLA", "SLS", "FDM"
- "rapid prototyping", "metal printing"
- "powder bed fusion", "material extrusion"

---

## How to Obtain Real Pitchbook Data

### Option 1: Pitchbook Direct Export
1. Log into Pitchbook (https://my.pitchbook.com)
2. Build search query:
   - **Sectors:** Autonomous Vehicles OR 3D Printing
   - **Financing Status:** Venture Capital
   - **Last Financing Date:** 2021-2025
   - **Geography:** US (or global)
3. Export as CSV/Excel with all company fields
4. Save as pipe-delimited .dat file

### Option 2: Pitchbook Excel Plugin
1. Use Pitchbook Excel Add-in
2. Create company list with filters
3. Pull all company fields
4. Export as .dat format

### Option 3: Pitchbook API (if available)
1. Use Pitchbook API credentials
2. Query companies by sector keywords
3. Download company and deal data
4. Format as pipe-delimited files

---

## Data Validation Checklist

Before replacing test data, verify:

### Company File Checks:
- [ ] Contains real AV companies (>10 companies minimum)
- [ ] Contains real 3DP companies (>10 companies minimum)  
- [ ] Has Description field with detailed text
- [ ] Has Keywords field
- [ ] Has TotalRaised, Employees, YearFounded
- [ ] CompanyID is unique
- [ ] File is pipe-delimited (|)

### Deal File Checks:
- [ ] Contains Series A deals (2021-2022)
- [ ] Contains Series B deals (2023-2025)
- [ ] CompanyID matches Company file
- [ ] Has DealDate, DealSize, DealType
- [ ] Has Investors and PostValuation
- [ ] File is pipe-delimited (|)

### Data Quality:
- [ ] AV companies have relevant keywords (lidar, autonomous, self-driving)
- [ ] 3DP companies have relevant keywords (additive, 3d print, stereolithography)
- [ ] Description fields contain substantive text (>50 characters)
- [ ] No excessive missing values in key fields

---

## Sample Data Queries for Pitchbook

### Query 1: Autonomous Vehicle Companies
```
Sector: Autonomous Vehicles
Financing Status: Venture Capital, Private Equity
Last Financing Date: 2021-01-01 to 2025-10-31
Geography: United States
Status: Active, Generating Revenue

Export Fields:
- All Company Fields (94 columns)
- Include: CompanyID, Name, Description, Keywords, Total Raised, Employees, Year Founded
```

### Query 2: 3D Printing Companies
```
Sector: 3D Printing, Additive Manufacturing
Financing Status: Venture Capital, Private Equity
Last Financing Date: 2021-01-01 to 2025-10-31
Geography: United States
Status: Active, Generating Revenue

Export Fields:
- All Company Fields (94 columns)
- Include: CompanyID, Name, Description, Keywords, Total Raised, Employees, Year Founded
```

### Query 3: Corresponding Deal Data
```
For each company list above:
- Export all deals for those companies
- Filter deals: Series A (2021-2022), Series B (2023-2025)
- Include all deal fields
```

---

## Expected Data Size for Real Analysis

### Minimum Viable Dataset:
- **AV Companies:** 20-50 companies
- **3DP Companies:** 20-50 companies  
- **Deals:** 50-200 funding rounds total
- **File size:** 500 KB - 5 MB

### Robust Dataset:
- **AV Companies:** 100-200 companies
- **3DP Companies:** 100-200 companies
- **Deals:** 500-1000 funding rounds
- **File size:** 5-50 MB

---

## Testing with Real Data

Once you have real Pitchbook files:

1. **Place files in correct location:**
   ```bash
   # Copy files to:
   data/raw/Company_AV_3DP.dat
   data/raw/Deal_AV_3DP.dat
   ```

2. **Run pipeline:**
   ```bash
   cd empirics
   python code/pipeline_xarray.py --from 1
   ```

3. **Check sector classification:**
   ```bash
   python code/sector_analysis_example.py
   ```

4. **Verify results:**
   - Company count for AV sector > 0
   - Company count for 3DP sector > 0
   - Deals loaded successfully
   - Vagueness scores calculated
   - Integration cost classified

---

## What the Pipeline Will Do with Real Data

1. **Filter to AI/ML companies** (which includes AV and 3DP)
2. **Classify into sectors** using keyword matching:
   - AV sector: Companies with "autonomous vehicle", "self-driving", etc.
   - 3DP sector: Companies with "3d print", "additive manufacturing", etc.
3. **Calculate vagueness scores** from Description text
4. **Classify integration cost** (high-i for hardware/AV, low-i for software)
5. **Filter deals** to Series A (2021-2022) and Series B (2023-2025)
6. **Create analysis panel** for hypothesis testing

---

## Hypothesis Test Variables (What We'll Measure)

Once you have real AV and 3DP data, the pipeline will test:

### Independent Variables:
- `vagueness` - Vagueness score (0-100) from Description
- `high_integration_cost` - Binary (1=high-i like AV, 0=low-i like software)
- `sector_AV` - Is this an AV company?
- `sector_3DP` - Is this a 3DP company?
- `series_b_dummy` - Is this Series B vs Series A?

### Dependent Variables:
- `funding_success` - Binary (1=got Series B, 0=did not)
- `deal_size` - Amount raised
- `post_valuation` - Post-money valuation

### Control Variables:
- `employees` - Company size
- `year_founded` - Company age
- `total_raised` - Prior funding
- `series_a_amount` - Series A size (for Series B analysis)

---

## Next Steps

1. **Access Pitchbook** - Get institutional access or API credentials
2. **Export AV data** - Use queries above to get 50-200 AV companies
3. **Export 3DP data** - Use queries above to get 50-200 3DP companies
4. **Export Deal data** - Get all deals for those companies
5. **Save as .dat files** - Pipe-delimited format
6. **Replace test data** - Put in data/raw/ directory
7. **Re-run pipeline** - See multi-sector classification in action!

---

## Questions to Answer

When looking for data, ask yourself:

1. **Do the companies match my research focus?**
   - Are they truly in "eras of ferment" (early-stage, high uncertainty)?
   - Do they represent distinct sectors (AV vs 3DP)?

2. **Is the time period correct?**
   - Series A: 2021-2022 (Era 1)
   - Series B: 2023-2025 (Era 2)

3. **Is there enough variation?**
   - Mix of vague vs. precise descriptions?
   - Mix of successful vs. unsuccessful funding outcomes?
   - Mix of high-i (AV, hardware) vs. low-i (software, SaaS)?

4. **Is the data quality sufficient?**
   - Complete Description fields?
   - Accurate funding amounts?
   - Reliable valuation data?

---

## Contact for Help

If you need help:
1. Check Pitchbook documentation
2. Contact your institution's Pitchbook representative
3. Review Pitchbook export guides
4. Reach out to colleagues who use Pitchbook for research

The pipeline is ready - it just needs real data!
