def main():
    with open("day22/data.txt", "r") as f:
        contents = f.read()

    def mix(x, s):
        return x^s
    def prune(x):
        return x%16777216

    data = contents.strip().split('\n')
    data = [int(x) for x in data]
    prices = [[] for _ in data]
    changes = [[0] for _ in data]

    def evolve(s):
        s1 = prune(mix(64*s, s))
        s2 = prune(mix(s1//32, s1))
        s3 = prune(mix(s2*2048, s2))
        return s3

    for (i, s) in enumerate(data):
        for j in range(2000):
            s = evolve(s)
            prices[i].append(s%10)
            if j > 0:
                changes[i].append(prices[i][-1]-prices[i][-2])
    
    sequence_map = {}

    for (i, prices_i) in enumerate(prices):
        for (j, price_j) in enumerate(prices_i):
            if j < 4:
                continue
            sequence = tuple(changes[i][j-3:j+1])
            if sequence not in sequence_map:
                sequence_map[sequence] = [None for _ in range(len(data))]
                sequence_map[sequence][i] = price_j
            else:
                if sequence_map[sequence][i] is None:
                    sequence_map[sequence][i] = price_j

    final_map = {}
    for key in sequence_map:
        final_map[key] = sum(x or 0 for x in sequence_map[key])

    print(max(final_map, key=final_map.get))
    print(max(final_map.values()))


if __name__ == "__main__":
    main()
