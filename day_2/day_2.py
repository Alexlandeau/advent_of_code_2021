# -*- coding: utf-8 -*-

# Import necessary modules
from typing import AnyStr, Dict, Tuple

# Read input data
with open("day_2/input.txt", "r") as f:
    instructions = f.read().splitlines()
instructions = [tuple(instruction.split(" ")) for instruction in instructions]
instructions = [(direction, int(value)) for direction, value in instructions]

starting_position = {"depth": 0, "horizontal": 0, "aim": 0}


def read_instruction(position: Dict, instruction: Tuple(AnyStr, int)):
    direction, value = instruction
    if direction == "forward":
        position["horizontal"] += value
    if direction == "down":
        position["depth"] += value
    if direction == "up":
        position["depth"] -= value


position = starting_position.copy()
[read_instruction(position, instruction) for instruction in instructions]
print(
    f"Part 1: final position is horizon: {position.get('horizontal')}, depth: {position.get('depth')}, coordinates product is {position.get('horizontal') * position.get('depth')}"
)


def read_instruction(position: Dict, instruction: Tuple):
    direction, value = instruction
    if direction == "forward":
        position["horizontal"] += value
        position["depth"] += position["aim"] * value
    if direction == "down":
        position["aim"] += value
    if direction == "up":
        position["aim"] -= value


position = starting_position.copy()
[read_instruction(position, instruction) for instruction in instructions]
print(
    f"Part 2: final position is horizon: {position.get('horizontal')}, depth: {position.get('depth')}, coordinates product is {position.get('horizontal') * position.get('depth')}"
)
