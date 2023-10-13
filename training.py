from dataset import CSVDataset
from torch.utils.data import DataLoader, random_split

if __name__ == "__main__":
    file_path = 'data/training_0.json'
    dataset = CSVDataset(file_path)
    train_size = int(0.8 * len(dataset)) 
    test_size = len(dataset) - train_size  
    train, test = random_split(dataset, [train_size, test_size])
    
    train_dl = DataLoader(train, batch_size=32, shuffle=True)
    test_dl = DataLoader(test, batch_size=1024, shuffle=False)
    