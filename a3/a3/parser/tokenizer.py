from typing import Generator, Tuple, Iterable, List

from a3.naibebayes.datapoint import Datapoint
from a3.util.util import initialize_or_increment


def parse_file(file_name: str) -> Generator[Tuple[str, List[str], str], None, None]:
    with open(file_name, "r") as file:
        file.readline()  # discard the first line of the document
        for line in file:
            split_line = line.split()
            tweet_id = split_line[0]
            text = lower_case(split_line[1: -7])
            label = split_line[-7]
            yield tweet_id, text, label


def lower_case(strings: Iterable[str]) -> Iterable[str]:
    return [string.lower() for string in strings]


def tweet_to_datapoints(tweets: Generator[Tuple[str, List[str], str], None, None]) -> Generator[Datapoint, None, None]:
    for tweet in tweets:
        features = {}
        for word in tweet[1]:
            initialize_or_increment(features, word, 1, 1)
        yield Datapoint(features, tweet[2])


def filter_vocabulary(datapoints: Generator[Datapoint, None, None], word_count_limit) -> Generator[Datapoint, None, None]:
    vocabulary = {}
    datapoints_list = list(datapoints)
    for datapoint in datapoints_list:
        for word in datapoint.features:
            word_count = datapoint.features[word]
            initialize_or_increment(vocabulary, word, word_count, word_count)

    for datapoint in datapoints_list:
        new_words = {}
        for word in datapoint.features:
            if vocabulary[word] >= word_count_limit:
                new_words[word] = datapoint.features[word]
        yield Datapoint(new_words, datapoint.label)
