from dataclasses import dataclass
from typing import Type, List, Tuple
from a2.position import Position

@dataclass
class Node:
    state: List[List[int]]
    position: Position
    cost: int
    total_cost: int
    moved_token: int
    sorting_key: int
    parent: Type["Node"]
