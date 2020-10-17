from a1 import __version__
from os import path, mkdir
from shutil import rmtree
from a1.modelenum import modeltype
from a1.main import main

output_file_path = "test_out/out.txt"
training_file = "test_dataset/train.csv"
test_file = "test_dataset/test.csv"

def setup_module(module):
    mkdir("test_dataset")
    mkdir("test_out")

    with open(training_file, 'w') as train:
        for i in range(10):
            train.write("1,1,1\n")
            train.write("0,0,0\n")

    with open(test_file, 'w') as test:
        for i in range(10):
            test.write("1,1,1\n")
            test.write("0,0,0\n")


def teardown_module(module):
    rmtree("test_dataset")
    rmtree("test_out")

def test_bayes():
    #given
    output_file = open(output_file_path, "w")

    # when
    main(training_file, test_file, modeltype.bayes, output_file)

    # then
    assert path.exists(output_file_path)
    with open(output_file_path, 'r') as f:
        assert f.read()

def test_basedt():
    # given
    output_file = open(output_file_path, "w")

    # when
    main(training_file, test_file, modeltype.basedt, output_file)

    # then
    assert path.exists(output_file_path)
    with open(output_file_path, 'r') as f:
        assert f.read()

def test_bestdt():
    # given
    output_file = open(output_file_path, "w")

    # when
    main(training_file, test_file, modeltype.basedt, output_file)

    # then
    assert path.exists(output_file_path)
    with open(output_file_path, 'r') as f:
        assert f.read()


def test_perceptron():
    # given
    output_file = open(output_file_path, "w")

    # when
    main(training_file, test_file, modeltype.perceptron, output_file)

    # then
    assert path.exists(output_file_path)
    with open(output_file_path, 'r') as f:
        assert f.read()


def test_basemlp():
    # given
    output_file = open(output_file_path, "w")

    # when
    main(training_file, test_file, modeltype.basemlp, output_file)

    # then
    assert path.exists(output_file_path)
    with open(output_file_path, 'r') as f:
        assert f.read()

def test_bestmlp():
    # given
    output_file = open(output_file_path, "w")

    # when
    main(training_file, test_file, modeltype.bestmlp, output_file)

    # then
    assert path.exists(output_file_path)
    with open(output_file_path, 'r') as f:
        print("file conent {}".format(f.read()))
        assert f.read()