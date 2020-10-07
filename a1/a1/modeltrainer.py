import argparse
import util
import naivebayes
import basedt
import perceptron
import basemlp

from enum import Enum

class Model(Enum):
    bayes = 'bayes'
    basedt = 'basetree'
    perceptron = 'perceptron'
    basemlp = 'baseMLP'


def main(training_dataset, model_enum):
    training_dataset_matrix = util.csv_to_nparray(training_dataset)
    features, labels = util.split_features_and_labels(training_dataset_matrix)

    if(model_enum == Model.bayes):
        model = naivebayes.train_model(features, labels)
    elif(model_enum == Model.basedt):
        model = basedt.train_model(features, labels)
    elif(model_enum == Model.perceptron):
        model = perceptron.train_model(features, labels)
    elif(model_enum == Model.basemlp):
        model = basemlp.train_model(features, labels)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Model trainer', description='An AI model trainer')
    parser.add_argument('--trainingset', metavar='path', required=True, help='the path to training set', )
    parser.add_argument('--model',
        type=Model,
        choices=Model,
        required=True,
        dest='model_enum',
        help='The model to train'
    )
    args = parser.parse_args()
    main(args.trainingset, args.model_enum)

