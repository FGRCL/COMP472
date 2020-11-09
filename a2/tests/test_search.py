from a2.search import UniformCostSearch, is_goal
from a2.state_space import successors
from a2.position import Position
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


def test_generate_start_state():
    state = (
        [
            [1, 2, 3, 4],
            [5, 6, 7, 0]
        ],
        Position(3, 1)
    )

    for i in range(100):
        choice = random.choice(list(successors(state[0], state[1])))
        state = (choice[0], choice[1])

    print(state)
    assert False

def test_ucs():
    # given
    state = [
        [4, 5, 1, 2],
        [0, 6, 3, 7]
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
    result = UniformCostSearch.find(state, goals)

    # then
    assert result.state in goals
    print(result)
