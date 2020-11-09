from a2.data_structure import ClosedList
from a2.game_node import Node, Position


def test_contains():
    inserted_state = [
        [1, 2, 3, 4],
        [3, 4, 5, 6]
    ]

    other_state = [
        [3, 4, 5, 6],
        [1, 2, 3, 4]
    ]

    inserted_node = Node(inserted_state, Position(0, 0), 0, None)
    other_node = Node(other_state, Position(0, 0), 0, None)

    testee = ClosedList()

    testee += inserted_node

    assert inserted_node in testee
    assert other_node not in testee
