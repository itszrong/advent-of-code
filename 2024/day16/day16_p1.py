import heapq
from math import inf

def main():

    HORIZONTAL = 0
    VERTICAL = 1

    def manhattan(a, b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])

    with open("day16/data.txt", "r") as f:
        contents = f.read()

    grid = [list(row) for row in contents.split('\n')]
    rows, cols = len(grid), len(grid[0])
    start, goal = None, None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                goal = (i, j)

    if start is None or goal is None:
        raise ValueError("Start or goal not found")
    

    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    def passable(i, j):
        return grid[i][j] == '.' or grid[i][j] == 'E' or grid[i][j] == 'S'

    start_state = (start[0], start[1], HORIZONTAL)

    g_score = {start_state: 0}
    open_heap = []
    counter = 0

    def heuristic(state):
        i, j, _axis = state
        return manhattan((i, j), goal)

    heapq.heappush(open_heap, (heuristic(start_state), counter, start_state))

    while open_heap:
        f, _tiebreak, state = heapq.heappop(open_heap)
        i, j, prev_axis = state
        current_g = g_score.get(state, inf)

        if f != current_g + heuristic(state):
            continue

        if (i, j) == goal:
            print(current_g)
            return 

        for dx, dy in dirs:
            ni, nj = i + dx, j + dy
            if not (0 <= ni < rows and 0 <= nj < cols):
                continue
            if not passable(ni, nj):
                continue

            new_axis = VERTICAL if dx != 0 else HORIZONTAL
            turn_penalty = 1000 if new_axis != prev_axis else 0
            step_cost = 1 + turn_penalty

            nxt = (ni, nj, new_axis)
            new_g = current_g + step_cost
            if new_g < g_score.get(nxt, inf):
                g_score[nxt] = new_g
                counter += 1
                f = new_g + heuristic(nxt)
                heapq.heappush(open_heap, (f, counter, nxt))

    print("No path found")


if __name__ == "__main__":
    main()
