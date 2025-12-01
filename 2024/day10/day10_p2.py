from tokenize import endpats


input = open("data.txt", "r").read()

data = input.split("\n")
rows, cols = len(data), len(data[0])
new_map = [["." for i in range(cols)] for i in range(rows)]
paths = set()

def dfs(i: int, j: int):

    if data[i][j] == "9":
        paths = []
        new_map[i][j] = data[i][j]
        paths.append([(i,j)])
        return paths

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    target = str(int(data[i][j]) + 1)
    new_points = []
    for dx, dy in dirs:
        if 0 <= (i+dx) <= rows-1 and 0 <= (j+dy) <= cols-1:
            if data[i+dx][j+dy] == target:
                new_points.append((i+dx, j+dy))

    if not new_points:
        return []

    paths = []
    for k, l in new_points:
        new_paths = dfs(k, l)
        if new_paths:
            new_map[i][j] = data[i][j]
            for path in new_paths:
                path.append((i,j))
        paths.extend(new_paths)
    
    if new_map[i][j] == data[i][j]:
        return paths
    else: return []

zeros = []
for row in range(rows):
    for col in range(cols):
        if data[row][col] == '0':
            zeros.append((row, col))

ratings = []

for i, j in zeros:
    paths = dfs(i, j)
    if paths:
        ratings.append(len(paths))
    paths = []

for row in data:
    print(" ".join(row))
print("")
for row in new_map:
    print(" ".join(row))
print("")
print(ratings)
print(sum(ratings))