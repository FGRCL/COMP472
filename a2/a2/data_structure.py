import heapq
from a2.game_node import Node
from typing import List


class OpenList(object):

    def __init__(self, initial_list: List[Node]):
        self._data = [(node.cost, key, node) for key, node in enumerate(initial_list)]
        self._key = len(self._data)
        heapq.heapify(self._data)

    def push(self, node: Node):
        heapq.heappush(self._data, (node.cost, self._key, node))
        self._key += 1

    def pop(self):
        print(len(self._data))
        return heapq.heappop(self._data)[2]


class ClosedList(object):

    def __init__(self):
        self._data = {}

    def __add__(self, node: Node):
        self._data[str(node.state)] = True
        return self

    def __contains__(self, node: Node):
        return str(node.state) in self._data
