import os, os.path as osp
from torch.utils import cpp_extension

dir_path = os.path.dirname(os.path.realpath(__file__))
add_cpp = cpp_extension.load(
    name="add_cpp", 
    sources=[osp.join(dir_path, "add.cpp")], 
    extra_cflags=['-O2'],
    verbose=True)

# import torch.nn as nn
# from torch import autograd

# class AddFunction(autograd.Function):
#     @staticmethod
#     def forward(ctx, input_a, input_b):
#         return add_cpp.forward(input_a, input_b)

#     @staticmethod
#     def backward(ctx, grad_outputs):
#         return add_cpp.backward(grad_outputs)


# class MyAdd(nn.Module):
#     def __init__(self):
#         super(self, MyAdd).__init__()
    
#     def forward(self, x, y):
#         return AddFunction.apply(x, y)