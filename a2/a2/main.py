import argparse
import numpy as np
from enum import Enum
from a2.heuristic import HeuristicInterface, NaiveHeuristic
from a2.search import SearchAlgorithmInterface, UniformCostSearch


class HeuristicChoice(Enum):
    naive = "naive", NaiveHeuristic

    def __init__(self, val: str, heuristic: HeuristicInterface):
        self.val = val
        self.heuristic = heuristic


class SearchAlgorithmChoice(Enum):
    ucs = "ucs", UniformCostSearch

    def __init__(self, val: str, algorithm: SearchAlgorithmInterface):
        self.val = val
        self.algorithm = algorithm


def main(input_puzzle, solution_file, search_file, search_timeout, algorithm: SearchAlgorithmInterface, heuristic: HeuristicInterface, width: int, height: int):
    goals = get_goals(width, height)

    puzzles = get_puzzles(input_puzzle, width, height)
    for puzzle in puzzles:
        #TODO print the results for now
        print(algorithm.find(puzzle, goals))


def get_puzzles(input_puzzle, width, height):
    puzzles = []
    for line in input_puzzle:
        puzzles.append(np.fromstring(line, dtype=int, sep=' ').reshape((height, width)).tolist())
    return puzzles


def get_goals(width, height):
    range = (width * height) + 1
    goal = np.arange(1, range)
    goal[len(goal)-1] = 0

    goals = [
        goal.reshape((height, width)).tolist(),
        goal.reshape((width, height)).transpose().tolist()
    ]

    return goals


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ᵡ-puzzle solver", description="A program to find the solution of a ᵡ-puzzle using a chosen algorithm")
    parser.add_argument("--inputpuzzle", "-in", metavar="input puzzle", help="the path to the file containing the puzzles to solve", type=open, default="in/puzzle.txt")
    parser.add_argument("--solutionfile", "-out", metavar="solution file", help="the path to the file to output the puzzle solution to", type=open, default="out/solution.txt")
    parser.add_argument("--searchfile", "-sf", metavar="search file", help="the path to the file to output the algorithm's searched states to", type=open)
    parser.add_argument("--searchtimeout", "-t", metavar="timeout", help="the allotted time for a search algorithm to find a solution in seconds", type=int, default=60)
    parser.add_argument("--dimensions", "-d", metavar="dimensions", help="the dimensions of the puzzle in the format: {width}x{height}. ex.: 4x2", type=str, default="4x2")
    parser.add_argument("--algorithm", "-a", metavar="search algorithm", help="the search algorithm to use", choices=SearchAlgorithmChoice, default=SearchAlgorithmChoice.ucs)
    parser.add_argument("--heuristic", "-he", metavar="heuristic", help="the heuristic to use for GBFS and A*", choices=HeuristicChoice, default=HeuristicChoice.naive)

    args = parser.parse_args()
    dimensions = args.dimensions.split("x")
    board_width = int(dimensions[0])
    board_height = int(dimensions[1])
    main(args.inputpuzzle, args.solutionfile, args.searchfile, args.searchtimeout, args.algorithm.algorithm, args.heuristic.heuristic, board_width, board_height)
