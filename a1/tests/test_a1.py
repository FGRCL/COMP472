from a1 import __version__
from os import path
from a1.modelenum import modeltype
from a1.main import main

#Yeah they're pretty terrible tests but it's better than nothing
def test_bayes():
    # given
    output_file = 'testresults/bayes.txt'

    # when
    main('dataset/train_1.csv', 'dataset/test_with_label_1.csv', modeltype.bayes, output_file)

    # then
    assert path.exists(output_file)
    with open(output_file, 'r') as f:
        assert f.read()

def test_basedt():
    # given
    output_file = 'testresults/basedt.txt'

    # when
    main('dataset/train_1.csv', 'dataset/test_with_label_1.csv', modeltype.basedt, output_file)

    # then
    assert path.exists(output_file)
    with open(output_file, 'r') as f:
        assert f.read()

def test_perceptron():
    # given
    output_file = 'testresults/perceptron.txt'

    # when
    main('dataset/train_1.csv', 'dataset/test_with_label_1.csv', modeltype.perceptron, output_file)

    # then
    assert path.exists(output_file)
    with open(output_file, 'r') as f:
        assert f.read()


def test_basemlp():
    # given
    output_file = 'testresults/basemlp.txt'

    # when
    main('dataset/train_1.csv', 'dataset/test_with_label_1.csv', modeltype.basemlp, output_file)

    # then
    assert path.exists(output_file)
    with open(output_file, 'r') as f:
        assert f.read()
