# Sector Classification Configuration

This directory contains configuration files for multi-sector company classification.

## Files

- `sector_keywords.py`: Keyword definitions for each sector
- `__init__.py`: Package initialization

## Usage

### Import sector definitions

```python
from config.sector_keywords import SECTOR_DEFINITIONS, get_all_sectors

# Get all available sectors
sectors = get_all_sectors()  # Returns: ['AV', '3DP', 'AI_ML', 'Robotics', 'Software', 'Hardware']

# Get keywords for a specific sector
av_keywords = get_sector_keywords('AV')

# Get full sector information
av_info = get_sector_info('AV')
print(av_info['name'])  # 'Autonomous Vehicles'
print(av_info['description'])
print(av_info['keywords'])
```

### Available Sectors

1. **AV** - Autonomous Vehicles
   - Self-driving cars, LIDAR, perception systems, ADAS
   
2. **3DP** - 3D Printing
   - Additive manufacturing, stereolithography, metal printing
   
3. **AI_ML** - AI/Machine Learning
   - Deep learning, NLP, language models, computer vision
   
4. **Robotics** - Robotics
   - Industrial robots, manipulation, cobots, automation
   
5. **Software** - Software/SaaS
   - Cloud platforms, APIs, web applications, SaaS
   
6. **Hardware** - Hardware
   - Chips, semiconductors, ASICs, FPGAs, edge devices

## Adding New Sectors

To add a new sector:

1. Open `sector_keywords.py`
2. Add a new entry to `SECTOR_DEFINITIONS`:

```python
'NewSector': {
    'name': 'Full Sector Name',
    'description': 'Description of the sector',
    'keywords': [
        'keyword1', 'keyword2', 'keyword3'
    ],
    'version': '1.0',
    'last_updated': '2025-10-26'
}
```

3. Re-run the pipeline: `python pipeline_xarray.py --from 1`

## Keyword Best Practices

- Use lowercase for all keywords
- Include variations and synonyms
- Add domain-specific terminology
- Include company/product names if relevant
- Test keywords on sample data before committing

## Version Control

- Track keyword changes in git
- Update version numbers when making changes
- Document major changes in this README
