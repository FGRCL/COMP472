from a2.heuristic import NaiveHeuristic, ManhattanHeuristic


def test_naive_4x2_0():
    # given
    state = [
        [1, 2, 3, 4],
        [5, 6, 7, 0]
    ]

    # when
    result = NaiveHeuristic.evaluate(state)

    # then
    assert result == 0


def test_naive_4x2_1():
    # given
    state = [
        [1, 2, 0, 4],
        [5, 6, 7, 3]
    ]

    # when
    result = NaiveHeuristic.evaluate(state)

    # then
    assert result == 1


def test_naive_5x5_0():
    # given
    state = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 0]
    ]

    # when
    result = NaiveHeuristic.evaluate(state)

    # then
    assert result == 0


def test_naive_5x5_1():
    # given
    state = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 0, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 13]
    ]

    # when
    result = NaiveHeuristic.evaluate(state)

    # then
    assert result == 1

def test_manhattan_3x3():
    #given 
    state = [
        [7, 2, 4],
        [5, 0, 6],
        [8, 3, 1]
    ]

    # when
    result = ManhattanHeuristic.evaluate(state)

    #then 
    assert result == 14

def test_manhattan_2x4():
    #given 
    state = [
        [1, 2, 7, 4],
        [5, 6, 3, 0]
    ]

    # when
    result = ManhattanHeuristic.evaluate(state)

    #then 
    assert result == 2