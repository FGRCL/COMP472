from a2.game_node import Node
from a2.priority_queue import Heap
from abc import ABCMeta, abstractmethod
import heapq


class SearchAlgorithmInterface(ABCMeta):
    @staticmethod
    @abstractmethod
    def find(state, goal): raise NotImplemented

class UniformCostSearch(SearchAlgorithmInterface):
    @staticmethod
    def find(state, goal):
        startNode = Node(state, find_element(state, 0), 0, None)
        open = Heap(startNode, lambda node: node.cost)
        closed = {}

        current_node = open.pop()
        while not is_goal(current_node, goal):
            for successor in succesors
            pass


def is_goal(state, goal):
    return state == goal


def find_element(state, element):
    for i in len(state):
        for j in len(state[i]):
            if state[i][j] == element:
                return i, j