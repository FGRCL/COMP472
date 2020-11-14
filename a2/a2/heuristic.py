from abc import ABCMeta, abstractmethod
import numpy as np

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

class ManhattanHeuristic(HeuristicInterface):
    @staticmethod
    def evaluate(state):
        width = len(state[0])

        goal=[1,3,5,7,2,4,6,0]

        curr_state = [val for state in state for val in state]

        # Standard Score
        standard_score = sum(abs((val-1)%width - i%width) + abs((val-1)//width - i//width)
            for i, val in enumerate(curr_state) if val)

        # Non-standard
        nonstandard_score = sum(abs(b%width - g%width) + abs(b//width - g//width)
            for b, g in ((curr_state.index(i), goal.index(i)) for i in range(1,8)))

        return min(standard_score, nonstandard_score)