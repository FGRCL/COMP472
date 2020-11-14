from a2 import state_space
from a2.position import Position


def test_successors_4x2_major_corner():
    # given
    current_state = [
        [4, 2, 3, 1],
        [5, 6, 7, 0]
    ]
    current_position = Position(3, 1)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [4, 2, 3, 0],
                [5, 6, 7, 1],
            ],
            Position(3, 0),
            1,
            1
        ),
        (
            [
                [4, 2, 3, 1],
                [5, 6, 0, 7],
            ],
            Position(2, 1),
            1,
            7
        ),
        (
            [
                [4, 2, 3, 1],
                [0, 6, 7, 5],
            ],
            Position(0, 1),
            2,
            5
        ),
        (
            [
                [4, 2, 0, 1],
                [5, 6, 7, 3],
            ],
            Position(2, 0),
            3,
            3
        ),
        (
            [
                [0, 2, 3, 1],
                [5, 6, 7, 4],
            ],
            Position(0, 0),
            3,
            4
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors


def test_successors_4x2_minor_corner():
    # given
    current_state = [
        [1, 2, 3, 4],
        [0, 6, 7, 5]
    ]
    current_position = Position(0, 1)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [0, 2, 3, 4],
                [1, 6, 7, 5]
            ],
            Position(0, 0),
            1,
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [6, 0, 7, 5]
            ],
            Position(1, 1),
            1,
            6
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 0]
            ],
            Position(3, 1),
            2,
            5
        ),
        (
            [
                [1, 0, 3, 4],
                [2, 6, 7, 5]
            ],
            Position(1, 0),
            3,
            2
        ),
        (
            [
                [1, 2, 3, 0],
                [4, 6, 7, 5]
            ],
            Position(3, 0),
            3,
            4
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors


def test_successor_4x2_horizontal_edge_up():
    # given
    current_state = [
        [1, 0, 3, 4],
        [5, 6, 7, 2]
    ]
    current_position = Position(1, 0)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [0, 1, 3, 4],
                [5, 6, 7, 2]
            ],
            Position(0, 0),
            1,
            1
        ),
        (
            [
                [1, 3, 0, 4],
                [5, 6, 7, 2]
            ],
            Position(2, 0),
            1,
            3
        ),
        (
            [
                [1, 6, 3, 4],
                [5, 0, 7, 2]
            ],
            Position(1, 1),
            1,
            6
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors


def test_successor_4x2_horizontal_edge_down():
    # given
    current_state = [
        [1, 2, 3, 4],
        [5, 6, 0, 7]
    ]
    current_position = Position(2, 1)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [1, 2, 0, 4],
                [5, 6, 3, 7]
            ],
            Position(2, 0),
            1,
            3
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 0]
            ],
            Position(3, 1),
            1,
            7
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 0, 6, 7]
            ],
            Position(1, 1),
            1,
            6
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors


def test_successor_4x4_middle():
    # given
    current_state = [
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 7]
    ]
    current_position = Position(2, 1)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [1, 2, 0, 4],
                [5, 6, 3, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 7]
            ],
            Position(2, 0),
            1,
            3
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 11, 8],
                [9, 10, 0, 12],
                [13, 14, 15, 7]
            ],
            Position(2, 2),
            1,
            11
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 0, 6, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 7]
            ],
            Position(1, 1),
            1,
            6
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 8, 0],
                [9, 10, 11, 12],
                [13, 14, 15, 7]
            ],
            Position(3, 1),
            1,
            8
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors


def test_successor_4x4_vertical_edge_left():
    # given
    current_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [0, 10, 11, 12],
        [13, 14, 15, 9]
    ]
    current_position = Position(0, 2)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [1, 2, 3, 4],
                [0, 6, 7, 8],
                [5, 10, 11, 12],
                [13, 14, 15, 9]
            ],
            Position(0, 1),
            1,
            5
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [13, 10, 11, 12],
                [0, 14, 15, 9]
            ],
            Position(0, 3),
            1,
            13
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [10, 0, 11, 12],
                [13, 14, 15, 9]
            ],
            Position(1, 2),
            1,
            10
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors


def test_successor_4x4_vertical_edge_right():
    # given
    current_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 0],
        [9, 10, 11, 12],
        [13, 14, 15, 13]
    ]
    current_position = Position(3, 1)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [1, 2, 3, 4],
                [5, 6, 0, 7],
                [9, 10, 11, 12],
                [13, 14, 15, 13]
            ],
            Position(2, 1),
            1,
            7
        ),
        (
            [
                [1, 2, 3, 0],
                [5, 6, 7, 4],
                [9, 10, 11, 12],
                [13, 14, 15, 13]
            ],
            Position(3, 0),
            1,
            4
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 12],
                [9, 10, 11, 0],
                [13, 14, 15, 13]
            ],
            Position(3, 2),
            1,
            12
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors


def test_successor_4x4_major_corner():
    # given
    current_state = [
        [0, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 1]
    ]
    current_position = Position(0, 0)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [2, 0, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 1]
            ],
            Position(1, 0),
            1,
            2
        ),
        (
            [
                [5, 2, 3, 4],
                [0, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 1]
            ],
            Position(0, 1),
            1,
            5
        ),
        (
            [
                [4, 2, 3, 0],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 1]
            ],
            Position(3, 0),
            2,
            4
        ),
        (
            [
                [13, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [0, 14, 15, 1]
            ],
            Position(0, 3),
            2,
            13
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]
            ],
            Position(3, 3),
            3,
            1
        ),
        (
            [
                [6, 2, 3, 4],
                [5, 0, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 1]
            ],
            Position(1, 1),
            3,
            6
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors


def test_successor_4x4_minor_corner():
    # given
    current_state = [
        [1, 2, 3, 0],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 4]
    ]
    current_position = Position(3, 0)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [1, 2, 0, 3],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 4]
            ],
            Position(2, 0),
            1,
            3
        ),
        (
            [
                [1, 2, 3, 8],
                [5, 6, 7, 0],
                [9, 10, 11, 12],
                [13, 14, 15, 4]
            ],
            Position(3, 1),
            1,
            8
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]
            ],
            Position(3, 3),
            2,
            4
        ),
        (
            [
                [0, 2, 3, 1],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 4]
            ],
            Position(0, 0),
            2,
            1
        ),
        (
            [
                [1, 2, 3, 7],
                [5, 6, 0, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 4]
            ],
            Position(2, 1),
            3,
            7
        ),
        (
            [
                [1, 2, 3, 13],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [0, 14, 15, 4]
            ],
            Position(0, 3),
            3,
            13
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors


def test_successor_4x4_horizontal_edge_up():
    # given
    current_state = [
        [1, 0, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 2]
    ]
    current_position = Position(1, 0)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [0, 1, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 2]
            ],
            Position(0, 0),
            1,
            1
        ),
        (
            [
                [1, 3, 0, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 2]
            ],
            Position(2, 0),
            1,
            3
        ),
        (
            [
                [1, 6, 3, 4],
                [5, 0, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 2]
            ],
            Position(1, 1),
            1,
            6
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors


def test_successor_4x4_horizontal_edge_down():
    # given
    current_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 0, 15]
    ]
    current_position = Position(2, 3)

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]
            ],
            Position(3, 3),
            1,
            15
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 0, 14, 15]
            ],
            Position(1, 3),
            1,
            14
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 0, 12],
                [13, 14, 11, 15]
            ],
            Position(2, 2),
            1,
            11
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors
