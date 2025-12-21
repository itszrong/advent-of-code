def main():
    with open("day25/data.txt", "r") as f:
        contents = f.read()

    locks = []
    keys = []

    def convert(part):
        values = [0 for _ in range(5)]
        for row in part.splitlines():
            for (i, c) in enumerate(row):
                if c == '#':
                    values[i] += 1
        return values

    for part in contents.split('\n\n'):
        if part[:5] == '#####':
            locks.append(convert(part))
        else:
            keys.append(convert(part))

    res = 0
    for lock in locks:
        for key in keys:
            valid = True
            for i in [lock[i]+key[i] for i in range(len(lock))]:
                if i > 7:
                    valid = False
            if valid:
                res += 1
                
    print(res)


if __name__ == "__main__":
    main()
