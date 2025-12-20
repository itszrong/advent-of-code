def main():
    with open("day22/data.txt", "r") as f:
        contents = f.read()

    def mix(x, s):
        return x^s
    def prune(x):
        return x%16777216

    data = contents.split('\n')
    data = [int(x) for x in data]

    def evolve(s):
        s1 = prune(mix(64*s, s))
        s2 = prune(mix(s1//32, s1))
        s3 = prune(mix(s2*2048, s2))
        return s3

    for (i, s) in enumerate(data):
        for _ in range(2000):
            s = evolve(s)
        data[i] = s

    print(sum(data))


if __name__ == "__main__":
    main()
