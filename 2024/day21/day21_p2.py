from collections import deque, defaultdict
from functools import lru_cache

NUMPAD = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    ['.','0','A'],
]

DIRPAD = [
    ['.','^','A'],
    ['<','v','>'],
]

DIRS = [(-1,0,'^'), (1,0,'v'), (0,-1,'<'), (0,1,'>')]

def build_mapping(grid):
    mp = {}
    for r,row in enumerate(grid):
        for c,ch in enumerate(row):
            if ch != '.':
                mp[ch] = (r,c)
    return mp

def all_shortest_move_strings(grid, mp, a, b):
    """All shortest move-strings (^v<>) to move pointer from key a -> b on this grid."""
    start = mp[a]
    goal = mp[b]
    if start == goal:
        return [""]

    R, C = len(grid), len(grid[0])

    # BFS distances
    dist = {start: 0}
    q = deque([start])
    while q:
        r,c = q.popleft()
        for dr,dc,ch in DIRS:
            nr,nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '.':
                if (nr,nc) not in dist:
                    dist[(nr,nc)] = dist[(r,c)] + 1
                    q.append((nr,nc))

    dgoal = dist[goal]

    # parents DAG for shortest paths
    parents = defaultdict(list)
    for (r,c), d in dist.items():
        if d == 0:
            continue
        for dr,dc,ch in DIRS:
            pr,pc = r-dr, c-dc
            if (pr,pc) in dist and dist[(pr,pc)] == d-1:
                parents[(r,c)].append(((pr,pc), ch))

    out = []
    def backtrack(node, acc):
        if node == start:
            out.append("".join(reversed(acc)))
            return
        for p, ch in parents[node]:
            backtrack(p, acc + [ch])

    backtrack(goal, [])
    return [s for s in out if len(s) == dgoal]

def solve(contents: str, dir_layers: int) -> int:
    """
    dir_layers=2 for part1, dir_layers=25 for part2.
    """
    num_mp = build_mapping(NUMPAD)
    dir_mp = build_mapping(DIRPAD)

    # Precompute all shortest moves for each pair
    num_paths = {a: {b: all_shortest_move_strings(NUMPAD, num_mp, a, b) for b in num_mp} for a in num_mp}
    dir_paths = {a: {b: all_shortest_move_strings(DIRPAD, dir_mp, a, b) for b in dir_mp} for a in dir_mp}

    @lru_cache(None)
    def cost_type(depth: int, seq: str) -> int:
        """Min cost to make a dirpad type seq, with `depth` more dirpads above it."""
        cur = 'A'
        total = 0
        for ch in seq:
            total += cost_press(depth, cur, ch)
            cur = ch
        return total

    @lru_cache(None)
    def cost_press(depth: int, from_key: str, to_key: str) -> int:
        """Min cost to move from_key -> to_key on a dirpad and press A (select), with recursion depth."""
        best = 10**18
        for moves in dir_paths[from_key][to_key]:
            program = moves + "A"
            if depth == 0:
                best = min(best, len(program))          # human presses directly
            else:
                best = min(best, cost_type(depth-1, program))
        return best

    def code_cost(code: str) -> int:
        depth = dir_layers - 1
        cur = 'A'
        total = 0
        for ch in code:
            best = 10**18
            for moves in num_paths[cur][ch]:
                program = moves + "A"  # what the first dirpad must type
                best = min(best, cost_type(depth, program))
            total += best
            cur = ch
        return total

    ans = 0
    for line in contents.splitlines():
        line = line.strip()
        if not line:
            continue
        ans += code_cost(line) * int(line[:-1])
    return ans

def main():
    with open("day21/data.txt") as f:
        contents = f.read()
    print("part1:", solve(contents, dir_layers=2))
    print("part2:", solve(contents, dir_layers=25))

if __name__ == "__main__":
    main()
