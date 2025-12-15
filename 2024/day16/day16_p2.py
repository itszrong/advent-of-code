import heapq
from math import inf

HORIZONTAL = 0
VERTICAL = 1

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def main():
    with open("day16/data.txt", "r") as f:
        contents = f.read().rstrip("\n")

    grid = [list(row) for row in contents.split("\n")]
    R, C = len(grid), len(grid[0])

    start = goal = None
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "S": start = (i, j)
            if grid[i][j] == "E": goal = (i, j)
    if start is None or goal is None:
        raise ValueError("Start or goal not found")

    def passable(i, j):
        return grid[i][j] in (".", "S", "E")

    dirs = [(1,0),(0,1),(-1,0),(0,-1)]

    def h(state):
        i, j, _axis = state
        return manhattan((i, j), goal)

    start_state = (start[0], start[1], HORIZONTAL)
    g = {start_state: 0}
    preds = {start_state: set()}

    open_heap = []
    counter = 0
    heapq.heappush(open_heap, (h(start_state), counter, start_state))

    best_goal_cost = inf
    goal_states = set()

    while open_heap:
        f, _, state = heapq.heappop(open_heap)
        current_g = g.get(state, inf)
        if f != current_g + h(state):
            continue

        if f > best_goal_cost:
            break

        i, j, prev_axis = state
        if (i, j) == goal:
            if current_g < best_goal_cost:
                best_goal_cost = current_g
                goal_states = {state}
            elif current_g == best_goal_cost:
                goal_states.add(state)
            continue

        for dx, dy in dirs:
            ni, nj = i + dx, j + dy
            if not (0 <= ni < R and 0 <= nj < C):
                continue
            if not passable(ni, nj):
                continue

            new_axis = VERTICAL if dx != 0 else HORIZONTAL
            turn_penalty = 1000 if new_axis != prev_axis else 0
            step_cost = 1 + turn_penalty

            nxt = (ni, nj, new_axis)
            ng = current_g + step_cost

            best = g.get(nxt, inf)
            if ng < best:
                g[nxt] = ng
                preds[nxt] = {state}
                counter += 1
                heapq.heappush(open_heap, (ng + h(nxt), counter, nxt))
            elif ng == best:
                preds[nxt].add(state)

    if best_goal_cost == inf:
        print("No path found")
        return

    tiles = set()
    stack = list(goal_states)
    seen_states = set(goal_states)

    while stack:
        s = stack.pop()
        tiles.add((s[0], s[1]))
        for p in preds.get(s, ()):
            if p not in seen_states:
                seen_states.add(p)
                stack.append(p)

    print("Best cost:", best_goal_cost)
    print("Number of tiles in any best path:", len(tiles))

if __name__ == "__main__":
    main()
