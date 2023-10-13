from torch.utils.data import Dataset
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
        
        """TODO whats the best way to store the data in the CSVDataset??
        what does the Dataloader class expect?"""
        self.X = np.empty([0,4])
        self.Y = np.empty([0,2])
        
        for dict in data_dict.values():
            dv = dict.values()
            l_dv = list(dv)
            for l in l_dv:
                new_feature_list = [l[0][0],l[0][1],l[0][2][0],l[0][2][1]]
                new_feature_np_array = np.array(new_feature_list)
                label_np_array = np.array(l[1]) 
                np.append(self.X, new_feature_np_array) #BUG append doesnt work
                np.append(self.Y, label_np_array)

    # number of rows in the dataset
    def __len__(self):
        return len(self.X)

    # get a row at an index
    def __getitem__(self, idx):
        return [self.X[idx], self.y[idx]]