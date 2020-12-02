from dataclasses import dataclass
from typing import Iterable


@dataclass
class Datapoint:
    features: Iterable[str]
    label: str
