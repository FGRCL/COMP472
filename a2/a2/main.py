import argparse
import numpy as np
from enum import Enum
from a2.heuristic import HeuristicInterface, NaiveHeuristic, ManhattanHeuristic, HammingDistance, SumOfPermutationInversions
from a2.search import SearchAlgorithmInterface, UniformCostSearch, GreedyBestFirstSearch, A_Star
from a2.output_files import write_solution_file, write_search_file, write_no_solution
from func_timeout import func_timeout, FunctionTimedOut
class HeuristicChoice(Enum):
    naive = NaiveHeuristic
    manhattan = ManhattanHeuristic
    hamming = HammingDistance
    permutations = SumOfPermutationInversions

    def __init__(self, heuristic: HeuristicInterface):
        self.heuristic = heuristic

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(name):
        return HeuristicChoice[name]


class SearchAlgorithmChoice(Enum):
    ucs = UniformCostSearch
    gbfs = GreedyBestFirstSearch
    astar = A_Star

    def __init__(self, algorithm: SearchAlgorithmInterface):
        self.algorithm = algorithm

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(name):
        return SearchAlgorithmChoice[name]


def main(input_puzzle, solution_directory, search_directory, search_timeout, algorithm: SearchAlgorithmChoice, heuristic: HeuristicChoice, width: int, height: int):
    goals = get_goals(width, height)

    # TODO we might be able to solve different puzzles in parallel
    puzzles = get_puzzles(input_puzzle, width, height)
    for i, puzzle in enumerate(puzzles):
        solution_file_path = '{}{}_{}-{}_solution.txt'.format(solution_directory, i, algorithm.name, heuristic.name)
        search_file_path = '{}{}_{}_{}_search.txt'.format(search_directory, i, algorithm.name, heuristic.name)
        puzzle_solver_worker(puzzle, goals, algorithm.algorithm, heuristic.heuristic, solution_file_path, search_file_path, search_timeout)


def puzzle_solver_worker(puzzle, goals, search_algorithm, heuristic, solution_file_path, search_file_path, search_timeout):
    with open(solution_file_path, 'w+') as solution_file, open(search_file_path, 'w+') as search_file:
        try:
            final_node, closed_list, exec_time = func_timeout(search_timeout, search_algorithm.find, args=(puzzle, goals, heuristic))
            write_solution_file(final_node, solution_file, exec_time)
            write_search_file(closed_list, search_file)
        except FunctionTimedOut:
            write_no_solution(solution_file)


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
    parser.add_argument("--solutiondirectory", "-out", metavar="solution directory", help="the path to the directory to output the puzzle solutions to", type=str, default="out/solution/")
    parser.add_argument("--searchfile", "-sf", metavar="search file", help="the path to the file to output the algorithm's searched states to", type=str, default="out/search/")
    parser.add_argument("--searchtimeout", "-t", metavar="timeout", help="the allotted time for a search algorithm to find a solution in seconds", type=int, default=60)
    parser.add_argument("--dimensions", "-d", metavar="dimensions", help="the dimensions of the puzzle in the format: {width}x{height}. ex.: 4x2", type=str, default="4x2")
    parser.add_argument("--algorithm", "-a", help="the search algorithm to use", choices=SearchAlgorithmChoice, type=SearchAlgorithmChoice.from_string, default=SearchAlgorithmChoice.ucs)
    parser.add_argument("--heuristic", "-he", help="the heuristic to use for GBFS and A*", choices=HeuristicChoice, type=HeuristicChoice.from_string, default=HeuristicChoice.naive)

    args = parser.parse_args()
    dimensions = args.dimensions.split("x")
    board_width = int(dimensions[0])
    board_height = int(dimensions[1])
    main(args.inputpuzzle, args.solutiondirectory, args.searchfile, args.searchtimeout, args.algorithm, args.heuristic, board_width, board_height)
