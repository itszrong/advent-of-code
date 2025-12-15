from collections import deque

def main():
    with open("day15/data.txt", "r") as f:
        contents = f.read()

    parts = contents.split("\n\n")
    grid_temp = parts[0].split('\n')
    replace_dict = {
        'O': ['[', ']'],
        '#': ['#', '#'],
        '.': ['.', '.'],
        '@': ['@', '.']
    }
    grid = [[] for _ in range(len(grid_temp))]
    for (i, row) in enumerate(grid_temp):
        for el in row:
            grid[i].append(replace_dict[el][0])
            grid[i].append(replace_dict[el][1])

    instructions = ''.join(parts[1]).replace('\n', '')

    starting_point = [(i, row.index('@')) for (i, row) in enumerate(grid) if '@' in row]
    dirs_dict = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0),
    }

    def shift_line(grid, i, j, dx, dy, multiple):
        for k in range(multiple, 1, -1):
            grid[i + k*dx][j + k*dy] = grid[i + (k-1)*dx][j + (k-1)*dy]


    def move_horizontal(i, j, dx, dy, grid):
        multiple = 1
        dx2, dy2 = dx, dy
        while grid[i+dx2][j+dy2] == '[' or grid[i+dx2][j+dy2] == ']':
            multiple += 1
            dx2, dy2 = multiple*dx, multiple*dy
        if grid[i+dx2][j+dy2] == '.':
            shift_line(grid, i, j, dx, dy, multiple)
            grid[i][j], grid[i+dx][j+dy] = '.', '@'
            i, j = i+dx, j+dy
        
        return i, j, grid

    def move_vertical(i, j, dx, dy, grid):

        cluster = set()
        q = deque()
        q.append((i+dx,j+dy))

        while q:
            k, l = q.popleft()
            if (k, l, grid[k][l]) not in cluster:
                cluster.add((k, l, grid[k][l]))
                if grid[k][l] == '[':
                    if (k, l+1, grid[k][l+1]) not in cluster:
                        q.append((k, l+1))
                else:
                    if (k, l-1, grid[k][l-1]) not in cluster:
                        q.append((k, l-1))
            if grid[k+dx][l+dy] == '[' or grid[k+dx][l+dy] == ']':
                q.append((k+dx, l+dy))
            elif grid[k+dx][l+dy] == '#':
                return i, j, grid
        
        for (k, l, _) in cluster:
            grid[k][l] = '.'
        for (k, l, el) in cluster:
            grid[k+dx][l+dy] = el
        grid[i][j], grid[i+dx][j+dy] = '.', '@'

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
        elif grid[i+dx][j+dy] == '[' or grid[i+dx][j+dy] == ']':
            if dy != 0:
                i, j, grid = move_horizontal(i, j, dx, dy, grid)
            else:
                i, j, grid = move_vertical(i, j, dx, dy, grid)

    for row in grid:
        print("".join(row))

    res = 0
    for (i, row) in enumerate(grid):
        for (j, el) in enumerate(row):
            if el == '[':
                res += 100*i + j

    print(res)

if __name__ == "__main__":
    main()
