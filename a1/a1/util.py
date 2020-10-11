import numpy as np

def csv_to_nparray(csv_dataset):
    return np.loadtxt(csv_dataset, delimiter=',', dtype=int)

def split_features_and_labels(dataset):
    length = len(dataset[0])
    samples = dataset[:,0:length-2]
    labels = dataset[:,length-1]
    return samples, labels