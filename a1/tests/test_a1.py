from a1 import __version__
from a1.modelenum import modeltype
from a1.main import main

#Yeah they're pretty terrible tests but it's better than nothing
def test_bayes():
    main('dataset/train_1.csv', modeltype.bayes)
    assert True

def test_basedt():
    main('dataset/train_1.csv', modeltype.basedt)
    assert True

def test_perceptron():
    main('dataset/train_1.csv', modeltype.perceptron)
    assert True

def test_basemlp():
    main('dataset/train_1.csv', modeltype.basemlp)
    assert True
