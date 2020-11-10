from abc import ABCMeta, abstractmethod
from enum import Enum


class HeuristicInterface(ABCMeta):
    @staticmethod
    @abstractmethod
    def evaluate(state): raise NotImplemented


class NaiveHeuristic(HeuristicInterface):
    @staticmethod
    def evaluate(state):
        height = len(state)
        width = len(state[0])
        return 0 if state[height-1][width-1] == 0 else 1


class Heuristic(Enum):
    naive = 1, NaiveHeuristic.evaluate

    def __init__(self, val, heuristic_function):
        self.val = val
        self.heuristic_function = heuristic_function
