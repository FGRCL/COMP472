import heapq
from a2.game_node import Node
from typing import List

# TODO hashing matrices to strings could be problematic for very large matrices
class OpenList(object):

    def __init__(self, initial_list: List[Node]):
        self._heap = [(node.cost, key, node) for key, node in enumerate(initial_list)]
        self._hash_map = {}
        for node in initial_list:
            self._hash_map[str(node.state)] = node
        self._key = len(self._heap)
        heapq.heapify(self._heap)

    def push(self, node: Node):
        heapq.heappush(self._heap, (node.cost, self._key, node))
        self._hash_map[str(node.state)] = node
        self._key += 1

    def pop(self):
        return heapq.heappop(self._heap)[2]

    def replace_if_smaller(self, new_node: Node):
        node = self._hash_map[str(new_node.state)]
        if node.state == new_node.state:
            node.cost = new_node.cost
            node.parent = new_node.parent


class ClosedList(object):

    def __init__(self):
        self._data = {}

    def __add__(self, node: Node):
        self._data[str(node.state)] = True
        return self

    def __contains__(self, node: Node):
        # TODO could maybe optimize
        return str(node.state) in self._data
