import numpy as np
import os

def csv_to_nparray(csv_dataset):
    return np.loadtxt(csv_dataset, delimiter=',', dtype=int)

def split_features_and_labels(dataset):
    length = len(dataset[0])
    samples = dataset[:,0:length-1]
    labels = dataset[:,length-1]
    return samples, labels

def parse_dataset(csv_dataset):
    return split_features_and_labels(csv_to_nparray(csv_dataset))

def parseFileName(training_dataset_file):
    (head, tail) = os.path.split(training_dataset_file)
    return tail[0:tail.index('.')]
