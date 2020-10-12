from a1 import naivebayes, basedt, bestdt, perceptron, basemlp, bestmlp
from enum import Enum

class modeltype(Enum):
    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, val, create_model_lambda): # I'd rather put "name" than "alias" but "name" is already reserved by some other python thing
        self.val = val
        self.create_model_lambda = create_model_lambda

    @staticmethod
    def from_string(string):
        return modeltype[string]

    bayes = 1, lambda training_dataset, features, labels: naivebayes.train_model(training_dataset, features, labels)
    basedt = 2, lambda training_dataset, features, labels: basedt.train_model(training_dataset, features, labels)
    bestdt = 3, lambda training_dataset, features, labels: bestdt.train_model(training_dataset, features, labels)
    perceptron = 4, lambda training_dataset, features, labels: perceptron.train_model(training_dataset, features, labels)
    basemlp = 5, lambda training_dataset, features, labels: basemlp.train_model(training_dataset, features, labels)
    bestmlp = 6, lambda training_dataset, features, labels: bestmlp.train_model(training_dataset, features, labels)

modeltype.from_string = staticmethod(modeltype.from_string)