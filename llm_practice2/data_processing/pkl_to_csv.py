import pickle
import pandas as pd

# 피클 파일 로드
file_path = './clean_df_100.pkl'

# 피클 파일을 DataFrame으로 로드
try:
    with open(file_path, 'rb') as file:
        data = pickle.load(file)

    # DataFrame인지 확인 후 CSV로 저장
    if isinstance(data, pd.DataFrame):
        csv_file_path = './clean_df_100.csv'
        data.to_csv(csv_file_path, index=False)
        csv_status = f"CSV 파일로 변환되었습니다: {csv_file_path}"
    else:
        csv_status = "데이터는 DataFrame이 아닙니다."
except Exception as e:
    csv_status = f"파일 로드 중 오류 발생: {e}"

csv_status
