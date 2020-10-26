from a2 import state_space

def test_successors_4x2_major_corner():
    # given
    current_state = [
        [4, 2, 3, 1],
        [5, 6, 7, 0]
    ]
    current_position = [3, 1]

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [4, 2, 3, 0],
                [5, 6, 7, 1],
            ],
            1
        ),
        (
            [
                [4, 2, 3, 1],
                [5, 6, 0, 7],
            ],
            1
        ),
        (
            [
                [4, 2, 3, 1],
                [0, 6, 7, 5],
            ],
            2
        ),
        (
            [
                [4, 2, 0, 1],
                [5, 6, 7, 3],
            ],
            3
        ),
        (
            [
                [0, 2, 3, 1],
                [5, 6, 7, 4],
            ],
            3
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
    current_position = [0, 1]

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [0, 2, 3, 4],
                [1, 6, 7, 5]
            ],
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [6, 0, 7, 5]
            ],
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 0]
            ],
            2
        ),
        (
            [
                [1, 0, 3, 4],
                [2, 6, 7, 5]
            ],
            3
        ),
        (
            [
                [1, 2, 3, 0],
                [4, 6, 7, 5]
            ],
            3
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
    current_position = [1, 0]

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [0, 1, 3, 4],
                [5, 6, 7, 2]
            ],
            1
        ),
        (
            [
                [1, 3, 0, 4],
                [5, 6, 7, 2]
            ],
            1
        ),
        (
            [
                [1, 6, 3, 4],
                [5, 0, 7, 2]
            ],
            1
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
    current_position = [2, 1]

    # when
    result = list(state_space.successors(current_state, current_position))

    # then
    expected_successors = [
        (
            [
                [1, 2, 0, 4],
                [5, 6, 3, 7]
            ],
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 0]
            ],
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 0, 6, 7]
            ],
            1
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
    current_position = [2, 1]

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
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 11, 8],
                [9, 10, 0, 12],
                [13, 14, 15, 7]
            ],
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 0, 6, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 7]
            ],
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 8, 0],
                [9, 10, 11, 12],
                [13, 14, 15, 7]
            ],
            1
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
    current_position = [0, 2]

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
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [13, 10, 11, 12],
                [0, 14, 15, 9]
            ],
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [10, 0, 11, 12],
                [13, 14, 15, 9]
            ],
            1
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
    current_position = [3, 1]

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
            1
        ),
        (
            [
                [1, 2, 3, 0],
                [5, 6, 7, 4],
                [9, 10, 11, 12],
                [13, 14, 15, 13]
            ],
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 12],
                [9, 10, 11, 0],
                [13, 14, 15, 13]
            ],
            1
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
    current_position = [0, 0]

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
            1
        ),
        (
            [
                [5, 2, 3, 4],
                [0, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 1]
            ],
            1
        ),
        (
            [
                [4, 2, 3, 0],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 1]
            ],
            2
        ),
        (
            [
                [13, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [0, 14, 15, 1]
            ],
            2
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]
            ],
            3
        ),
        (
            [
                [6, 2, 3, 4],
                [5, 0, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 1]
            ],
            3
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
    current_position = [3, 0]

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
            1
        ),
        (
            [
                [1, 2, 3, 8],
                [5, 6, 7, 0],
                [9, 10, 11, 12],
                [13, 14, 15, 4]
            ],
            1
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]
            ],
            2
        ),
        (
            [
                [0, 2, 3, 1],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 4]
            ],
            2
        ),
        (
            [
                [1, 2, 3, 7],
                [5, 6, 0, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 4]
            ],
            3
        ),
        (
            [
                [1, 2, 3, 13],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [0, 14, 15, 4]
            ],
            3
        )
    ]

    assert len(result) == len(expected_successors)
    for successor in result:
        assert successor in expected_successors