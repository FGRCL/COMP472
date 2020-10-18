import argparse
import sys
from a1 import util
from a1.modelenum import modeltype
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, accuracy_score, f1_score
import pandas as pd

def main(training_dataset, test_dataset, model_enum, output_file):
    features, labels = util.parse_dataset(training_dataset)
    input, expected_labels = util.parse_dataset(test_dataset)

    model = model_enum.create_model_lambda(training_dataset, features, labels)
    predictions = model.predict(input)
    confusion = confusion_matrix(expected_labels, predictions)
    metrics = precision_recall_fscore_support(expected_labels, predictions, average=None)
    accuracy = accuracy_score(expected_labels, predictions)
    f1_macro = f1_score(expected_labels, predictions, average='macro')
    f1_weighted = f1_score(expected_labels, predictions, average='weighted')

    # Output
    write_result_to_file(output_file, predictions, confusion, metrics, accuracy, f1_macro, f1_weighted)


def write_result_to_file(output_file, predictions, confusion, metrics, accuracy, f1_macro, f1_weighted):

    # Predicted Class
    generate_predicted_class(output_file, predictions)
    
    # Confusion Matrix
    generate_confusion_matrix(output_file, confusion)

    # Class Metrics
    generate_class_metrics(output_file, metrics)

    # Model Metrics
    generate_model_metrics(output_file, accuracy, f1_macro, f1_weighted)

def generate_predicted_class(output_file, predictions):
    print('=================================', file=output_file)
    print('PREDICTED CLASSIFICATION', file=output_file)
    print('=================================', file=output_file)
    print('', file=output_file)
    for pair in zip(range(len(predictions)), predictions):
        print('{},{}'.format(pair[0], pair[1]), file=output_file)


def generate_confusion_matrix(output_file, confusion):
    print('', file=output_file)
    print('=================================', file=output_file)
    print('CONFUSION MATRIX', file=output_file)
    print('=================================', file=output_file)
    print('', file=output_file)

    pd.DataFrame(confusion).to_csv(output_file, mode='a', header='false')


def generate_class_metrics(output_file, metrics):
    metric_type = ["PRECISION", "RECALL", "F-MEASURE", "SUPPORT (# of occurences of each expected label)"]

    for index, metric in enumerate(metrics):
            print('', file=output_file)
            print('=================================', file=output_file)
            print(metric_type[index], file=output_file)
            print('=================================', file=output_file)
            print('', file=output_file)
            for pair in zip(range(len(metric)), metric):
                print('{},{}'.format(pair[0], pair[1]), file=output_file)

def generate_model_metrics(output_file, accuracy, f1_macro, f1_weighted) :
    print('', file=output_file)
    print('=================================', file=output_file)
    print('MODEL METRICS', file=output_file)
    print('=================================', file=output_file)
    print('', file=output_file)

    print('{},{}'.format("ACCURACY", accuracy), file=output_file)
    print('', file=output_file)
    print('{},{}'.format("MACRO-AVERAGE F1-MEASURE", f1_macro), file=output_file)
    print('', file=output_file)
    print('{},{}'.format("WEIGHTED-AVERAGE F1-MEASURE", f1_weighted), file=output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Model trainer', description='An AI model trainer')
    parser.add_argument('--trainingset', '-tr', metavar='training set path', required=True, help='the path to training set', )
    parser.add_argument('--testset', '-ts', metavar='test set path', required=True, help='the path to test set', )
    parser.add_argument('--output', '-o', metavar='the path to the ouput file', required=False, help='the path to output file', default=sys.stdout)
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

