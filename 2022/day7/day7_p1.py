def main():
    with open("day7/data.txt", "r") as f:
        contents = f.read()

    graph = {}

    prev_dirs = []
    cur_dir = ''
    lines = contents.splitlines()
    i = 1
    while i < len(lines):
        line = lines[i]
        if line.startswith('$ cd ..'):
            prev_dirs.pop()
            if not prev_dirs:
                prev_dirs = ['']
                cur_dir = ''
            else:
                cur_dir ='/'.join(prev_dirs)
        elif line.startswith('$ cd '):
            cur_dir = '/'.join(prev_dirs)+'/'+line[len('$ cd '):]
            if cur_dir != '':
                prev_dirs.append(cur_dir.split('/')[-1])           
            if not cur_dir.startswith('/'):
                cur_dir = '/'+cur_dir
        elif line == '$ ls':
            pass
        else:
            if cur_dir not in graph:
                graph[cur_dir] = []
            if line.startswith('dir '):
                new_dir = cur_dir+'/'+line[len('$ cd ')-1:]
                graph[cur_dir].append(new_dir)
            else:
                graph[cur_dir].append(line.split(' ')[0])
        i += 1

    start = ''
    def dfs(graph, pos):
        if not graph[pos]:
            return '0'
        for i in range(len(graph[pos])):
            val = graph[pos][i]
            if not val.isdigit():
                graph[pos][i] = dfs(graph, val)
        res = 0
        for i in graph[pos]:
            res += int(i)
        return str(res)

    
    _ = dfs(graph, start)

    results_array = []
    for i in graph:
        results_array.append(sum([int(x) for x in graph[i]]))
    
    result = 0
    for i in results_array:
        if i <= 100000:
            result += i

    print(result)

if __name__ == "__main__":
    main()
