from dataclasses import dataclass
from typing import Dict

@dataclass
class Datapoint:
    features: Dict[str, int]
    label: str
