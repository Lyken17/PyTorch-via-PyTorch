import torch
# from lltm.jit import lltm_cpp
from addition.jit import add_cpp

a = torch.randn(3, requires_grad=True)
b = torch.randn(3, requires_grad=True)

c = add_cpp.forward(a, b)
d = a + b

print(c[0])
print(d)

grad_outputs = torch.randn(d.size())
th_grads = torch.autograd.grad(d, (a, b), grad_outputs=grad_outputs, create_graph=True)

my_grads = add_cpp.backward(grad_outputs)
print(grad_outputs)
print("PyTorch Results:", th_grads[1])
print("Myimplt Results:", my_grads[1])
