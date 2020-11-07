from dataclasses import dataclass
from typing import Type
import array

@dataclass
class Node:
    state: array
    position: array
    cost: int
    parent: Type['Node']
