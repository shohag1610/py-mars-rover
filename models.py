from dataclasses import dataclass
from enums import CompassDirection


@dataclass
class PlateauSize:
    width: int
    height: int


@dataclass
class Position:
    x: int
    y: int
    direction: CompassDirection

