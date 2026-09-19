def main():
    with open("day9/data.txt", "r") as f:
        contents = f.read()

    H = (0, 0)
    T = (0, 0)
    positions = set((0,0))
    moves = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }

    for line in contents.splitlines():
        dir, n = line.split(' ')
        d = moves[dir]
        for i in range(int(n)):
            prev_H = H
            H = (H[0]+d[0], H[1]+d[1])
            if abs(H[0]-T[0]) > 1 or abs(H[1]-T[1]) > 1:
                T = prev_H
                positions.add(T)
    print(len(positions))


if __name__ == "__main__":
    main()
