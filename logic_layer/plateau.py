from input_layer.models import PlateauSize, RoverPosition
from logic_layer.rover import Rover
from logic_layer.enums import AddRoverResult

class Plateau:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.rovers = [] 
    
    def is_within_bounds(self, position: RoverPosition) -> bool:
        return 0 <= position.x <= self.width and 0 <= position.y <= self.height
    
    def is_position_free(self, position: RoverPosition) -> bool:
        for rover in self.rovers:
            if rover.position.x == position.x and rover.position.y == position.y:
                return False
        return True

    def add_rover(self, rover: Rover) -> AddRoverResult:
        
        if not self.is_within_bounds(rover.position):
            return AddRoverResult.OUT_OF_BOUNDS

        if not self.is_position_free(rover.position):
            return AddRoverResult.CRASH_INTO_ROVER

        self.rovers.append(rover)
        return AddRoverResult.SUCCESS

