import heapq
from a2.game_node import Node
from typing import List


class OpenList(object):

    def __init__(self, initial_list: List[Node]):
        self._heap = [(node.sorting_key, key, node) for key, node in enumerate(initial_list)]
        self._hash_map = {}
        for node in initial_list:
            self._hash_map[str(node.state)] = node
        self._key = len(self._heap)
        heapq.heapify(self._heap)

    def push(self, node: Node):
        heapq.heappush(self._heap, (node.sorting_key, self._key, node))
        self._hash_map[str(node.state)] = node
        self._key += 1

    def pop(self):
        node: Node = heapq.heappop(self._heap)[2]
        del self._hash_map[str(node.state)]
        return node

    def replace_if_smaller(self, new_node:Node):
        if str(new_node.state) in self._hash_map:
            node = self._hash_map[str(new_node.state)]
            if node.state == new_node.state and node.sorting_key > new_node.sorting_key:
                node.cost = new_node.cost
                node.heuristic_score = new_node.heuristic_score
                node.total_cost = new_node.total_cost
                node.moved_token = new_node.moved_token
                node.sorting_key = new_node.sorting_key
                node.parent = new_node.parent
            return True
        return False


class ClosedList(object):

    def __init__(self):
        self._data = {}

    def __add__(self, node: Node):
        self._data[str(node.state)] = node
        return self

    def __contains__(self, node: Node):
        return str(node.state) in self._data

    def __iter__(self):
        yield from [self._data[key] for key in self._data]
