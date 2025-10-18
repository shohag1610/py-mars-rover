from logic_layer.movement import Movement
from input_layer.enums import CompassDirection
from input_layer.models import RoverPosition

def test_move_forward_north():
    pos = RoverPosition(1, 1, CompassDirection.NORTH)
    new_pos = Movement.move_forward(pos)
    assert (new_pos.x, new_pos.y) == (1, 2)

def test_move_forward_west():
    pos = RoverPosition(3, 3, CompassDirection.WEST)
    new_pos = Movement.move_forward(pos)
    assert (new_pos.x, new_pos.y) == (2, 3)
