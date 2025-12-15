from collections import deque

def main():
    with open("day16/data.txt", "r") as f:
        contents = f.read()

    grid = [[i for i in row] for row in contents.split('\n')]
    starting_position = [(i, row.find('S')) for (i, row) in enumerate(contents.split('\n')) if row.find('S') != -1]
    q = deque()
    q.append(starting_position)

    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    complete_paths = []

    while q:
        print('queue length: ', len(q))
        path = q.popleft()
        (i, j) = path[-1]
        if grid[i][j] == 'E':
            complete_paths.append(path)
            continue
        for dx, dy in dirs:
            if 0 <= i+dx < len(grid) and 0 <= j+dy < len(grid[0]):
                if (i+dx, j+dy) in path:
                    continue
                if grid[i+dx][j+dy] == '.' or grid[i+dx][j+dy] == 'E':
                    q.append(path + [(i+dx, j+dy)])
    
    res = float('inf')
    for path in complete_paths:
        turns = 0
        dir = 'horizontal'
        for i in range(len(path)-1):
            point = path[i]
            next_point = path[i+1]
            if dir == 'horizontal' and point[0] != next_point[0]:
                turns += 1
                dir = 'vertical'
            elif dir == 'vertical' and point[1] != next_point[1]:
                turns += 1
                dir = 'horizontal'
        res = min(res, len(path)-1+turns*1000)

    print(res)


if __name__ == "__main__":
    main()
