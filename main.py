import torch 
import numpy as np


def cudaIsAvailable():
    available = torch.cuda.is_available()
    print(f"CUDA available: {available}")
    return available
def pipelineTest(value):
    print("running pipeline...")
    if cudaIsAvailable():
        result = torch.Tensor([1,2,3]).float().cuda()+ value 
        result = result.cuda()
    else:
        result = torch.Tensor([1,2,3]).float()+ value 
    result = result.cpu().numpy()
    print("done!")
    return result

if __name__ == "__main__":
    pipelineTest(1)