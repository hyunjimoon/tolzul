"""
xarray 빠른 시작 가이드

Pipeline 실행 후 이 스크립트로 데이터 탐색하세요!
"""

import xarray as xr
import pandas as pd

# 1. 데이터 불러오기
print("=" * 60)
print("1. 데이터 불러오기")
print("=" * 60)

ds = xr.open_dataset('output/pitchbook_analysis.nc')
print(ds)
print()

# 2. Dimensions (차원) 확인
print("=" * 60)
print("2. Dimensions (차원)")
print("=" * 60)
print(f"회사: {ds.dims['company']}개")
print(f"딜: {ds.dims['deal']}개")
print(f"관측치: {ds.dims['observation']}개")
print()

# 3. Coordinates (좌표) 확인
print("=" * 60)
print("3. Coordinates (좌표)")
print("=" * 60)
print("회사 ID (처음 5개):")
print(ds.coords['company'].values[:5])
print()

# 4. Variables (변수) 목록
print("=" * 60)
print("4. Variables (변수) 목록")
print("=" * 60)
print("회사 데이터:")
for var in ds.data_vars:
    if var.startswith('company_'):
        print(f"  - {var}")
print()

print("딜 데이터:")
for var in ds.data_vars:
    if var.startswith('deal_'):
        print(f"  - {var}")
print()

print("패널 데이터:")
for var in ds.data_vars:
    if var.startswith('panel_'):
        print(f"  - {var}")
print()

# 5. 데이터 접근
print("=" * 60)
print("5. 데이터 접근 예제")
print("=" * 60)

# 5.1 모호성 점수 평균
vagueness = ds.company_vagueness.values
print(f"평균 모호성 점수: {vagueness.mean():.1f} (0-100 척도)")
print(f"표준편차: {vagueness.std():.1f}")
print()

# 5.2 Series A vs B 성공률
panel_df = pd.DataFrame({
    'round': ds.panel_round.values,
    'success': ds.panel_funding_success.values
})
success_by_round = panel_df.groupby('round')['success'].mean()
print("라운드별 펀딩 성공률:")
print(success_by_round)
print()

# 5.3 특정 회사 정보
company_id = ds.coords['company'].values[0]
print(f"첫 번째 회사 정보:")
print(f"  ID: {company_id}")
print(f"  이름: {ds.company_CompanyName.sel(company=company_id).values}")
print(f"  모호성: {ds.company_vagueness.sel(company=company_id).values}")
print()

# 6. Attributes (메타데이터)
print("=" * 60)
print("6. Attributes (메타데이터)")
print("=" * 60)
print(f"생성 코드: {ds.attrs['git_commit_url'][:80]}...")
print(f"브랜치: {ds.attrs['git_branch']}")
print(f"처리 완료: {ds.attrs['step_05_timestamp']}")
print(f"데이터 요약:")
print(f"  - 회사: {ds.attrs['n_companies']}개")
print(f"  - 딜: {ds.attrs['n_deals']}개")
print(f"  - 관측치: {ds.attrs['n_observations']}개")
print()

# 7. 유용한 팁
print("=" * 60)
print("7. 유용한 팁")
print("=" * 60)

print("# DataFrame으로 변환:")
print("df = ds.to_dataframe()")
print()

print("# 특정 변수만 선택:")
print("subset = ds[['company_vagueness', 'company_Employees']]")
print()

print("# 조건 필터링:")
print("high_vague = ds.where(ds.company_vagueness > 60, drop=True)")
print()

print("# 변수 계산:")
print("avg_vagueness = ds.company_vagueness.mean().values")
print()

print("완료! 이제 자유롭게 탐색해보세요!")
