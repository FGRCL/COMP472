from abc import ABCMeta, abstractmethod

class HeuristicInterface(ABCMeta):
    @staticmethod
    @abstractmethod
    def evaluate(state, goals): raise NotImplemented


class NaiveHeuristic(HeuristicInterface):
    @staticmethod
    def evaluate(state, goals):
        height = len(state)
        width = len(state[0])
        return 0 if state[height-1][width-1] == 0 else 1

class ManhattanHeuristic(HeuristicInterface):
    @staticmethod
    def evaluate(state, goals):
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

class HammingDistance(HeuristicInterface):
    @staticmethod
    def evaluate(state, goals):
        distances = [0] * len(goals)

        for d, goal in enumerate(goals):
            for i, row in enumerate(state):
                for j, element in enumerate(row):
                    if goal[i][j] != element:
                        distances[d] += 1

        return min(distances)

class SumOfPermutationInversions(HeuristicInterface):
    @staticmethod
    def evaluate(state, goals):
        curr_state = [val for state in state for val in state]

        # Standard Score
        standard_score = 0
        for i in range(0, len(curr_state)):
            for j in range(i + 1, len(curr_state)):
                if ((curr_state[i] > curr_state[j]) and curr_state[j] != 0):
                    standard_score += 1

        # Non-Standard Score
        nonstandard_score = 0
        for i in range(0, len(curr_state)):
            for j in range(i + 1, len(curr_state)):
                if ((curr_state[i] % 2) != 0): # odd case
                    if ((curr_state[j] % 2) != 0 and (curr_state[i] > curr_state[j])):
                        nonstandard_score += 1
                elif ((curr_state[i] % 2) == 0): # even case
                    if (((curr_state[j] % 2) != 0) or (((curr_state[j] % 2) == 0) and (curr_state[i] > curr_state[j]) and curr_state[j] != 0)):
                        nonstandard_score += 1

        return min(standard_score, nonstandard_score)
