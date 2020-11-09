from a2.game_node import Node
from a2.data_structure import OpenList, ClosedList
from a2.state_space import successors
from a2.position import Position
from abc import ABCMeta, abstractmethod


class SearchAlgorithmInterface(ABCMeta):
    @staticmethod
    @abstractmethod
    def find(state, goals): raise NotImplemented


class UniformCostSearch(SearchAlgorithmInterface):
    @staticmethod
    def find(state, goals):
        start_node = Node(state, find_element(state, 0), 0, None)
        open = OpenList([start_node])
        closed = ClosedList()

        current_node = open.pop()
        closed += current_node
        while not is_goal(current_node, goals):
            for successor in successors(current_node.state, current_node.position):
                new_node = Node(successor[0], successor[1], current_node.cost+successor[2], current_node)
                if new_node not in closed:  # TODO str(list) might result in collisions, not sure
                    open.push(new_node)
            closed += current_node
            current_node = open.pop()
        return current_node


def is_goal(state, goals):
    return any([state == goal for goal in goals])


def find_element(state, element):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == element:
                return Position(j, i)
