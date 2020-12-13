from a3.naivebayes.datapoint import Datapoint
from a3.parser.tokenizer import parse_file, tweet_to_datapoints, filter_vocabulary


def test_get_datapoints_from_file():
    result = parse_file("in/covid_training.tsv")

    expected_text = ["for", "the", "average", "american", "the", "best", "way", "to", "tell", "if", "you", "have",
                     "covid-19", "is", "to", "cough", "in", "a", "rich", "person’s", "face", "and", "wait", "for",
                     "their", "test", "results"]
    element = next(result)
    assert element[0] == '1241025578527903750'
    assert element[1] == expected_text
    assert element[2] == "no"


def test_tweet_to_datapoints():
    tweets = [
        (
            '1241025578527903750',
            ["the", "the", "test", "the", "result", "covid", "the", "result"],
            "no"
        )
    ]

    tweet_generator = (tweet for tweet in tweets)

    result = tweet_to_datapoints(tweet_generator)

    element = next(result)
    assert element.features == {"the": 4, "test": 1, "result": 2, "covid": 1}
    assert element.label == "no"


def test_filter_vocabulary():
    datapoints = [
        Datapoint({"the": 4, "test": 1, "result": 2, "covid": 1}, "no")
    ]

    datapoint_generator = (datapoint for datapoint in datapoints)

    result = filter_vocabulary(datapoint_generator, 2)

    element = next(result)
    assert element.features == {"the": 4, "result": 2}
    assert element.label == "no"
