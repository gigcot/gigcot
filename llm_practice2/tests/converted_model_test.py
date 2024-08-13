import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["MKL_THREADING_LAYER"] = "GNU"
import json
import torch
# Load model configuration
with open('../converted_file/config.json', 'r') as f:
    config = json.load(f)

# Load tokenizer configuration
with open('../converted_file/tokenizer_config.json', 'r') as f:
    tokenizer_config = json.load(f)

# Load the PyTorch model state_dict
model_path = '../converted_file/pytorch_model.bin'
model = torch.load(model_path, map_location=torch.device('cpu'))

# Check the model parameters
model_checks = {
    "architecture": config['architecture'],
    "n_layer": config['n_layer'],
    "n_head": config['n_head'],
    "dim": config['dim'],
    "intermediate_size": config['intermediate_size']
}

# Validate state_dict against config.json
layer_count_check = all(config['n_layer'] in name for name in model.keys() if 'layer' in name)
head_count_check = all(config['n_head'] in name for name in model.keys() if 'head' in name)

# Check vocab size consistency
vocab_size_check = len(tokenizer_config['added_tokens_decoder']) <= config['vocab_size']

# Validate token IDs in tokenizer_config.json
token_id_check = all(int(token_id) < config['vocab_size'] for token_id in tokenizer_config['added_tokens_decoder'])

# Compile results
results = {
    "model_checks": model_checks,
    "layer_count_check": layer_count_check,
    "head_count_check": head_count_check,
    "vocab_size_check": vocab_size_check,
    "token_id_check": token_id_check
}

print(results)
