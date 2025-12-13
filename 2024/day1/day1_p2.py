from collections import Counter

def main():
    with open("day1/data.txt", "r") as f:
        contents = f.read()

    col1, col2 = [], []
    for line in contents.splitlines():
        col1.append(int(line.split()[0]))
        col2.append(int(line.split()[1]))

    col1.sort()
    col2.sort()

    freq = Counter(col2)

    res = 0
    for i in range(len(col1)):
        res += col1[i]*freq[col1[i]]

    print(res)


if __name__ == "__main__":
    main()
