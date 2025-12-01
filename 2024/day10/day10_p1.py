from tokenize import endpats


input = open("data.txt", "r").read()

data = input.split("\n")
rows, cols = len(data), len(data[0])
new_map = [["." for i in range(cols)] for i in range(rows)]
end_points = set()

def dfs(i: int, j: int):
    global end_points

    if data[i][j] == "9":
        new_map[i][j] = data[i][j]
        end_points.add((i,j))
        return True

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    target = str(int(data[i][j]) + 1)
    new_points = []
    for dx, dy in dirs:
        if 0 <= (i+dx) <= rows-1 and 0 <= (j+dy) <= cols-1:
            if data[i+dx][j+dy] == target:
                new_points.append((i+dx, j+dy))

    if not new_points:
        return False

    for k, l in new_points:
        if dfs(k, l):
            new_map[i][j] = data[i][j]
    
    if new_map[i][j] == data[i][j]:
        return True
    else: return False

zeros = []
for row in range(rows):
    for col in range(cols):
        if data[row][col] == '0':
            zeros.append((row, col))

print(zeros)
scores = []

for i, j in zeros:
    dfs(i, j)
    scores.append(len(end_points))
    end_points = set()

for row in data:
    print(" ".join(row))
print("")
for row in new_map:
    print(" ".join(row))
print("")
print(scores)
print(sum(scores))