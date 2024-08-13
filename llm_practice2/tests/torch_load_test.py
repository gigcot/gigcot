import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer

# 모델 파일과 토크나이저의 절대 경로를 생성
base_path = "D:/ML_practice_data/llm_practice2/gguf-to-torch/model_output.pth"
model_file = "pytorch_model.bin"

# 절대 경로 조합
model_path = os.path.join(base_path, model_file)

try:
    model = torch.load(model_path)
    print("모델이 성공적으로 로드되었습니다")
except Exception as e:
    print(f"모델 로드 실패: {e}")
