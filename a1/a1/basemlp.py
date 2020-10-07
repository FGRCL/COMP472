from sklearn.neural_network import MLPClassifier

def train_model(features, labels):
    model = MLPClassifier((100), 'logistic', 'sgd')
    model.fit(features, labels)
    return model