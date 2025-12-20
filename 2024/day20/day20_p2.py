import heapq
from math import inf

def main():
    with open("day20/data.txt", "r") as f:
        contents = f.read()

    grid = [[el for el in row] for row in contents.split('\n')]


    def manhattan(a, b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])

    start, goal = None, None
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                goal = (i, j)

    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    def passable(i, j):
        return grid[i][j] == '.' or grid[i][j] == 'E' or grid[i][j] == 'S'


    def find_path():
        start_state = (start[0], start[1], [(start[0], start[1])])
        g_score = {start_state[:-1]: 0}
        open_heap = []
        counter = 0

        def heuristic(state):
            i, j = state
            return manhattan((i, j), goal)

        heapq.heappush(open_heap, (heuristic(start_state[:-1]), counter, start_state))

        while open_heap:
            f, _tiebreak, state = heapq.heappop(open_heap)
            i, j, points = state
            current_g = g_score.get(state[:-1], inf)

            if f != current_g + heuristic(state[:-1]):
                continue

            if (i, j) == goal:
                return current_g, points

            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if not (0 <= ni < rows and 0 <= nj < cols):
                    continue
                if not passable(ni, nj):
                    continue

                step_cost = 1

                nxt = (ni, nj, points + [(ni, nj)])
                new_g = current_g + step_cost
                if new_g < g_score.get(nxt[:-1], inf):
                    g_score[nxt[:-1]] = new_g
                    counter += 1
                    f = new_g + heuristic(nxt[:-1])
                    heapq.heappush(open_heap, (f, counter, nxt))

        print("No path found")
        return 0

    improvements = set()
    baseline, points = find_path()
    for (i, point) in enumerate(points):
        for (j, point2) in enumerate(points):
            if i <= j:
                continue
            if manhattan(point, point2) <= 20:
                if abs(i-j) - manhattan(point, point2) >= 100:
                    improvements.add((i, j))

    print(baseline)
    print(len(points))
    print(len(improvements))

if __name__ == "__main__":
    main()
