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
        event_counts = {}
        prior_counts = {}
        features = set()
        datapoint_count = 0

        for datapoint in datapoints:
            label = datapoint.label
            datapoint_count += 1
            for feature in datapoint.features:
                features.add(feature)
                initialize_or_increment(prior_counts, label, 1, 1)
                safe_init(event_counts, label, {})
                initialize_or_increment(event_counts[label], feature, 1+delta, 1)

        for label in prior_counts:
            prior_counts[label] += len(features)
            for feature in features:
                safe_init(event_counts[label], feature, delta)

        for label in event_counts:
            for feature in features:
                safe_init(self.conditionals, label, {})

                event = event_counts[label][feature]
                prior = prior_counts[label]
                self.conditionals[label][feature] = event / prior

            self.class_probabilities[label] = prior_counts[label] / datapoint_count

    def predict(self, features: Iterable[str]):
        scores = []
        for label in self.class_probabilities:
            score = self.class_probabilities[label]
            for feature in features:
                score += math.log(self.conditionals[label][feature])
            scores.append((score, label))
        return max(scores)
