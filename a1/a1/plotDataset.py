import numpy as np
import matplotlib.pyplot as plt
import argparse


def main(csv_dataset):
    dataset = np.loadtxt(csv_dataset, delimiter=',', dtype=int)
    plot_dataset(dataset)


def plot_dataset(dataset):
    labels = [point[len(point) - 1] for point in dataset]
    buckets = np.zeros(max(labels) + 1)
    for label in labels:
        buckets[label] += 1
    display_bargraph(np.arange(len(buckets)), buckets)


def display_bargraph(categories, values):
    plt.bar(categories, values)
    plt.xticks(categories, categories)
    plt.xlabel('Label ID')
    plt.ylabel('# of occurrence in dataset')
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='plot a dataset')
    parser.add_argument('--dataset', metavar='path', required=True, help='the path to dataset')
    args = parser.parse_args()
    main(args.dataset)
