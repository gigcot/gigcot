print("11..")
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
print("2..")
os.environ["MKL_THREADING_LAYER"] = "GNU"
print("3..")
from transformers import AutoConfig
print("4..")
# Path to the model directory
model_path = "../converted_file/pytorch_model.bin"
print("5..")
# Use AutoConfig to detect model type
try:
    config = AutoConfig.from_pretrained(model_path)
    print(f"Detected model type: {config.model_type}")
except Exception as e:
    print(f"Could not detect model type: {e}")