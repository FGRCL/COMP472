from a2.heuristic import NaiveHeuristic, ManhattanHeuristic, HammingDistance, SumOfPermutationInversions


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

def test_manhattan_3x3_0():
    #given 
    state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    # when
    result = ManhattanHeuristic.evaluate(state)

    #then 
    assert result == 0

def test_manhattan_3x3_1():
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

def test_hamming_2x4_0():
    #given 
    state = [
        [1,2,3,4],
        [5,6,7,0]
    ]

    # when
    result = HammingDistance.evaluate(state)

    #then 
    assert result == 0

def test_hamming_2x4_1():
    #given 
    state = [
        [7,2,3,1],
        [5,6,4,0]
    ]

    # when
    result = HammingDistance.evaluate(state)

    #then 
    assert result == 3

def test_hamming_3x3_0():
    #given 
    state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    # when
    result = HammingDistance.evaluate(state)

    #then 
    assert result == 0

def test_hamming_3x3_1():
    #given 
    state = [
        [5, 0, 8],
        [4, 2, 1],
        [7, 3, 6]
    ]

    # when
    result = HammingDistance.evaluate(state)

    #then 
    assert result == 6

def test_permutations_2x4():
    #given 
    state = [
        [7,2,3,1],
        [5,6,4,0]
    ]

    # when
    result = SumOfPermutationInversions.evaluate(state)

    #then 
    assert result == 8