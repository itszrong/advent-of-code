import numpy as np

def main():
    with open("day8/data.txt", "r") as f:
        contents = f.read()

    
    grid = [[int(x) for x in line] for line in contents.splitlines()]
    mask = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

    # horizontal looks left
    int_count = 0
    p1_start, p2_start, increment = 0, 1, 1
    for y in range(1, len(grid)):
        p1, p2 = p1_start, p2_start
        while p2 <= len(grid[0])-1:
            if grid[y][p1] < grid[y][p2]:
                mask[y][p2] = 1
                p1 = p2
                p2 += increment
            else:
                p2 += increment

    # horizontal looks right
    p1_start, p2_start, increment = len(grid[0])-1, len(grid[0])-2, -1
    for y in range(1, len(grid)):
        p1, p2 = p1_start, p2_start
        while p2 >= 0:
            if grid[y][p1] < grid[y][p2]:
                mask[y][p2] = 1
                p1 = p2
                p2 += increment
            else:
                p2 += increment

    # vertical looks top to bottom
    p1_start, p2_start, increment = 0, 1, 1
    for x in range(1, len(grid)):
        p1, p2 = p1_start, p2_start
        while p2 <= len(grid[0])-1:
            if grid[p1][x] < grid[p2][x]:
                mask[p2][x] = 1
                p1 = p2
                p2 += increment
            else:
                p2 += increment

    # vertical looks bottom to top
    p1_start, p2_start, increment = len(grid[0])-1, len(grid[0])-2, -1
    for x in range(1, len(grid)):
        p1, p2 = p1_start, p2_start
        while p2 >= 0:
            if grid[p1][x] < grid[p2][x]:
                mask[p2][x] = 1
                p1 = p2
                p2 += increment
            else:
                p2 += increment

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if i == 0 or i == len(grid[0])-1 or j == 0 or j == len(grid)-1:
                mask[i][j] = 1

    # for line in mask:
    #     print(line)
    print(sum(sum(np.asarray(mask))))

if __name__ == "__main__":
    main()
