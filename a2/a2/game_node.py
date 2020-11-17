from dataclasses import dataclass
from typing import Type, List, Tuple
from a2.position import Position

@dataclass
class Node:
    state: List[List[int]]
    position: Position
    heuristic_score: int
    cost: int
    total_cost: int
    f: int
    moved_token: int
    sorting_key: int
    parent: Type["Node"]
