from input_layer.input_parser import InputParser

from logic_layer.rover import Rover
from logic_layer.plateau import Plateau
from input_layer.enums import CompassDirection, Instruction
from logic_layer.enums import AddRoverResult, MoveResult

def main():
    plateau_str = "5 5"
    position_str = "1 2 N"
    instruction_str = "LMLLMR"

    # plateau = InputParser.parse_plateau_size(plateau_str)
    # position = InputParser.parse_position(position_str)
    # instructions = InputParser.parse_instructions(instruction_str)

    # print("=== Parsed Data ===")
    # print(f"Plateau: {plateau}")
    # print(f"Initial Rover Position: {position}")
    # print(f"Instructions: {instructions}")
    
    
    plateau = Plateau(5,5)
    rover = Rover(3, 2, CompassDirection.NORTH, plateau)
    result = plateau.add_rover(rover)
    
    if result != AddRoverResult.SUCCESS:
        print(f"Could not add rover: {result}")
        return

    instruction_str = "LMLMLMMM"

    # The input layer converts it into enums
    instructions = InputParser.parse_instructions(instruction_str)

    # The logic layer executes typed data
    result = rover.execute_instructions(instructions)
    
    if result == MoveResult.OUT_OF_BOUNDS:
        print(f"Could not move, out of surface!: {result}")
        return
        

    print("Final rover position:", rover.position)
    

if __name__ == "__main__":
    main()