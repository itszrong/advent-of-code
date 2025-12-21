from collections import deque, defaultdict

def main():
    with open("day23/data_ex.txt", "r") as f:
        contents = f.read()

    graph = defaultdict(list)
    t_starts = []
    for line in contents.split('\n'):
        s1, s2 = line.split('-')
        graph[s1].append(s2)
        graph[s2].append(s1)
        if s1.startswith('t'):
            if s1 not in t_starts:
                t_starts.append(s1)
        if s2.startswith('t'):
            if s2 not in t_starts:
                t_starts.append(s2)

    seen_lists = []
    final_sets = []
    q = deque()
    for start in t_starts:
        new_list = []
        new_list.append(start)
        q.append((start, new_list))
        while q:
            (curr, curr_list) = q.popleft()
            if len(curr_list) > 3:
                continue
            for i in graph[curr]:
                next_list = curr_list.copy()
                if i in curr_list[0] and len(curr_list) == 3:
                    next_list.sort()
                    if next_list not in final_sets:
                        final_sets.append(next_list)
                    continue
                next_list.append(i)
                if next_list not in seen_lists:
                    seen_lists.append(next_list)
                    q.append((i, next_list))

    print(len(final_sets))
    f = open('day23/save_ex.txt','w')
    for line in final_sets:
        f.write(f"{line}\n")
    f.close()

if __name__ == "__main__":
    main()
