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
        height = len(state)

        standard_score = 0
        nonstandard_score = 0

        for i, row in enumerate(state):
            for j, element in enumerate(row):
                x_standard, y_standard = ManhattanHeuristic.get_standard_position(element, width, height)
                standard_score += (abs(x_standard - j)) + (abs(y_standard - i))

                x_nonstandard, y_nonstandard = ManhattanHeuristic.get_nonstandard_position(element, width, height)
                nonstandard_score += (abs(x_nonstandard - j)) + (abs(y_nonstandard - i))

        return min(standard_score, nonstandard_score)

    @staticmethod
    def get_standard_position(element, width, height):
        if element == 0:
            x, y = width - 1, height - 1
        else:
            x = (element - 1) % width
            y = (element - 1) // width
        return x, y

    @staticmethod
    def get_nonstandard_position(element, width, height):
        if element == 0:
            x, y = width - 1, height - 1
        else:
            x = (element - 1) // height
            y = (element - 1) % height
        return x, y

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
