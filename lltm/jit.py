import os, os.path as osp
from torch.utils.cpp_extension import load

dir_path = os.path.dirname(os.path.realpath(__file__))
lltm_cpp = load(
    name="lltm_cpp", 
    sources=[osp.join(dir_path, "lltm.cpp")], 
    extra_cflags=['-O2'],
    verbose=True
)


# Example usage
# from lltm.jit import lltm_cpp

