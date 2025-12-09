import sys
from pathlib import Path
import xarray as xr

# src 모듈을 가져오기 위해 경로 설정
sys.path.append(str(Path.cwd()))

from src.data_prep import build_panel_v3

def main():
    print("="*60)
    print("🔄 OPERATION: BATCH CONVERSION (Parquet -> NetCDF)")
    print("="*60)

    # 1. 탐색할 대상 폴더 (outputs/ 아래의 폴더들)
    base_dir = Path("outputs")
    
    # 이미지에 있는 폴더들을 포함해 타겟 설정
    # (dataset.parquet이 존재하는 모든 하위 폴더를 자동으로 찾습니다)
    target_files = list(base_dir.glob("**/dataset.parquet"))

    if not target_files:
        print("❌ 'outputs/' 폴더 내에서 'dataset.parquet' 파일을 찾을 수 없습니다.")
        return

    print(f"🎯 총 {len(target_files)}개의 타겟 파일 발견.\n")

    # 2. 순회하며 변환 실행
    for input_path in target_files:
        scenario_name = input_path.parent.name  # all, quantum, transportation, eyeball_test 등
        output_path = input_path.parent / "panel_v3.nc" # 같은 폴더에 .nc로 저장

        print(f"🚀 Processing Scenario: [{scenario_name}]")
        print(f"   - Input:  {input_path}")
        print(f"   - Output: {output_path}")

        try:
            # src/data_prep.py의 핵심 함수 호출
            # (V3 스코어링 + Founder DB 병합 + Xarray 변환이 자동 수행됨)
            ds = build_panel_v3(str(input_path), str(output_path))
            
            print(f"   ✅ 변환 성공! (Dimensions: {dict(ds.dims)})")
            
        except Exception as e:
            print(f"   ❌ 변환 실패: {e}")
            import traceback
            traceback.print_exc()
        
        print("-" * 60)

    print("\n🏁 모든 작업이 완료되었습니다.")

if __name__ == "__main__":
    main()