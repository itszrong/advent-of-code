def main():
    with open("day15/data.txt", "r") as f:
        contents = f.read()

    parts = contents.split("\n\n")
    grid_temp = parts[0].split('\n')
    grid = [[i for i in row] for row in grid_temp]

    instructions = ''.join(parts[1]).replace('\n', '')

    starting_point = [(i, row.find('@')) for (i, row) in enumerate(grid_temp) if row.find('@') != -1]
    dirs_dict = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0),
    }

    def move(i, j, dx, dy, grid):
        multiple = 1
        dx2, dy2 = dx, dy
        while grid[i+dx2][j+dy2] == 'O':
            multiple += 1
            dx2, dy2 = multiple*dx, multiple*dy
        if grid[i+dx2][j+dy2] == '.':
            grid[i][j], grid[i+dx][j+dy], grid[i+dx2][j+dy2] = '.', '@', 'O' 
            i, j = i+dx, j+dy
        
        return i, j, grid

    i, j = starting_point[0][0], starting_point[0][1]
    rows, cols = len(grid), len(grid[0])
    for m in instructions:
        (dx, dy) = dirs_dict[m]
        if i + dx < 0 or i + dx > rows-1 or j + dy < 0 or j + dy > cols-1:
            continue
        elif grid[i+dx][j+dy] == '.':
            grid[i][j], grid[i+dx][j+dy] = '.', '@'
            i, j = i+dx, j+dy
            continue
        elif grid[i+dx][j+dy] == 'O':
            i, j, grid = move(i, j, dx, dy, grid)

    for row in grid:
        print("".join(row))

    res = 0
    for (i, row) in enumerate(grid):
        for (j, el) in enumerate(row):
            if el == 'O':
                res += 100*i + j

    print(res)

if __name__ == "__main__":
    main()
