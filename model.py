import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch

class LR_Model(nn.Module):
    def __init__(self):
        super(LR_Model, self).__init__()
        self.layer = nn.Linear(3, 2)  # Three inputs and two outputs
        print(self.layer.weight.dtype)
        self.activation = F.sigmoid

    def forward(self, x):
        print(x.dtype)
        x = x.to(torch.float32)
        out = self.activation(self.layer(x))
        print(out.dtype)
        return out