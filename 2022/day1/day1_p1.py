def main():
    with open("day1/data.txt", "r") as f:
        contents = f.read()

    result = 0
    elves = contents.split('\n\n')
    for elf in elves:
        running = 0
        x = elf.split('\n')
        for i in x:
            running += int(i)
        result = max(result, running)
    print(result)

if __name__ == "__main__":
    main()
