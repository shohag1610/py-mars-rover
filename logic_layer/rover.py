from input_layer.models import RoverPosition
from input_layer.enums import CompassDirection, Instruction

class Rover:
    def __init__(self, x:int, y:int, facing: CompassDirection, plateau = None):
        self.position = RoverPosition(x, y, facing)
        self.plateau = plateau
        
    @property
    def facing(self) -> CompassDirection:
        return self.position.direction

    @facing.setter
    def facing(self, new_direction: CompassDirection):
        self.position.direction = new_direction
        
    def turn_left(self):
        directions = [
            CompassDirection.NORTH,
            CompassDirection.WEST,
            CompassDirection.SOUTH,
            CompassDirection.EAST,
        ]
        index = directions.index(self.facing)
        self.facing = directions[(index + 1) % len(directions)]

    def turn_right(self):
        directions = [
            CompassDirection.NORTH,
            CompassDirection.EAST,
            CompassDirection.SOUTH,
            CompassDirection.WEST,
        ]
        index = directions.index(self.facing)
        self.facing = directions[(index + 1) % len(directions)]

    # --------------------
    # Movement Logic
    # --------------------
    def move_forward(self):
        dx, dy = 0, 0
        if self.facing == CompassDirection.NORTH:
            dy = 1
        elif self.facing == CompassDirection.SOUTH:
            dy = -1
        elif self.facing == CompassDirection.EAST:
            dx = 1
        elif self.facing == CompassDirection.WEST:
            dx = -1

        new_position = RoverPosition(
            self.position.x + dx, self.position.y + dy, self.facing
        )

        # Move successful
        self.position = new_position

    def execute_instructions(self, instructions: list[Instruction]):
        """Iterate through instructions and execute them in order."""
        for instruction in instructions:
            if instruction == Instruction.LEFT:
                self.turn_left()
            elif instruction == Instruction.RIGHT:
                self.turn_right()
            elif instruction == Instruction.MOVE:
                self.move_forward()