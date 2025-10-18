from enum import Enum

class AddRoverResult(Enum):
    SUCCESS = "success"
    OUT_OF_BOUNDS = "out_of_bounds"
    CRASH_INTO_ROVER = "crash_into_rover"
    
class MoveResult(Enum):
    SUCCESS = "success"
    OUT_OF_BOUNDS = "out_of_bounds"
