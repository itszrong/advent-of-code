import re
import numpy as np
from collections import deque, defaultdict

input = open("data.txt", "r").read()

def region(input):

    data = input.split("\n")
    rows, cols = len(data), len(data[0])
    seen = set()

    def dfs(i, j):
        target = data[i][j]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        points = []
        for dx, dy in dirs:
            new_i, new_j = i+dx, j+dy
            if (new_i, new_j) not in seen:
                if 0 <= new_i < rows and 0 <= new_j < cols:
                    if data[new_i][new_j] == target:
                        seen.add((new_i, new_j))
                        points.append((new_i, new_j))

        if points:
            for (k, l) in points:
                new_points = dfs(k, l)
                if new_points:
                    points.extend(new_points)
        return points

    def calcPerimeter(points):

        perimeter = 0

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for i, j in points:
            for dx, dy in dirs:
                new_i, new_j = i+dx, j+dy
                if -1 <= new_i < rows+1 and -1 <= new_j < cols+1:
                    if (new_i, new_j) not in points:
                        perimeter += 1
        return perimeter

    total = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) in seen:
                continue
            seen.add((i,j))
            points = dfs(i, j)
            points.append((i,j))
            area = len(points)
            perimeter = calcPerimeter(points)
            # print(data[i][j], area, perimeter, "coord:", (i, j), "price", area*perimeter)
            total += area*perimeter

    return total

print(region(input))


