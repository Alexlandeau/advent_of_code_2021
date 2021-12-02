# -*- coding: utf-8 -*-

# Import necessary modules
from typing import List

# Read input data
with open("day_1/input.txt", "r") as f:
    depths = f.read().splitlines()
depths = [int(depth) for depth in depths]


def window_sum(data: List, window_size):
    data_windows = [sum(data[i-window_size+1:i+1]) for i in range(window_size-1, len(data))]
    return data_windows

depths_window_1 = window_sum(depths, 1)
depth_increases = sum([(depths_window_1[i] < depths_window_1[i+1]) for i in range(len(depths_window_1)-1)])
print(f"Part 1: total number of increases is {depth_increases}")

depths_window_3 = window_sum(depths, 3)
depth_increases = sum([(depths_window_3[i] < depths_window_3[i+1]) for i in range(len(depths_window_3)-1)])
print(f"Part 2: total number of increases is {depth_increases}")
