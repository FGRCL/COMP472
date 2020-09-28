import numpy as np
import csv
import matplotlib.pyplot as plt
import argparse

def main(csvDataset):
    parser = argparse.ArgumentParser(description='Plot dataset')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

    dataset = np.loadtxt(csvDataset, delimiter=',')
    plotDataset(dataset)
    
def plotDataset(dataset):
    labels = [point[len(point)] for point in dataset]
    buckets = np.zeros(max(labels))
    for label in labes:
        buckets[label] += 1
    plt.plot(np.arrange(buckets), buckets)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='plot a dataset')
    parser.add_argument('--dataset', metavar='path', required=True, help='the path to dataset')
    main(args.dataset)