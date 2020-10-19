import argparse
from a1 import util
from sklearn.tree import export_graphviz
from a1.modelenum import modeltype


def main(model, trainingset, validationset, graphoutput):
    features, labels = util.parse_dataset(trainingset)
    validation_features, validation_labels = util.parse_dataset(validationset)

    gridSearch = model.perform_grid_search_lambda(features, labels, validation_features, validation_labels)

    # Creating a grpah
    # To run, I installed graphviz using poetry
    # Then to convert .dot file to png run $ dot -Tpng BestDT.dot -o BestDT.png
    if graphoutput is not None:
        export_graphviz(
            gridSearch.best_estimator_,
            out_file=(graphoutput),
            filled=True
        )

    print(gridSearch.best_estimator_)
    print(gridSearch.best_params_)
    # print(gridSearch.cv_results_)
    print(gridSearch.best_score_)
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Model trainer', description='An AI grid searcher')
    parser.add_argument('--trainingset', '-tr', metavar='training set path', required=True, help='the path to training set', )
    parser.add_argument('--validationset', '-vs', metavar='validation set path', required=True, help='the path to the validation set', )
    parser.add_argument('--graphoutput', '-go', metavar='output for the graph')
    parser.add_argument('-m', '--model',
        type=modeltype.from_string,
        choices=modeltype,
        required=True,
        dest='model_enum',
        help='The model to train'
    )

    args = parser.parse_args()
    main(args.model_enum, args.trainingset, args.validationset, args.graphoutput)