# src/definitions.py
"""
Shared definitions for vagueness scoring and data preparation.

Contains:
- MARKET_KEYWORDS: Categorized keywords for market entropy calculation
- TECH_SPEC_PATTERNS: Regex patterns for technical specificity
- CONSTANTS: Numerical constants
- Architecture keywords (Hardware/Software)
- Sector mappings
"""

# =============================================================================
# MARKET KEYWORDS (for V3 Market Entropy calculation)
# =============================================================================
# Categories represent different market verticals
# Shannon entropy is computed over hits across these categories

MARKET_KEYWORDS = {
    "fintech": [
        "fintech", "payment", "banking", "insurance", "insurtech",
        "lending", "credit", "mortgage", "wealth management", "trading",
        "blockchain", "cryptocurrency", "defi", "neobank"
    ],
    "healthcare": [
        "healthcare", "health tech", "medical", "pharma", "biotech",
        "diagnostic", "therapeutics", "clinical", "patient", "hospital",
        "telemedicine", "digital health", "drug discovery"
    ],
    "enterprise": [
        "enterprise", "b2b", "saas", "crm", "erp", "workflow",
        "collaboration", "productivity", "hr tech", "recruiting",
        "sales enablement", "customer success"
    ],
    "consumer": [
        "consumer", "b2c", "e-commerce", "retail", "marketplace",
        "social", "gaming", "entertainment", "media", "content",
        "subscription", "d2c"
    ],
    "infrastructure": [
        "infrastructure", "cloud", "devops", "api", "platform",
        "data infrastructure", "database", "storage", "compute",
        "kubernetes", "serverless", "microservices"
    ],
    "ai_ml": [
        "artificial intelligence", "machine learning", "deep learning",
        "nlp", "computer vision", "generative ai", "llm", "ml ops",
        "neural network", "predictive analytics"
    ],
    "hardware": [
        "hardware", "semiconductor", "chip", "sensor", "robotics",
        "autonomous", "drone", "iot", "edge computing", "device",
        "manufacturing", "3d printing"
    ],
    "cleantech": [
        "cleantech", "renewable", "solar", "wind", "battery",
        "energy storage", "ev", "electric vehicle", "sustainability",
        "carbon", "climate tech"
    ],
    "cybersecurity": [
        "cybersecurity", "security", "privacy", "encryption",
        "identity", "authentication", "threat detection", "compliance",
        "zero trust", "soc"
    ],
    "logistics": [
        "logistics", "supply chain", "transportation", "delivery",
        "fulfillment", "warehouse", "freight", "shipping", "fleet"
    ],
}

# =============================================================================
# TECHNICAL SPEC PATTERNS (for V3 Tech Abstractness)
# =============================================================================
# Regex patterns to detect concrete technical specifications
# Higher density = lower abstractness

TECH_SPEC_PATTERNS = {
    "metrics_units": r"""
        \b\d+\.?\d*\s*
        (?:nm|μm|mm|cm|m|km|                           # length
        ghz|mhz|khz|hz|                                 # frequency
        gb|tb|mb|kb|pb|                                 # storage
        gbps|mbps|kbps|                                 # bandwidth
        ms|μs|ns|s|                                     # time
        kw|mw|w|kwh|mwh|                               # power
        fps|rpm|                                        # rate
        °c|°f|k|                                        # temperature
        db|dbi|                                         # signal
        %|pct|percent)                                  # percentage
        \b
    """,
    "versions": r"""
        \b(?:
        v\d+(?:\.\d+){0,3}|                            # v1.2.3
        version\s+\d+|                                  # version 1
        release\s+\d+|                                  # release 1
        sdk\s+v?\d+|                                    # sdk v2
        api\s+v?\d+                                     # api v2
        )\b
    """,
    "timelines": r"""
        \b(?:
        20[0-2]\d|                                      # years 2000-2029
        q[1-4]\s*20[0-2]\d|                            # Q1 2024
        (?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+20[0-2]\d  # month year
        )\b
    """,
    "standards": r"""
        \b(?:
        iso\s*\d+|                                      # ISO standards
        ieee\s*\d+|                                     # IEEE standards
        fda|ce\s*mark|                                  # regulatory
        soc\s*[12]|hipaa|gdpr|pci|                     # compliance
        ul\s*\d+|iec\s*\d+                             # safety standards
        )\b
    """,
    "performance": r"""
        \b(?:
        latency|throughput|bandwidth|uptime|           # performance metrics
        accuracy|precision|recall|f1|auc|              # ML metrics
        error\s*rate|success\s*rate|                   # rates
        roi|cac|ltv|arr|mrr|gmv                        # business metrics
        )\b
    """,
}

# =============================================================================
# CONSTANTS
# =============================================================================

CONSTANTS = {
    "ENTROPY_EPS": 1e-10,  # Small value to avoid log(0)
    "MIN_WORDS": 5,        # Minimum words for valid vagueness scoring
    "IDF_SMOOTH": 1.0,     # IDF smoothing parameter
}

# =============================================================================
# ARCHITECTURE KEYWORDS (Hardware vs Software classification)
# =============================================================================

ARCH_HARDWARE_KEYWORDS = [
    "hardware", "robotics", "robot", "chip", "asic", "semiconductor",
    "device", "sensor", "fpga", "silicon", "biotech", "quantum",
    "autonomous vehicle", "av", "battery", "manufacturing", "actuator",
    "lidar", "camera module", "edge device", "physical", "mechanical",
    "circuit", "pcb", "antenna", "motor", "embedded"
]

ARCH_SOFTWARE_KEYWORDS = [
    "software", "saas", "api", "cloud", "platform", "sdk",
    "microservice", "data", "ml", "ai", "nlp", "cv", "llm",
    "analytics", "developer tool", "web", "mobile app", "dashboard",
    "automation", "integration", "workflow", "algorithm"
]

# =============================================================================
# SECTOR MAPPINGS (Nanda-style sector codes)
# =============================================================================

NANDA_SECTOR_TO_CODE = {
    "Information Technology": "IT",
    "Healthcare": "HC",
    "Financial Services": "FS",
    "Consumer Products and Services": "CP",
    "Business Products and Services": "BP",
    "Energy": "EN",
    "Materials and Resources": "MR",
    "Other": "OT",
}

# Reverse mapping
NANDA_CODE_TO_SECTOR = {v: k for k, v in NANDA_SECTOR_TO_CODE.items()}
