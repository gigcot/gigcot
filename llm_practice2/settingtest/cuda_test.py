# import torch

# def check_cuda():
#     print(f"PyTorch version: {torch.__version__}")

#     # Check if CUDA is available
#     cuda_available = torch.cuda.is_available()
#     print(f"CUDA is available: {cuda_available}")

#     if cuda_available:
#         # Get the name of the current GPU device
#         device_name = torch.cuda.get_device_name(0)
#         print(f"Current GPU device: {device_name}")

#         # Get the current device ID
#         current_device = torch.cuda.current_device()
#         print(f"Current device ID: {current_device}")

#         # Check GPU memory usage
#         allocated_memory = torch.cuda.memory_allocated(0) / 1024**3
#         cached_memory = torch.cuda.memory_reserved(0) / 1024**3
#         print(f"Allocated GPU memory: {allocated_memory:.2f} GB")
#         print(f"Cached GPU memory: {cached_memory:.2f} GB")

#         # Perform a simple CUDA tensor operation
#         x = torch.rand(3, 3).cuda()
#         y = torch.rand(3, 3).cuda()
#         z = x + y
#         print("CUDA tensor operation result:\n", z)

# if __name__ == "__main__":
#     check_cuda()
import torch
print(torch.version.cuda)
print(torch.__version__)
device_name = torch.cuda.get_device_name(0)
print(f"Current GPU device: {device_name}")
print(torch.version.cuda)
print(torch.cuda.is_available())
