from sklearn.linear_model import Perceptron

def train_model(features, labels):
    model = Perceptron()
    model.fit(features, labels)
    return model