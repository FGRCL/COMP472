import argparse
from a1 import util
from a1.modelenum import modeltype

def main(training_dataset, model_enum):
    training_dataset_matrix = util.csv_to_nparray(training_dataset)
    features, labels = util.split_features_and_labels(training_dataset_matrix)

    model = model_enum.create_model_lambda(features, labels)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Model trainer', description='An AI model trainer')
    parser.add_argument('--trainingset', metavar='path', required=True, help='the path to training set', )
    parser.add_argument('--model',
        type=modeltype.from_string,
        choices=modeltype,
        required=True,
        dest='model_enum',
        help='The model to train'
    )
    args = parser.parse_args()
    main(args.trainingset, args.model_enum)

