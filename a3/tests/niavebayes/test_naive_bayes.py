from a3.naibebayes.datapoint import Datapoint
from a3.naibebayes.naive_bayes import NaiveBayes


def test_naive_bayes():
    datapoints = [
        Datapoint(("test", "mother", "ship"), True),
        Datapoint(("test", "mother", "land"), False)
    ]
    bayesClassifier = NaiveBayes()
    bayesClassifier.train(datapoints)

    document_to_predict = ("test", "mother", "ship")

    result = bayesClassifier.predict(document_to_predict)

    assert result[1] == True

    document_to_predict = ("test", "mother", "land")

    result = bayesClassifier.predict(document_to_predict)

    assert result[1] == False

    document_to_predict = ("test", "mother")

    result = bayesClassifier.predict(document_to_predict)

    assert result[1] == True

