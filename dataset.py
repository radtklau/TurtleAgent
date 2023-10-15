from torch.utils.data import Dataset
import numpy as np
import json
import torch

class CSVDataset(Dataset):
    # load the dataset
    def __init__(self, path):
        try:
            with open(path, 'r') as json_file:
                data_dict = json.load(json_file)
        except FileNotFoundError:
            # The file doesn't exist, so we catch the `FileNotFoundError` exception and initialize an empty dictionary.
            pass
        
        """TODO whats the best way to store the data in the CSVDataset??
        what does the random_split() expect?"""

        
        for ind, dict in enumerate(data_dict.values()):
            dv = dict.values()
            l_dv = list(dv)
            for ind2, l in enumerate(l_dv):
                if ind == 0 and ind2 == 0:
                    new_feature_list = [l[0][0],l[0][1],l[0][2][0],l[0][2][1]]
                    new_feature_np_array = np.array(new_feature_list)
                    label_np_array = np.array(l[1]) 
                    self.X = np.expand_dims(new_feature_np_array, axis=0)
                    self.Y = np.expand_dims(label_np_array, axis=0) 
                else:
                    new_feature_list = [l[0][0],l[0][1],l[0][2][0],l[0][2][1]]
                    new_feature_np_array = np.expand_dims(np.array(new_feature_list), axis=0)
                    label_np_array = np.expand_dims(np.array(l[1]), axis=0)
                    self.X = np.concatenate((self.X, new_feature_np_array), axis=0)
                    self.Y = np.concatenate((self.Y, label_np_array), axis=0)
                    
        self.X = torch.tensor(self.X, dtype=torch.float32)
        self.Y = torch.tensor(self.Y, dtype=torch.float32)

    # number of rows in the dataset
    def __len__(self):
        return len(self.X)

    # get a row at an index
    def __getitem__(self, idx):
        return [self.X[idx], self.Y[idx]]