# -*- coding: utf-8 -*-

# Import necessary modules
from typing import AnyStr, List, Set

# Read input data
with open("day_4/input.txt", "r") as f:
    bingo = f.read().split("\n\n")
drawn_numbers, grids = (bingo[0], bingo[1:])
drawn_numbers = drawn_numbers.split(",")
grids = [grid.split("\n") for grid in grids]
grids = [[row.split() for row in grid] for grid in grids]


class Grid:
    def __init__(self, grid: List[List[AnyStr]]):
        # Converts a grid to a list of 4 rows and 4 columns
        self.cols = [set(col) for col in zip(*grid)]
        self.rows = [set(row) for row in grid]
        self.grid = self.cols + self.rows


def get_board_score(last_number: AnyStr, remaining_values: Set[AnyStr]):
    return sum([int(value) for value in remaining_values]) * int(last_number)


def get_winners(drawn_numbers: List[AnyStr], grids: List[Grid]):
    victories = []
    for number in drawn_numbers:
        grids_to_remove = []
        for grid in grids:
            for line in grid.grid:
                if number in line:
                    line.remove(number)
            if min([len(line) for line in grid.grid]) == 0:
                grid_remainder = set.union(*grid.grid)
                victories.append((number, grid_remainder))
                grids_to_remove.append(grid)
        [grids.remove(grid) for grid in grids_to_remove]
    return victories


grids = [Grid(grid) for grid in grids]
winners = get_winners(drawn_numbers, grids)

print(f"Part 1: answer is: {get_board_score(*winners[0])}")
print(f"Part 2: answer is: {get_board_score(*winners[-1])}")
