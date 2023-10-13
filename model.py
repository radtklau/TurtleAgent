import torch.nn as nn
import torch.nn.functional as F

class LR_Model(nn.Module):
    def __init__(self):
        super(LR_Model, self).__init__()
        self.layer = nn.Linear(3, 2)  # Three inputs and two outputs
        self.activation = F.sigmoid()

    def forward(self, x):
        out = self.activation(self.linear(x))
        return out