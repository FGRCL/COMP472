import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from a1 import util

# Grid search hyperparameters
# I'm guessing it has to do with the combination of all 3 parameters but sometimes 
# we get "ConvergenceWarning: <ACTIVATION_TYPE>: Maximum iterations (200) reached and the optimization hasn't converged yet."

# Test set #1
# nodes > layers
# adam > sgd
# Logistic is better
# best -> logistic, 500, adam

param_grid = {
    'activation' : ['logistic', 'tanh', 'relu', 'identity'], # Requirement (Note: logistic == sigmoid)
    'hidden_layer_sizes' : [(5,5,5,5,5), (10, 10, 10), (30, 50), (200, 200), (500,)], # Values of our choice
    'solver' : ['adam', 'sgd'] # Requirement
}

# This takes a very long time to run 
def train_model(training_dataset, features, labels):
    model = MLPClassifier((500), solver='adam', activation='tanh')
    model.fit(features, labels)
    return model

def perform_grid_search(features, labels, validation_features, validation_labels):
    all_features = np.concatenate([features, validation_features])
    all_labels = np.concatenate([labels, validation_labels])

    test_fold = [-1 for _ in features] + [0 for _ in validation_features]
    cv = PredefinedSplit(test_fold)

    gridSearch = GridSearchCV(MLPClassifier(), param_grid, verbose=5, cv=cv)  # Change verbose size for more or less console output
    gridSearch.fit(all_features, all_labels)

    return gridSearch
