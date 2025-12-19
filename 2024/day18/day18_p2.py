import heapq
from math import inf

def main():
    with open("day18/data.txt", "r") as f:
        contents = f.read()

    rows = cols = 71
    total = len(contents.split('\n'))

    def check(rows, cols, contents, cutoff):
        grid = [['.' for _ in range(cols)] for _ in range(rows)]
        data = contents.split('\n')[:cutoff]
        for line in data:
            nums = line.split(',')
            i = int(nums[1])
            j = int(nums[0])
            grid[i][j] = '#'

        # for row in grid:
        #     print(''.join(row))

        def manhattan(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        start, goal = (0, 0), (rows-1, cols-1)
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def passable(i, j):
            return grid[i][j] == '.'

        start_state = (start[0], start[1])

        g_score = {start_state: 0}
        open_heap = []
        counter = 0

        def heuristic(state):
            i, j = state
            return manhattan((i, j), goal)

        heapq.heappush(open_heap, (heuristic(start_state), counter, start_state))

        while open_heap:
            f, _tiebreak, state = heapq.heappop(open_heap)
            i, j = state
            current_g = g_score.get(state, inf)

            if f != current_g + heuristic(state):
                continue

            if (i, j) == goal:
                return 0

            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if not (0 <= ni < rows and 0 <= nj < cols):
                    continue
                if not passable(ni, nj):
                    continue

                step_cost = 1

                nxt = (ni, nj)
                new_g = current_g + step_cost
                if new_g < g_score.get(nxt, inf):
                    g_score[nxt] = new_g
                    counter += 1
                    f = new_g + heuristic(nxt)
                    heapq.heappush(open_heap, (f, counter, nxt))

        print('Cutoff', cutoff, " - No path found")
        return cutoff

    for i in range(0, total):
        output = check(rows, cols, contents, i)
        if output != 0:
            print(i-1)
            print(contents.split('\n')[i-1])
            break

if __name__ == "__main__":
    main()
