from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from a1 import util

# Grid search hyperparameters
# I'm guessing it has to do with the combination of all 3 parameters but sometimes 
# we get "ConvergenceWarning: <ACTIVATION_TYPE>: Maximum iterations (200) reached and the optimization hasn't converged yet."
param_grid = {
    'activation' : ['logistic', 'tanh', 'relu', 'identity'], # Requirement (Note: logistic == sigmoid)
    'hidden_layer_sizes' : [(30, 50), (10, 10, 10)], # Values of our choice
    'solver' : ['adam', 'sgd'] # Requirement
}

# This takes a very long time to run 
def train_model(training_dataset, features, labels):
    gridSearch = GridSearchCV(MLPClassifier(), param_grid, verbose=5) # Change verbose size for more or less console output
    gridSearch.fit(features, labels)

    # You can uncomment the following to see detailed results

    # print(gridSearch.best_estimator_)
    # print(gridSearch.best_params_)
    # print(gridSearch.cv_results_)
    # print(gridSearch.best_score_)

    return gridSearch