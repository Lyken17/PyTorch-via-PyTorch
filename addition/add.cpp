#include <torch/extension.h>
#include <vector>
#include <iostream>
#include <cassert>


std::vector<torch::Tensor> add_forward(
    torch::Tensor inputA,
    torch::Tensor inputB
){
  // assert inputA.dim() == inputB.dim(); 
  // assert inputA.size() == inputB.size();
  return {inputA + inputB};
}

std::vector<torch::Tensor> add_backward(
    torch::Tensor grad_outputs
){
  return {
    torch::ones_like(grad_outputs) * grad_outputs, 
    torch::ones_like(grad_outputs) * grad_outputs
  };
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("forward", &add_forward, "Addition forward");
  m.def("backward", &add_backward, "Addition backward");
}