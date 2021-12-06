# -*- coding: utf-8 -*-

# Import necessary modules
from typing import AnyStr, List

# Read input data
with open("day_3/input.txt", "r") as f:
    diag = f.read().splitlines()
diag = [[int(digit) for digit in line] for line in diag]


# Compute ratios
def get_gamma(diag: List[List[AnyStr]]):
    return [int(sum(col)/len(diag) >= 0.5) for col in zip(*diag)]


def get_oxygen_rating(diag: List[List[AnyStr]]):
    filtered_diag = diag
    for i in range(len(diag[0])):
        if len(filtered_diag) > 1:
            gamma = get_gamma(filtered_diag)
            filtered_diag = [line for line in filtered_diag if line[i] == gamma[i]]
    return filtered_diag[0]


def get_co2_rating(diag: List[List[AnyStr]]):
    filtered_diag = diag
    for i in range(len(diag[0])):
        if len(filtered_diag) > 1:
            gamma = get_gamma(filtered_diag)
            epsilon = [1 - term for term in gamma]
            filtered_diag = [line for line in filtered_diag if line[i] == epsilon[i]]
    return filtered_diag[0]


gamma = get_gamma(diag)
epsilon = [1 - term for term in gamma]

# Binary conversion
gamma = int("".join([str(i) for i in gamma]), 2)
epsilon = int("".join([str(i) for i in epsilon]), 2)

print(f"Part 1: power consumption is: {gamma * epsilon}")

# Binary conversion again
oxygen_rating = int("".join([str(i) for i in get_oxygen_rating(diag)]), 2)
co2_rating = int("".join([str(i) for i in get_co2_rating(diag)]), 2)

print(f"Part 2: life support rating is: {oxygen_rating * co2_rating}")
