from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import GridSearchCV
from a1 import util

# Grid search hyperparameters
param_grid = {
    'criterion' : ['gini', 'entropy'], # Requirement
    'max_depth' : [None, 10], # Requirement
    'min_samples_split' : [0.5, 1.0], # Values of our choice
    'min_impurity_decrease' : [0.0, 0.1, 0.5], # Values of our choice
    'class_weight' : [None, 'balanced'] # Requirement
}

def train_model(training_dataset, features, labels):
    
    fileName = util.parseFileName(training_dataset)
    gridSearch = GridSearchCV(DecisionTreeClassifier(), param_grid, verbose=5) # Change verbose size for more or less console output
    gridSearch.fit(features, labels)

    # Creating a grpah 
    # To run, I installed graphviz using poetry
    # Then to convert .dot file to png run $ dot -Tpng BestDT.dot -o BestDT.png   
    export_graphviz(
        gridSearch.best_estimator_,
        out_file=("../exports/"+fileName+"-BestDT.dot"),
        filled=True
    )
    
    # You can uncomment the following to see detailed results

    # print(gridSearch.best_estimator_)
    # print(gridSearch.best_params_)
    # print(gridSearch.cv_results_)

    return gridSearch