from collections import defaultdict, deque
from functools import lru_cache

def main():
    with open("day21/data.txt", "r") as f:
        contents = f.read()

    keypad_grid = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['.', '0', 'A']]
    move_grid = [['.', '^', 'A'], ['<', 'v', '>']]
    dir_grid = [['.', (-1,0), 'A'], [(0, -1), (1,0), (0,1)]]

    def create_graphs(grid):
        graph = defaultdict(list)
        mapping = defaultdict(tuple)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        for (i, row) in enumerate(grid):
            for (j, el) in enumerate(row):
                if el == '.':
                    continue
                mapping[el] = (i, j)
                for (dx, dy) in dirs:
                    if 0 <= i+dx <= rows-1 and 0 <= j+dy <= cols-1:
                        if grid[i+dx][j+dy] == '.':
                            continue
                        graph[el].append(grid[i+dx][j+dy])

        return graph, mapping

    keypad_graph, keypad_mapping = create_graphs(keypad_grid)
    dir_graph, dir_mapping = create_graphs(dir_grid)
    move_graph, move_mapping = create_graphs(move_grid)

    def diff_paths_to_str(diff_paths):
        res = ''
        for dx, dy in diff_paths:
            if dx > 0:
                res += dx*'v'
            elif dx < 0:
                res += abs(dx)*'^'
            if dy > 0:
                res += dy*'>'
            elif dy < 0:
                res += abs(dy)*'<'
        
        return res

    

    @lru_cache(None)
    def get_diff_bfs(target_coord, curr_coord, is_keypad):
        """
        Return ALL shortest paths from curr_coord -> target_coord as lists of (dx,dy) steps.
        is_keypad: True for numeric keypad (forbidden=(3,0), rows=4, cols=3),
                False for dirpad (forbidden=(0,0), rows=2, cols=3).
        """
        if curr_coord == target_coord:
            return ((),)  # tuple-of-paths; each path is tuple-of-steps

        if is_keypad:
            forbidden = (3, 0); rows, cols = 4, 3
        else:
            forbidden = (0, 0); rows, cols = 2, 3

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # 1) BFS distances (no visited-as-bool; we need full dist map)
        dist = {curr_coord: 0}
        q = deque([curr_coord])
        while q:
            i, j = q.popleft()
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if not (0 <= ni < rows and 0 <= nj < cols):
                    continue
                if (ni, nj) == forbidden:
                    continue
                if (ni, nj) not in dist:
                    dist[(ni, nj)] = dist[(i, j)] + 1
                    q.append((ni, nj))

        if target_coord not in dist:
            return tuple()  # unreachable (shouldn't happen)

        # 2) Build parent links along shortest-path edges
        parents = defaultdict(list)  # node -> list of (prev_node, step_taken)
        for (i, j), d in dist.items():
            if d == 0:
                continue
            for dx, dy in dirs:
                pi, pj = i - dx, j - dy
                if (pi, pj) in dist and dist[(pi, pj)] == d - 1:
                    parents[(i, j)].append(((pi, pj), (dx, dy)))

        # 3) Backtrack all shortest paths (tiny grid, so OK)
        out = []
        def backtrack(node, acc_steps):
            if node == curr_coord:
                out.append(tuple(reversed(acc_steps)))
                return
            for prev_node, step in parents[node]:
                backtrack(prev_node, acc_steps + [step])

        backtrack(target_coord, [])
        return tuple(out)


    def get_instructions(s, mapping, is_keypad):
        """
        Return a list of candidate instruction strings to type `s` on this keypad,
        considering all shortest paths per hop.
        """
        curr = 'A'
        candidates = [""]  # start with empty program

        for ch in s:
            target_coord = mapping[ch]
            curr_coord = mapping[curr]

            paths = get_diff_bfs(target_coord, curr_coord, is_keypad)
            # paths is tuple of paths; each path is tuple of (dx,dy)

            # expand candidates by all shortest paths for this character
            new_candidates = []
            for base in candidates:
                for path in paths:
                    new_candidates.append(base + diff_paths_to_str(path) + "A")
            candidates = new_candidates

            curr = ch

        return candidates


    res = 0
    for line in contents.splitlines():
        line = line.strip()
        if not line:
            continue

        instructions_list = get_instructions(line, keypad_mapping, True)

        for _ in range(2):
            new_instructions = set()
            for instruction in instructions_list:
                new_instructions.update(get_instructions(instruction, move_mapping, False))
            instructions_list = list(new_instructions)

        shortest_instruction = min(instructions_list, key=len)
        num = int(line[:-1])
        res += len(shortest_instruction) * num

    print(res)
    
if __name__ == "__main__":
    main()
