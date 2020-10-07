from sklearn.tree import DecisionTreeClassifier

def train_model(features, labels):
    model = DecisionTreeClassifier()
    model.fit(features, labels)
    return model