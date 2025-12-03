input = open("data.txt", "r").read()

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

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        x_buffer = []
        y_buffer = []
        for i, j in points:
            for dx, dy in dirs:
                new_i, new_j = i+dx, j+dy
                if -1 <= new_i < rows+1 and -1 <= new_j < cols+1:
                    if (new_i, new_j) not in points:
                        if dx != 0:
                            x_buffer.append((new_i, new_j))
                        else:
                            y_buffer.append((new_j, new_i))

        x_buffer.sort()
        y_buffer.sort()

        # print(data[points[0][0]][points[0][1]], x_buffer)
        # print(data[points[0][0]][points[0][1]], y_buffer)

        def get_sides(buffer):
            sides = 0
            prev = (-10, -10)
            duplicates = []
            if not buffer:
                return 0, []
            for i, j in buffer:
                if i == prev[0]:
                    if j == prev[1]:
                        duplicates.append((i,j))
                        # continue
                    if abs(j-prev[1]) != 1:
                        sides += 1
                else:
                    sides += 1
                prev = (i, j)
            return sides, duplicates

        x_sides, x_duplicates = get_sides(x_buffer)
        y_sides, y_duplicates = get_sides(y_buffer)

        # print(x_duplicates)
        # print(y_duplicates)
        
        x_dup_sides, _ = get_sides(x_duplicates)
        y_dup_sides, _ = get_sides(y_duplicates)


        vis = []
        for i in range(-1, rows+1, 1):
            vis_sub = []
            for j in range(-1, cols+1, 1):
                if (i, j) in x_buffer or (j, i) in y_buffer:
                    vis_sub.append("*")
                elif (i, j) in points:
                    vis_sub.append(data[i][j])
                else:
                    vis_sub.append(" ")
            vis.append(vis_sub)

        x_sides = x_sides+x_dup_sides-len(x_duplicates)
        x_sides = y_sides+y_dup_sides-len(y_duplicates)
        sides = x_sides+y_sides
        print(sides, x_sides, y_sides, x_dup_sides, y_dup_sides)
        for row in vis:
            if any(el != " " for el in row):
                print("".join(row))

        return sides

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
            # print(data[i][j], area, sides, "coord:", (i, j), "price", area*sides)
            total += area*sides

    return total

print(region(input))


