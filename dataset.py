import torch.utils.data.dataset as Dataset
import numpy as np
import json

class CSVDataset(Dataset):
    # load the dataset
    def __init__(self, path):
        try:
            with open(path, 'r') as json_file:
                data_dict = json.load(json_file)
        except FileNotFoundError:
            # The file doesn't exist, so we catch the `FileNotFoundError` exception and initialize an empty dictionary.
            pass
        # store the inputs and outputs
        
        data = np(list(data_dict.values()))
        
        self.X = data[:,0]
        self.y = data[:,1]

    # number of rows in the dataset
    def __len__(self):
        return len(self.X)

    # get a row at an index
    def __getitem__(self, idx):
        return [self.X[idx], self.y[idx]]