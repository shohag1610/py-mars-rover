import pytest

from input_layer.input_parser import InputParser
from input_layer.enums import Instruction, CompassDirection
from input_layer.models import PlateauSize, RoverPosition

#plateau size
def test_parse_plateau_size_empty():
    with pytest.raises(ValueError):
        result = InputParser.parse_plateau_size("")

def test_parse_plateau_size_valid():
    result = InputParser.parse_plateau_size("5 5")
    assert result == PlateauSize(5, 5)

def test_parse_plateau_size_invalid():
    with pytest.raises(ValueError):
        InputParser.parse_plateau_size("5 five")

#rover position
def test_parse_position_empty():
    with pytest.raises(ValueError):
        InputParser.parse_position("")

def test_parse_position_less_dimension():
    with pytest.raises(ValueError):
        InputParser.parse_position("1 2")

def test_parse_position_extra_dimension():
    with pytest.raises(ValueError):
        InputParser.parse_position("1 2 N 5")

def test_parse_position_valid():
    result = InputParser.parse_position("1 2 N")
    assert result == RoverPosition(1, 2, CompassDirection.NORTH)

def test_parse_position_invalid_direction():
    with pytest.raises(ValueError):
        InputParser.parse_position("1 2 Z") 

def test_parse_position_invalid_format():
    with pytest.raises(ValueError):
        InputParser.parse_position("12N")

#instructions
def test_parse_instructions_empty():
    assert InputParser.parse_instructions("") == []

def test_parse_instructions_valid():
    instructions = InputParser.parse_instructions("LMLMR")
    assert instructions == [
        Instruction.LEFT,
        Instruction.MOVE,
        Instruction.LEFT,
        Instruction.MOVE,
        Instruction.RIGHT
    ]

def test_parse_instructions_with_invalid_chars():
    instructions = InputParser.parse_instructions("LMXMRB")
    assert instructions == [
        Instruction.LEFT,
        Instruction.MOVE,
        Instruction.MOVE,
        Instruction.RIGHT
    ]