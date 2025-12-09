# Test Suite

Comprehensive unit tests for the 5-stage multiverse analysis pipeline.

## Test Structure

```
test/
├── test_stage1_build.py      # Stage 1: Data loading and consolidation
├── test_stage2_define.py     # Stage 2: Feature engineering
├── test_stage3_plot1.py      # Stage 3: Variable distributions
├── test_stage4_test.py       # Stage 4: Hypothesis testing
├── test_stage5_plot2.py      # Stage 5: Multiverse visualization
└── README.md                 # This file
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run tests for a specific stage
```bash
# Stage 1 (BUILD)
pytest test/test_stage1_build.py -v

# Stage 2 (DEFINE)
pytest test/test_stage2_define.py -v

# Stage 3 (PLOT1)
pytest test/test_stage3_plot1.py -v

# Stage 4 (TEST)
pytest test/test_stage4_test.py -v

# Stage 5 (PLOT2)
pytest test/test_stage5_plot2.py -v
```

### Run tests with markers
```bash
# Run only unit tests
pytest -m unit

# Run only stage 1 tests
pytest -m stage1
```

### Run a specific test
```bash
pytest test/test_stage1_build.py::TestStage1Build::test_consolidate_basic_loading -v
```

### Run with coverage
```bash
pytest --cov=modules --cov-report=html
```

## Test Coverage

### Stage 1: BUILD (Data Loading)
- ✅ Basic .dat file loading
- ✅ Parquet caching (save and load)
- ✅ Selective year loading
- ✅ Data validation
- ✅ Quantum company filtering
- ✅ Empty directory handling

### Stage 2: DEFINE (Feature Engineering)
- ✅ Required column creation
- ✅ Vagueness score calculation
- ✅ Hardware/software classification
- ✅ Early funding derivation (Series A filtering)
- ✅ Growth variable (Series B+ indicator)
- ✅ Sector fixed effects classification
- ✅ Log transformation (employees)
- ✅ Firm age calculation
- ✅ Z-score standardization
- ✅ Founding cohort creation
- ✅ Missing value handling

### Stage 3: PLOT1 (Distributions)
- ✅ Distribution plot creation
- ✅ File saving
- ✅ Missing variable handling
- ✅ Empty DataFrame handling

### Stage 4: TEST (Hypotheses)
- ✅ H1 model execution (Early Funding ~ Vagueness)
- ✅ H2 model execution (Growth ~ Vagueness × Hardware)
- ✅ Vagueness coefficient presence
- ✅ Interaction term presence
- ✅ Missing data handling
- ✅ Small sample convergence
- ✅ Minimal controls

### Stage 5: PLOT2 (Multiverse)
- ✅ Expectation vs reality heatmap
- ✅ Specification curve plotting
- ✅ Alignment calculation
- ✅ Alignment score range validation
- ✅ Edge case handling

## Requirements

Install test dependencies:
```bash
pip install pytest pytest-cov
```

## Test Fixtures

Tests use pytest fixtures to create mock data:
- `mock_data_dir`: Temporary directory with mock .dat files
- `sample_df`: Sample raw company data
- `engineered_df`: Sample engineered features
- `sample_processed_df`: Sample processed data for plotting
- `sample_analysis_df`: Sample data for hypothesis testing
- `sample_spec_df`: Sample multiverse specification results

## Continuous Integration

These tests can be integrated into CI/CD pipelines:

```yaml
# GitHub Actions example
- name: Run tests
  run: |
    pip install pytest pytest-cov
    pytest --cov=modules --cov-report=xml
```

## Writing New Tests

Follow this structure for new tests:

```python
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from modules import features

class TestNewFeature:
    """Test suite for new feature"""

    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing"""
        return pd.DataFrame({...})

    def test_feature_works(self, sample_data):
        """Test that feature works as expected"""
        result = features.new_function(sample_data)
        assert result is not None
```

## Troubleshooting

### Import errors
If you get import errors, ensure the modules are in your Python path:
```python
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
```

### Missing dependencies
Install required packages:
```bash
pip install pandas numpy statsmodels matplotlib seaborn scipy
```

### Test discovery issues
Make sure:
- Test files start with `test_`
- Test classes start with `Test`
- Test functions start with `test_`

## Contact

For issues or questions about tests, refer to:
- Main pipeline: `../MAIN_PIPELINE_README.md`
- Caching features: `../PARQUET_QUANTUM_README.md`
- Selective loading: `../SELECTIVE_LOADING_GUIDE.md`
