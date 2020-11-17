import time
from a2.game_node import Node
from a2.data_structure import OpenList, ClosedList
from a2.state_space import successors
from a2.position import Position
from a2.decorator.timed import timedfunction
from abc import ABCMeta, abstractmethod


class SearchAlgorithmInterface(ABCMeta):
    @staticmethod
    @abstractmethod

    def find(state, goals, heuristic): raise NotImplemented


class UniformCostSearch(SearchAlgorithmInterface):
    @staticmethod
    @timedfunction
    def find(state, goals, heuristic):
        start_node = Node(state, find_element(state, 0), 0, 0, 0, 0, 0, 0, None)
        open = OpenList([start_node])
        closed = ClosedList()

        current_node = open.pop()
        while not is_goal(current_node.state, goals):  # TODO do we need to check if the open list is empty?
            for successor in successors(current_node.state, current_node.position):
                new_node = Node(successor[0], successor[1], 0, successor[2], current_node.total_cost + successor[2], 0, successor[3], current_node.sorting_key + successor[2], current_node)
                if (new_node not in closed and not open.replace_if_smaller(new_node)):
                    open.push(new_node)
            closed += current_node
            current_node = open.pop()

        return current_node, closed


class GreedyBestFirstSearch(SearchAlgorithmInterface):
    @staticmethod
    @timedfunction
    def find(state, goals, heuristic):
        start_node = Node(state, find_element(state, 0), 0, 0, 0, 0, 0, 0, None)
        open = OpenList([start_node])
        closed = ClosedList()

        current_node = open.pop()
        while not is_goal(current_node.state, goals):
            for successor in successors(current_node.state, current_node.position):
                heuristic_score = heuristic.evaluate(successor[0], goals)
                new_node = Node(successor[0], successor[1], heuristic_score, successor[2], current_node.total_cost + successor[2], 0, successor[3], heuristic_score, current_node)
                if new_node not in closed and not open.replace_if_smaller(new_node):
                    open.push(new_node)
            closed += current_node
            current_node = open.pop()

        return current_node, closed


class A_Star(SearchAlgorithmInterface):
    @staticmethod
    @timedfunction
    def find(state, goals, heuristic):
        start_node = Node(state, find_element(state, 0), 0, 0, 0, 0, 0, 0, None)
        open = OpenList([start_node])
        closed = ClosedList()

        current_node = open.pop()
        while not is_goal(current_node.state, goals):
            for successor in successors(current_node.state, current_node.position):
                heuristic_score = heuristic.evaluate(successor[0], goals)
                sorting_key = current_node.total_cost + successor[2] + heuristic_score
                new_node = Node(successor[0], successor[1], heuristic_score, successor[2], current_node.total_cost + successor[2], sorting_key, successor[3], sorting_key, current_node)

                if (new_node not in closed and not open.replace_if_smaller(new_node)):
                    open.push(new_node)
            closed += current_node
            current_node = open.pop()

        return current_node, closed


def is_goal(state, goals):
    return any([state == goal for goal in goals])


def find_element(state, element):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == element:
                return Position(j, i)
