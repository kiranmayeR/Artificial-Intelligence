import torch
import torch.nn as nn
class feedforward(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(feedforward, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        out = self.linear(x)
        return out
input_dim = 28*28
output_dim = 10

model = feedforward(input_dim, output_dim)
print(model)
