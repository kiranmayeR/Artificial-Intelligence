import torch
import torch.nn as nn
class simulatedann(nn.Module):
    def __init__(self,idim,odim):
        super(simulatedann,self).__init__()
        self.linear=nn.Linear(idim,odim)
    def simulatedanni(self,x):
        out=self.linear(x)
        return out 
idim=28*28
odim=10
m=simulatedann(idim,odim)
print(m)
