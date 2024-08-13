import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["MKL_THREADING_LAYER"] = "GNU"
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, LlamaForCausalLM, LlamaTokenizer
from datasets import load_dataset
from peft import LoraConfig#, Trainer, TrainingArguments
from transformers import Trainer, TrainingArguments
import logging
# 환경 변수 설정
logging.basicConfig(level=logging.DEBUG)
logging.debug("Starting the script...")

# 모델 파일과 토크나이저의 절대 경로를 생성
base_path = "gigcot/first_proj"
# model_file = "pytorch_model.bin"
print("1...")
# 절대 경로 조합
# model_path = os.path.join(base_path, model_file)
# model_path = os.path.join("dddd")
model_path = "ggml-model-Q5_K_M.gguf"
# tokenizer_path = base_path
print("2...")
# 경로 존재 여부 확인
# if not os.path.exists(model_path):
#     raise FileNotFoundError(f"Model file not found: {model_path}")
# print("2-1...")
# 모델 및 토크나이저 로드
try:
    model = AutoModelForCausalLM.from_pretrained(
    base_path,
    gguf_file=model_path,
    torch_dtype=torch.float16,   # Optional: use float16 to reduce memory usage
    device_map='auto'           # Optional: automatically choose CPU/GPU
)
    # model = LlamaForCausalLM.from_pretrained(tokenizer_path)
    print("3...")
    tokenizer = AutoTokenizer.from_pretrained(base_path, gguf_file=model_path)
    # tokenizer = LlamaTokenizer.from_pretrained(tokenizer_path)
    print("모델 및 토크나이저 로드 성공")
except Exception as e:
    logging.error(f"모델 로드 실패: {e}")
print("4...")
# 데이터셋 로드
dataset = load_dataset('csv', data_files='../qa_data.csv')
print("5...")
def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True)
tokenized_datasets = dataset.map(tokenize_function, batched=True)
print("6...")
# # 데이터셋 분할
# train_test_split = tokenized_datasets['train'].train_test_split(test_size=0.1)
# train_dataset = train_test_split['train']
# eval_dataset = train_test_split['test']
# DoRA 설정 초기화
config = LoraConfig(use_dora=True)
print("7...")
# 훈련 인자 설정
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=1e-5,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    gradient_accumulation_steps=4,
    num_train_epochs=3,
    weight_decay=0.01,
    fp16=True
)
print("8...")
# 트레이너 초기화 및 훈련
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    config=config
)
try:
    trainer.train()
except Exception as e:
    logging.error(f"Training failed: {e}")

# 모델 저장
trainer.save_model("fine-tuned-model")
