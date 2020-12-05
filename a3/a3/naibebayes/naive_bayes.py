import math
from typing import Iterable
from a3.naibebayes.datapoint import Datapoint
from a3.util.util import initialize_or_increment, safe_init

class NaiveBayes:
    def __init__(self):
        self.conditionals = {}
        self.class_probabilities = {}

    def train(self, datapoints: Iterable[Datapoint]):
        delta = 0.01

        event_counts, prior_counts, features, datapoint_count = self.__get_event_prior_counts(datapoints, delta)
        # self.__smoothing(event_counts, prior_counts, features, delta)
        for label in event_counts:
            for feature in features:
                safe_init(self.conditionals, label, {})
                if feature not in event_counts[label]:
                    event = delta
                else :
                    event = event_counts[label][feature] + delta
                prior = prior_counts[label] + (len(features) * 0.01)
            self.class_probabilities[label] = prior_counts[label] / datapoint_count

    @staticmethod
    def __get_event_prior_counts(datapoints, delta):
        event_counts = {}
        prior_counts = {}
        features = {}
        datapoint_count = 0
        prior_prob = {}; 

        for datapoint in datapoints:
            label = datapoint.label
            datapoint_count += 1
            initialize_or_increment(prior_counts, label, 1, 1)
            for feature in datapoint.features:
                features[feature] = 1
                # features.add(feature)
                # word_count = datapoint.features[feature]
                # initialize_or_increment(prior_counts, label, word_count, word_count)
                safe_init(event_counts, label, {})
                # initialize_or_increment(event_counts[label], feature, word_count, word_count)
                initialize_or_increment(event_counts[label], feature, 1, 1)
        return event_counts, prior_counts, features, datapoint_count

    # @staticmethod
    # def __smoothing(event_counts, prior_counts, features, delta):
    #     for label in prior_counts:
    #         prior_counts[label] += len(features)
    #         for feature in features:
    #             safe_init(event_counts[label], feature, delta)

    def predict(self, features: Iterable[str]):
        scores = []
        for label in self.class_probabilities:
            score = self.class_probabilities[label]
            for feature in features:
                if feature in self.conditionals[label]:
                    score += math.log(self.conditionals[label][feature])
            scores.append((score, label))
        return max(scores)
