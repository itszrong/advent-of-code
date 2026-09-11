def main():
    with open("day1/data.txt", "r") as f:
        contents = f.read()

    results = []
    elves = contents.split('\n\n')
    for elf in elves:
        running = 0
        x = elf.split('\n')
        for i in x:
            running += int(i)
        results.append(running)
    results.sort(reverse=True)
    print(sum(results[0:3]))

if __name__ == "__main__":
    main()
