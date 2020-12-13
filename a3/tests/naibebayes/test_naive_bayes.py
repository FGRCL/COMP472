from a3.naivebayes.datapoint import Datapoint
from a3.naivebayes.naive_bayes import NaiveBayes


def test_naive_bayes():
    datapoints = [
        Datapoint({"test": 1, "mother": 1, "ship": 1}, "yes"),
        Datapoint({"test": 1, "mother": 1, "land": 1}, "no")
    ]
    bayes_classifier = NaiveBayes()
    bayes_classifier.train(datapoints)

    document_to_predict = ("test", "mother", "ship")

    result = bayes_classifier.predict(document_to_predict)

    assert result[1] == "yes"

    document_to_predict = ("test", "mother", "land")

    result = bayes_classifier.predict(document_to_predict)

    assert result[1] == "no"

    document_to_predict = ("test", "mother")

    result = bayes_classifier.predict(document_to_predict)

    assert result[1] == "yes"
