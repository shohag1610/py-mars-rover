from dataclasses import dataclass
from enums import CompassDirection


@dataclass
class PlateauSize:
    width: int
    height: int


@dataclass
class RoverPosition:
    x: int
    y: int
    direction: CompassDirection
