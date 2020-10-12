from sklearn.naive_bayes import GaussianNB

def train_model(training_dataset, features, labels):
    model = GaussianNB()
    model.fit(features, labels)
    return model