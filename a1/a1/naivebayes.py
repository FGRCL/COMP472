from sklearn.naive_bayes import GaussianNB
import argparse
import util

def main(training_dataset):
    training_dataset_matrix = util.csv_to_nparray(training_dataset)
    features, labels = util.split_features_and_labels(training_dataset_matrix)

    model = train_model(features, labels)

def train_model(features, labels):
    model = GaussianNB()
    model.fit(features, labels)
    return model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gaussian Naive Bayes Classifier')
    parser.add_argument('--trainingset', metavar='path', required=True, help='the path to training set')
    args = parser.parse_args()
    main(args.trainingset)