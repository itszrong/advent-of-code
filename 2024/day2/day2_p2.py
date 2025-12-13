def main():
    with open("day2/data.txt", "r") as f:
        contents = f.read()

    def check(line):
        prev = prev_diff = None
        for curr in line:
            if not prev:
                prev = curr
                continue
            diff = curr - prev
            if abs(diff) < 1 or abs(diff) > 3:
                return False
            if prev_diff and ((prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0)):
                return False
            prev_diff, prev = diff, curr

        return True 

    res = 0
    for line in contents.splitlines():
        line = [int(num) for num in line.split()]
        if check(line):
            res += 1
            continue
        for i in range(len(line)):
            if check(line[:i]+line[i+1:]):
                valid = True
                res += 1
                break
    
    print(res)


if __name__ == "__main__":
    main()
