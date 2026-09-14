from collections import Counter

def main():
    with open("day6/data.txt", "r") as f:
        contents = f.read()

    l = 14
    for i in range(len(contents)):
        counts = Counter(contents[i:i+l])
        if len(list(counts.keys())) == l:
            break
    print(i+l)


if __name__ == "__main__":
    main()
