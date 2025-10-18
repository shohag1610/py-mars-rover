from logic_layer.rotation import Rotation
from input_layer.enums import CompassDirection

def test_turn_left():
    assert Rotation.turn_left(CompassDirection.NORTH) == CompassDirection.WEST
    assert Rotation.turn_left(CompassDirection.WEST) == CompassDirection.SOUTH
    assert Rotation.turn_left(CompassDirection.SOUTH) == CompassDirection.EAST
    assert Rotation.turn_left(CompassDirection.EAST) == CompassDirection.NORTH

def test_turn_right():
    assert Rotation.turn_right(CompassDirection.NORTH) == CompassDirection.EAST
    assert Rotation.turn_right(CompassDirection.EAST) == CompassDirection.SOUTH
    assert Rotation.turn_right(CompassDirection.SOUTH) == CompassDirection.WEST
    assert Rotation.turn_right(CompassDirection.WEST) == CompassDirection.NORTH
