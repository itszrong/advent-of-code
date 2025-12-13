input = open("day12/data.txt", "r").read()

def region(input):

    data = input.split("\n")
    rows, cols = len(data), len(data[0])
    seen = set()

    def dfs(i, j):
        target = data[i][j]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        points = []
        for dx, dy in dirs:
            new_i, new_j = i+dx, j+dy
            if (new_i, new_j) not in seen:
                if 0 <= new_i < rows and 0 <= new_j < cols:
                    if data[new_i][new_j] == target:
                        seen.add((new_i, new_j))
                        points.append((new_i, new_j))

        if points:
            for (k, l) in points:
                new_points = dfs(k, l)
                if new_points:
                    points.extend(new_points)
        return points

    def calcSides(points):

        dirs = [(1,0), (-1,0), (0, 1), (0, -1)]
        x_boundary_edges_bottom = []
        x_boundary_edges_top = []
        y_boundary_edges_left = []
        y_boundary_edges_right = []
        for (i, j) in points:
            for (dx, dy) in dirs:
                if (i+dx, j+dy) not in points:
                    if dx == -1:
                        x_boundary_edges_bottom.append((i, j))
                    if dx == 1:
                        x_boundary_edges_top.append((i, j))
                    if dy == -1:
                        y_boundary_edges_left.append((j, i))
                    if dy == 1:
                        y_boundary_edges_right.append((j, i))


        x_boundary_edges_bottom.sort()
        x_boundary_edges_top.sort()
        y_boundary_edges_left.sort()
        y_boundary_edges_right.sort()

        def sides_boundary_edges(boundary_edges):
            if not boundary_edges:
                return 0
            prev, sides = None, 0
            for (i, j) in boundary_edges:
                if prev is None:
                    sides += 1
                    prev = (i, j)
                    continue
                if i == prev[0]:
                    if j-prev[1] > 1:
                        sides += 1
                else:
                    sides += 1
                prev = (i, j)
            return sides

        x_sides_bottom = sides_boundary_edges(x_boundary_edges_bottom)
        x_sides_top = sides_boundary_edges(x_boundary_edges_top)
        y_sides_left = sides_boundary_edges(y_boundary_edges_left)
        y_sides_right = sides_boundary_edges(y_boundary_edges_right)

        return x_sides_bottom+x_sides_top+y_sides_left+y_sides_right

    total = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) in seen:
                continue
            seen.add((i,j))
            points = dfs(i, j)
            points.append((i,j))
            area = len(points)
            sides = calcSides(points)
            total += area*sides

    return total

print(region(input))


