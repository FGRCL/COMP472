from a1 import naivebayes, basedt, perceptron, basemlp
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

    def from_string(string):
        return modeltype[string]

    bayes = 1, lambda features, labels: naivebayes.train_model(features, labels)
    basedt = 2, lambda features, labels: basedt.train_model(features, labels)
    perceptron = 3, lambda features, labels: perceptron.train_model(features, labels)
    basemlp = 4, lambda features, labels: basemlp.train_model(features, labels)

