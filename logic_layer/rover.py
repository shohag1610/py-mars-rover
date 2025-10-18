from input_layer.models import RoverPosition
from input_layer.enums import CompassDirection, Instruction
from logic_layer.rotation import Rotation
from logic_layer.movement import Movement
from logic_layer.enums import MoveResult



class Rover:
    def __init__(self, x: int, y: int, facing: CompassDirection, plateau=None):
        self.position = RoverPosition(x, y, facing)
        self.plateau = plateau

    @property
    def facing(self) -> CompassDirection:
        return self.position.direction

    @facing.setter
    def facing(self, new_direction: CompassDirection):
        self.position.direction = new_direction

    def turn_left(self):
        self.facing = Rotation.turn_left(self.facing)

    def turn_right(self):
        self.facing = Rotation.turn_right(self.facing)

    def move_forward(self) -> MoveResult:
        new_position = Movement.move_forward(self.position)

        if self.plateau and not self.plateau.is_within_bounds(new_position):
            return MoveResult.OUT_OF_BOUNDS

        self.position = new_position
        return MoveResult.SUCCESS

    def execute_instructions(self, instructions: list[Instruction]):
        for instruction in instructions:
            if instruction == Instruction.LEFT:
                self.turn_left()
            elif instruction == Instruction.RIGHT:
                self.turn_right()
            elif instruction == Instruction.MOVE:
                result = self.move_forward()
                if result == MoveResult.OUT_OF_BOUNDS:
                    return MoveResult.OUT_OF_BOUNDS
