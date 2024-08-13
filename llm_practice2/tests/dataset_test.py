from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
dataset = load_dataset('csv', data_files='../qa_data.csv')

def tokenize_function(examples):
    return tokenizer(examples['질문'], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
