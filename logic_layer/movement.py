from input_layer.models import RoverPosition
from input_layer.enums import CompassDirection


class Movement:

    @staticmethod
    def move_forward(position: RoverPosition) -> RoverPosition:
        dx, dy = 0, 0

        if position.direction == CompassDirection.NORTH:
            dy = 1
        elif position.direction == CompassDirection.SOUTH:
            dy = -1
        elif position.direction == CompassDirection.EAST:
            dx = 1
        elif position.direction == CompassDirection.WEST:
            dx = -1

        return RoverPosition(
            x=position.x + dx,
            y=position.y + dy,
            direction=position.direction
        )
