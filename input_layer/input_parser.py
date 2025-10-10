from enums import Instruction, CompassDirection
from models import PlateauSize, RoverPosition

class InputParser:

   @staticmethod
   def parse_plateau_size(size_str)-> PlateauSize:
      
      try:
         width, height = map(int, size_str.split())
         return PlateauSize(width, height)
      except ValueError:
         raise ValueError(f"Invalid Plateau size format: {size_str}")

   @staticmethod
   def parse_position(position_str)-> RoverPosition:
      try:
         position_and_direction = position_str.split()
         if len(position_and_direction) != 3:
            raise ValueError
         x, y = int(position_and_direction[0]), int(position_and_direction[1])
         direction = CompassDirection(position_and_direction[2].upper())
         
         return RoverPosition(x, y, direction)
      except (ValueError, KeyError):
         raise ValueError(f"Invalid rover position format: {position_str}")

   @staticmethod
   def parse_instructions(instruction_str):
         instructions = []
         
         for char in instruction_str.upper():
            try:
               instructions.append(Instruction(char))
            except ValueError:
               continue
            
         return instructions
      