from input_layer.enums import CompassDirection

class Rotation:

    @staticmethod
    def turn_left(current_direction: CompassDirection) -> CompassDirection:
        order = [
            CompassDirection.NORTH,
            CompassDirection.WEST,
            CompassDirection.SOUTH,
            CompassDirection.EAST,
        ]
        index = order.index(current_direction)
        return order[(index + 1) % len(order)]

    @staticmethod
    def turn_right(current_direction: CompassDirection) -> CompassDirection:
        order = [
            CompassDirection.NORTH,
            CompassDirection.EAST,
            CompassDirection.SOUTH,
            CompassDirection.WEST,
        ]
        index = order.index(current_direction)
        return order[(index + 1) % len(order)]
