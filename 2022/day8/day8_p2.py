import numpy as np

def main():
    with open("day8/data.txt", "r") as f:
        contents = f.read()

    
    grid = [[int(x) for x in line] for line in contents.splitlines()]
    mask = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

    def look_h(y, p1_start, p2_start, increment):
        result = 1
        p1, p2 = p1_start, p2_start
        if p2 < 0 or p2 > len(grid[0])-1:
            return 0
        if increment > 0:
            while p2 <= len(grid[0])-2:
                if grid[y][p1] > grid[y][p2]:
                    result += 1
                    p2 += increment
                else:
                    break
        else:
            while p2 >= 1:
                if grid[y][p1] > grid[y][p2]:
                    result += 1
                    p2 += increment
                else:
                    break

        return result

    def look_v(x, p1_start, p2_start, increment):
        result = 1
        p1, p2 = p1_start, p2_start
        if p2 < 0 or p2 > len(grid)-1:
            return 0
        if increment > 0:
            while p2 <= len(grid[0])-2:
                if grid[p1][x] > grid[p2][x]:
                    result += 1
                    p2 += increment
                else:
                    break
        else:
            while p2 >= 1:
                if grid[p1][x] > grid[p2][x]:
                    result += 1
                    p2 += increment
                else:
                    break
        
        return result

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            x, y = i, j
            p1_start, p2_start, increment = x, x+1, 1
            right = look_h(y, p1_start, p2_start, increment)
            p1_start, p2_start, increment = x, x-1, -1
            left = look_h(y, p1_start, p2_start, increment)

            p1_start, p2_start, increment = y, y+1, 1
            down = look_v(x, p1_start, p2_start, increment)
            p1_start, p2_start, increment = y, y-1, -1
            up = look_v(x, p1_start, p2_start, increment)
            result = left * right * up * down
            mask[j][i] = result

    print(np.max(np.array(mask)))

if __name__ == "__main__":
    main()
