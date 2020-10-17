import argparse
import sys
from a1 import util
from a1.modelenum import modeltype
from sklearn.metrics import confusion_matrix
import pandas as pd

def main(training_dataset, test_dataset, model_enum, output_file):
    features, labels = util.parse_dataset(training_dataset)
    input, expected_labels = util.parse_dataset(test_dataset)

    model = model_enum.create_model_lambda(training_dataset, features, labels)
    predictions = model.predict(input)
    confusion = confusion_matrix(expected_labels, predictions)
    write_result_to_file(output_file, predictions, confusion)


def write_result_to_file(output_file, predictions, confusion):
    for pair in zip(range(len(predictions)), predictions):
        print('{},{}'.format(pair[0], pair[1]), file=output_file)
    print('confusion matrix:\n{}'.format(pd.DataFrame(confusion)), file=output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Model trainer', description='An AI model trainer')
    parser.add_argument('--trainingset', '-tr', metavar='training set path', required=True, help='the path to training set', )
    parser.add_argument('--testset', '-ts', metavar='test set path', required=True, help='the path to test set', )
    parser.add_argument('--output', '-o', metavar='the path to the ouput file', required=False, help='the path to training set', default=sys.stdout)
    parser.add_argument('-m', '--model',
        type=modeltype.from_string,
        choices=modeltype,
        required=True,
        dest='model_enum',
        help='The model to train'
    )
    args = parser.parse_args()
    output_file = args.output
    if type(args.output) is str:
        output_file = open(args.output, 'w')
    main(args.trainingset, args.testset, args.model_enum, output_file)

