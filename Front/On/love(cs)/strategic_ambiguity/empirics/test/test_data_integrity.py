# test/test_data_integrity.py
import pytest
import pandas as pd
import numpy as np
from pathlib import Path

class TestDataIntegrity:
    """데이터 무결성 검증 테스트"""

    @pytest.fixture
    def df(self):
        """분석용 데이터 로드"""
        path = Path("outputs/all/models/h2_analysis_dataset.csv")
        # 필요한 컬럼만 로드 (메모리 효율)
        cols = ['vagueness', 'growth', 'z_vagueness', 'founder_serial',
                'z_employees_log', 'founding_cohort']
        return pd.read_csv(path, usecols=cols)

    def test_sample_size(self, df):
        """N ≈ 1,250,000 확인 (actual data size)"""
        assert 1_000_000 < len(df) < 2_000_000, f"Unexpected N: {len(df)}"

    def test_vagueness_range(self, df):
        """V ∈ [0, 1] 또는 [0, 100] 확인"""
        v = df['vagueness'].dropna()
        assert v.min() >= 0, f"V min < 0: {v.min()}"
        # V가 0-100 스케일이면 0-1로 변환 필요
        if v.max() > 1:
            print(f"⚠️ V appears to be 0-100 scale (max={v.max():.2f})")

    def test_growth_binary(self, df):
        """G ∈ {0, 1} 확인"""
        unique_vals = df['growth'].dropna().unique()
        assert set(unique_vals).issubset({0, 1, 0.0, 1.0}), \
            f"Growth not binary: {unique_vals}"

    def test_growth_rate_reasonable(self, df):
        """성장률 1-50% 범위 확인 (actual rate ~4%)"""
        rate = df['growth'].mean()
        assert 0.01 < rate < 0.50, f"Unusual growth rate: {rate:.1%}"

    def test_z_vagueness_standardized(self, df):
        """z_vagueness가 표준화되었는지 확인"""
        z = df['z_vagueness'].dropna()
        assert abs(z.mean()) < 0.1, f"z_V mean not ~0: {z.mean():.4f}"
        assert 0.8 < z.std() < 1.2, f"z_V std not ~1: {z.std():.4f}"

    def test_no_extreme_missingness(self, df):
        """핵심 변수 결측률 < 20%"""
        for col in ['vagueness', 'growth', 'z_vagueness']:
            miss_rate = df[col].isna().mean()
            assert miss_rate < 0.20, f"{col} missing {miss_rate:.1%}"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
