import pandas as pd
input_df = pd.DataFrame([list(line) for line in input_str.split('\n')])
directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
directions_keys = []
for key in directions.keys():
    directions_keys.append(key)

def get_next_element(my_list, input_str):
    current_index = my_list.index(input_str)
    next_index = (current_index + 1) % len(my_list)
    next_element = my_list[next_index]
    return next_element

new_char = get_next_element(directions_keys, '^')
print(new_char)

import copy
copy_df = copy.deepcopy(input_df)
while any(item in directions.keys() for item in input_df.values.flatten()):
    for char in directions.keys():
        if char in input_df.values:
            # display(input_df)
            index = (input_df.stack() == char).idxmax()
            input_df.iloc[index] = "X"
            if (0 <= index[0] + directions[char][0] < input_df.shape[0]) and (0 <= index[1] + directions[char][1] < input_df.shape[1]):
                  if (0 <= index[0] + 2* directions[char][0] < input_df.shape[0]) and (0 <= index[1] + 2* directions[char][1] < input_df.shape[1]):
                      if input_df.iloc[index[0] + 2 * directions[char][0], index[1] + 2 * directions[char][1]] == "#":
                          new_char = get_next_element(directions_keys, char)
                          # print(new_char)
                          input_df.iloc[index[0] + directions[char][0], index[1] + directions[char][1]] = new_char
                      else:
                          input_df.iloc[index[0] + directions[char][0], index[1] + directions[char][1]] = char
                  else:
                      input_df.iloc[index[0] + directions[char][0], index[1] + directions[char][1]] = char
            # Break the inner loop after processing a character
            break
display(input_df)

x_count = (input_df == 'X').sum().sum()
print(f"The number of 'X' characters in the DataFrame is: {x_count}")

dot_indices = [(i, j) for i in range(copy_df.shape[0]) for j in range(copy_df.shape[1]) if copy_df.iloc[i, j] == "."]

# Highly optimized version
import numpy as np
import time

def run_simulation_optimized(input_grid):
    """
    Optimized simulation using numpy arrays
    """
    grid = input_grid.copy()  # Much faster than DataFrame.copy()
    seen_states = set()
    step = 0
    
    while True:
        # Check for loops
        current_state = tuple(grid.flatten())
        if current_state in seen_states:
            return grid, True  # Loop detected
        seen_states.add(current_state)
        
        # Find all arrows at once
        arrows = []
        for char in directions.keys():
            positions = np.where(grid == char)
            for i, j in zip(positions[0], positions[1]):
                arrows.append((i, j, char))
        
        if not arrows:
            break  # No more arrows
            
        # Process all arrows in parallel (or at least find them all)
        for i, j, char in arrows:
            # Mark current position as visited
            grid[i, j] = 'X'
            
            # Calculate next position
            ni, nj = i + directions[char][0], j + directions[char][1]
            
            # Check bounds
            if 0 <= ni < grid.shape[0] and 0 <= nj < grid.shape[1]:
                # Check if there's an obstacle two steps ahead
                ni2, nj2 = ni + directions[char][0], nj + directions[char][1]
                if (0 <= ni2 < grid.shape[0] and 0 <= nj2 < grid.shape[1] and 
                    grid[ni2, nj2] in ['#', 'O']):
                    # Change direction
                    new_char = get_next_element(directions_keys, char)
                    grid[ni, nj] = new_char
                else:
                    grid[ni, nj] = char
        
        step += 1
        
        # Safety check
        if step > 1000:
            return grid, True
    
    return grid, False

# Convert DataFrame to numpy array for much better performance
grid_array = copy_df.values

# Test performance
print("Testing optimized version...")
start_time = time.time()

no_of_obstacles_loops = 0
test_count = 0

# Test first 100 positions to compare speed
for i, dot_index in enumerate(dot_indices[:100]):
    if i % 10 == 0:
        print(f"Progress: {i}/100")
    
    # Create new grid with obstacle
    test_grid = grid_array.copy()
    test_grid[dot_index] = 'O'
    
    result, loop = run_simulation_optimized(test_grid)
    
    if loop:
        no_of_obstacles_loops += 1
        print(f"  Loop found at position {dot_index}")
    
    # Count X's
    # x_count = np.sum(result == 'X')
    # if x_count != 5242:
    #     print(f"  Different X count at {dot_index}: {x_count}")

end_time = time.time()
print(f"\nOptimized version took {end_time - start_time:.2f} seconds")
print(f"Loops found: {no_of_obstacles_loops}")

# Now run the full test
print("\nRunning full test...")
start_time = time.time()

no_of_obstacles_loops = 0
for i, dot_index in enumerate(dot_indices):
    if i % 1000 == 0:
        print(f"Progress: {i}/{len(dot_indices)}")
    
    test_grid = grid_array.copy()
    test_grid[dot_index] = 'O'
    
    result, loop = run_simulation_optimized(test_grid)
    
    if loop:
        no_of_obstacles_loops += 1
    
    # x_count = np.sum(result == 'X')
    # if x_count != 5242:
    #     print(f"Different X count at {dot_index}: {x_count}")

end_time = time.time()
print(f"\nFull test took {end_time - start_time:.2f} seconds")
print(f"Total loops found: {no_of_obstacles_loops}")

# Highly optimized version
import numpy as np
import time

def run_simulation_fixed(input_grid):
    grid = input_grid.copy()
    seen_states = set()
    step = 0

    while True:
        # Check for loop
        current_state = tuple(grid.flatten())
        if current_state in seen_states:
            return grid, True  # Loop detected
        seen_states.add(current_state)

        # Find the first arrow in direction order
        found_arrow = False
        for char in directions.keys():
            positions = np.where(grid == char)
            if positions[0].size > 0:
                i, j = positions[0][0], positions[1][0]
                grid[i, j] = 'X'
                ni, nj = i + directions[char][0], j + directions[char][1]
                if 0 <= ni < grid.shape[0] and 0 <= nj < grid.shape[1]:
                    ni2, nj2 = ni + directions[char][0], nj + directions[char][1]
                    if (0 <= ni2 < grid.shape[0] and 0 <= ni2 < grid.shape[1] and
                        grid[ni2, nj2] in ['#', 'O']):
                        new_char = get_next_element(directions_keys, char)
                        grid[ni, nj] = new_char
                    else:
                        grid[ni, nj] = char
                found_arrow = True
                break  # Only process one arrow per step

        if not found_arrow:
            break  # No more arrows

        step += 1
        if step > 10000:  # Safety check for infinite loops
            return grid, True

    return grid, False

# Convert DataFrame to numpy array for much better performance
grid_array = copy_df.values

# Test performance
print("Testing optimized version...")
start_time = time.time()

no_of_obstacles_loops = 0

# Test first 100 positions to compare speed
for i, dot_index in enumerate(dot_indices[:100]):
    if i % 10 == 0:
        print(f"Progress: {i}/100")
    
    # Create new grid with obstacle
    test_grid = grid_array.copy()
    test_grid[dot_index] = 'O'
    
    result, loop = run_simulation_fixed(test_grid)
    
    if loop:
        no_of_obstacles_loops += 1
        print(f"  Loop found at position {dot_index}")
    
    # Count X's
    # x_count = np.sum(result == 'X')
    # if x_count != 41:
    #     print(f"  Different X count at {dot_index}: {x_count}")

end_time = time.time()
print(f"\nOptimized version took {end_time - start_time:.2f} seconds")
print(f"Loops found: {no_of_obstacles_loops}")

# Now run the full test
print("\nRunning full test...")
start_time = time.time()

no_of_obstacles_loops = 0
for i, dot_index in enumerate(dot_indices):
    if i % 1000 == 0:
        print(f"Progress: {i}/{len(dot_indices)}")
    
    test_grid = grid_array.copy()
    test_grid[dot_index] = 'O'
    
    result, loop = run_simulation_fixed(test_grid)
    
    if loop:
        no_of_obstacles_loops += 1
    
    # x_count = np.sum(result == 'X')
    # if x_count != 41:
    #     print(f"Different X count at {dot_index}: {x_count}")

end_time = time.time()
print(f"\nFull test took {end_time - start_time:.2f} seconds")
print(f"Total loops found: {no_of_obstacles_loops}")

# Simple optimized version without multiprocessing
import numpy as np
import time

def run_simulation_fixed(input_grid):
    grid = input_grid.copy()
    seen_states = set()
    step = 0

    while True:
        current_state = tuple(grid.flatten())
        if current_state in seen_states:
            return grid, True
        seen_states.add(current_state)

        found_arrow = False
        for char in directions.keys():
            positions = np.where(grid == char)
            if positions[0].size > 0:
                i, j = positions[0][0], positions[1][0]
                grid[i, j] = 'X'
                ni, nj = i + directions[char][0], j + directions[char][1]
                if 0 <= ni < grid.shape[0] and 0 <= nj < grid.shape[1]:
                    ni2, nj2 = ni + directions[char][0], nj + directions[char][1]
                    if (0 <= ni2 < grid.shape[0] and 0 <= ni2 < grid.shape[1] and
                        grid[ni2, nj2] in ['#', 'O']):
                        new_char = get_next_element(directions_keys, char)
                        grid[ni, nj] = new_char
                    else:
                        grid[ni, nj] = char
                found_arrow = True
                break

        if not found_arrow:
            break

        step += 1
        if step > 100:
            return grid, True

    return grid, False

# Convert DataFrame to numpy array
grid_array = copy_df.values

print("Starting optimized test...")
start_time = time.time()

no_of_obstacles_loops = 0
for i, dot_index in enumerate(dot_indices):
    if i % 1000 == 0:
        print(f"Progress: {i}/{len(dot_indices)}")
    
    test_grid = grid_array.copy()
    test_grid[dot_index] = 'O'
    
    result, loop = run_simulation_fixed(test_grid)
    
    if loop:
        no_of_obstacles_loops += 1

end_time = time.time()

print(f"Total loops found: {no_of_obstacles_loops}")
print(f"Time taken: {end_time - start_time:.2f} seconds")

import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else '6.in'
p1 = 0
p2 = 0
D = input_str

G = D.split('\n')
R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == '^':
            sr,sc = r,c

for o_r in range(R):
    for o_c in range(C):
        r,c = sr,sc
        d = 0 # 0=up, 1=right, 2=down, 3=left
        SEEN = set()
        SEEN_RC = set()
        while True:
            if (r,c,d) in SEEN:
                p2 += 1
                break
            SEEN.add((r,c,d))
            SEEN_RC.add((r,c))
            dr,dc = [(-1,0),(0,1),(1,0),(0,-1)][d]
            rr = r+dr
            cc = c+dc
            if not (0<=rr<R and 0<=cc<C):
                if G[o_r][o_c]=='#':
                    p1 = len(SEEN_RC)
                break
            if G[rr][cc]=='#' or rr==o_r and cc==o_c:
                d = (d+1)%4
            else:
                r = rr
                c = cc
pr(p1)
pr(p2)