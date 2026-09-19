def main():
    with open("day9/data.txt", "r") as f:
        contents = f.read()

    H = (0, 0)
    T = (0, 0)
    positions = set()
    currs = [(0,0) for i in range(10)]
    moves = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }

    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0

    def vis_pos():
        grid = []
        for j in reversed(range(min_y-1, max_y+3)):
            row = []
            for i in range(min_x-1, max_x+2):
                if (i, j) == (0, 0):
                    row.append('s')
                elif (i, j) in positions:
                    row.append('#')
                else:
                    row.append('.')
            grid.append(row)
        for row in grid:
            print(row)

    def vis_rope():
        grid = []
        print('rope')
        for j in reversed(range(min_y-1, max_y+3)):
            row = []
            for i in range(min_x-1, max_x+2):
                if (i, j) == (0, 0):
                    row.append('s')
                elif (i, j) in currs:
                    index = currs.index((i, j))
                    if index == 0:
                        row.append('H')
                    else:
                        row.append(str(index))
                else:
                    row.append('.')
            grid.append(row)
        for row in grid:
            print(''.join(row))

    def calc_t_pos(H, T):
        dx = H[0]-T[0]
        dy = H[1]-T[1]
        if abs(dx) > 1 or abs(dy) > 1:
            if (dx) == 2 and dy == 1:
                    T = (T[0]+1, T[1]+1) 
            elif (dx) == 2 and dy == -1:
                    T = (T[0]+1, T[1]-1) 
            elif (dx) == 1 and dy == 2:
                    T = (T[0]+1, T[1]+1) 
            elif (dx) == 1 and dy == -2:
                    T = (T[0]+1, T[1]-1) 
            elif (dx) == -2 and dy == 1:
                    T = (T[0]-1, T[1]+1) 
            elif (dx) == -2 and dy == -1:
                    T = (T[0]-1, T[1]-1) 
            elif (dx) == -1 and dy == 2:
                    T = (T[0]-1, T[1]+1) 
            elif (dx) == -1 and dy == -2:
                    T = (T[0]-1, T[1]-1)
            
            # new moves
            elif (dx) == 2 and dy == 2:
                    T = (T[0]+1, T[1]+1)
            elif (dx) == -2 and dy == 2:
                    T = (T[0]-1, T[1]+1)
            elif (dx) == 2 and dy == -2:
                    T = (T[0]+1, T[1]-1)
            elif (dx) == -2 and dy == -2:
                    T = (T[0]-1, T[1]-1)
            
            # one direction
            elif (dx) == 2 and dy == 0:
                    T = (T[0]+1, T[1])
            elif (dx) == 0 and dy == 2:
                    T = (T[0], T[1]+1)
            elif (dx) == -2 and dy == 0:
                    T = (T[0]-1, T[1])
            elif (dx) == 0 and dy == -2:
                    T = (T[0], T[1]-1)
            
            else:
                T = (T[0]+d[0], T[1]+d[1])
        return T

    for line in contents.splitlines():
        dir, n = line.split(' ')
        d = moves[dir]
        for i in range(int(n)):
            H = (H[0]+d[0], H[1]+d[1])
            currs[0] = H
            for i in range(1, len(currs)):
                currs[i] = calc_t_pos(currs[i-1], currs[i])
            positions.add(currs[-1])
            max_x = max(max_x, H[0])
            max_y = max(max_y, H[1])
            min_x = min(min_x, H[0])
            min_y = min(min_y, H[1])

    # vis_pos()
    print(len(positions))


if __name__ == "__main__":
    main()
