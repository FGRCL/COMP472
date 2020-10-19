import numpy as np
from sklearn.model_selection import PredefinedSplit
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import GridSearchCV
from a1 import util


# Grid search hyperparameters
param_grid = {
    'criterion' : ['gini', 'entropy'], # Requirement
    'max_depth' : [None, 10], # Requirement
    'min_samples_split' : np.arange(2, 6, 1, dtype=int), # Values of our choice. favorites: dataset1: 4  dataset2: 2
    'min_impurity_decrease' : np.arange(0.0, 0.1, 0.01, dtype=float), # Values of our choice 0.0
    'class_weight' : [None, 'balanced'] # Requirement
}

# Best model after running grid search
# Training set 1
#   Criterion : gini, 
#   Max Depths : None
#   Min Impurity Decrease : 0.0
#   Min Samples Split : 3
#   Class Weight : None

# Training set 2 
#   Criterion : entropy, 
#   Max Depths : None
#   Min Impurity Decrease : 0.0
#   Min Samples Split : 3
#   Class Weight : None
def train_model(training_dataset, features, labels):
    model = DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=None, min_impurity_decrease=0.0, min_samples_split=2) # Change verbose size for more or less console output
    model.fit(features, labels)
    return model

def perform_grid_search(features, labels, validation_features, validation_labels):
    all_features = np.concatenate([features, validation_features])
    all_labels = np.concatenate([labels, validation_labels])


    test_fold = [-1 for _ in features] + [0 for _ in validation_features]
    cv = PredefinedSplit(test_fold)

    gridSearch = GridSearchCV(DecisionTreeClassifier(), param_grid, verbose=5, cv=cv)  # Change verbose size for more or less console output
    gridSearch.fit(all_features, all_labels)

    return gridSearch


