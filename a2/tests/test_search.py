from a2.search import UniformCostSearch, GreedyBestFirstSearch, is_goal
from a2.heuristic import NaiveHeuristic, ManhattanHeuristic, SumOfPermutationInversions
from a2.state_space import successors
from a2.position import Position
import numpy as np
import unittest
import random


def test_is_goal():
    goals = [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 0]
        ],
        [
            [1, 3, 5, 7],
            [2, 4, 6, 0]
        ]
    ]

    states = [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 0]
        ],
        [
            [1, 3, 5, 7],
            [2, 4, 6, 0]
        ]
    ]

    assert is_goal(states[0], goals)
    assert is_goal(states[1], goals)


@unittest.skip
def test_generate_start_state_4x2():
    state = (
        [
            [1, 2, 3, 4],
            [5, 6, 7, 0]
        ],
        Position(3, 1)
    )

    for i in range(10000):
        choice = random.choice(list(successors(state[0], state[1])))
        state = (choice[0], choice[1])

    print(state)
    assert True


@unittest.skip
def test_generate_start_state_10x10():
    state = (
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
            [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
            [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
            [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
            [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
            [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
            [91, 92, 93, 94, 95, 96, 97, 98, 99, 0]  # this is the most unsatisfying thing i've seen all week
        ],
        Position(9, 9)
    )

    for i in range(10000):
        choice = random.choice(list(successors(state[0], state[1])))
        state = (choice[0], choice[1])

    print(state)
    assert True


def test_ucs_4x2():
    # given
    state = [
        [3, 4, 2, 5],
        [7, 0, 1, 6]
    ]

    goals = [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 0]
        ],
        [
            [1, 3, 5, 7],
            [2, 4, 6, 0]
        ]
    ]

    # when
    result = UniformCostSearch.find(state, goals, None)

    # then
    assert result[0].state in goals
    print(result)

# Don't run this, it crashed my computer
@unittest.skip
def test_ucs_10x10():
    # given
    state = [[5, 8, 23, 26, 21, 20, 56, 77, 40, 76],
             [83, 7, 19, 36, 94, 42, 6, 53, 79, 86],
             [65, 69, 78, 61, 45, 3, 68, 89, 30, 29],
             [51, 73, 44, 97, 38, 18, 0, 4, 58, 49],
             [22, 47, 17, 25, 60, 16, 91, 70, 39, 84],
             [85, 13, 71, 14, 82, 10, 80, 74, 64, 43],
             [55, 95, 75, 98, 62, 46, 28, 57, 66, 59],
             [2, 52, 63, 1, 31, 50, 9, 88, 41, 34],
             [33, 35, 12, 11, 37, 92, 72, 32, 96, 48],
             [24, 67, 87, 99, 81, 93, 54, 90, 27, 15]]

    goal = np.arange(1, 101).reshape((10, 10))
    goal[9][9] = 0

    goals = [
        goal.data,
        np.transpose(goal).data
    ]

    # when
    result = UniformCostSearch.find(state, goals, None)

    # then
    assert result.state in goals
    print(result)

def test_gbfs_4x2():
    # given
    state = [
        [2, 5, 7, 1],
        [3, 0, 6, 4]
    ]

    goals = [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 0]
        ],
        [
            [1, 3, 5, 7],
            [2, 4, 6, 0]
        ]
    ]

    # when
    result1 = GreedyBestFirstSearch.find(state, goals, NaiveHeuristic)
    result2 = GreedyBestFirstSearch.find(state, goals, ManhattanHeuristic)
    result3 = GreedyBestFirstSearch.find(state, goals, SumOfPermutationInversions)

    # then
    assert result1[0].state in goals
    assert result2[0].state in goals
    assert result3[0].state in goals

def test_gbfs_3x3():
    # given
    state = [
        [1, 4, 5],
        [2, 3, 7],
        [8, 0, 6]
    ]

    goals = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
    ]

    # when
    result1 = GreedyBestFirstSearch.find(state, goals, NaiveHeuristic) # this takes a loot longer than all the others...
    result2 = GreedyBestFirstSearch.find(state, goals, ManhattanHeuristic)
    result3 = GreedyBestFirstSearch.find(state, goals, SumOfPermutationInversions)

    # then
    assert result1[0].state in goals
    assert result2[0].state in goals
    assert result3[0].state in goals

