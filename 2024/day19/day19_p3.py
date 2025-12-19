def main():
    with open("day19/data.txt", "r") as f:
        contents = f.read()

    parts = contents.split('\n\n')
    patterns = parts[0].split(', ')
    desired_list = parts[1].split('\n')

    memoized = {}
    def dfs(desired):
        check = memoized.get(desired)
        if check:
            return check
        
        res = 0
        if desired == '':
            return 1
        
        for pattern in patterns:
            if pattern == desired[:len(pattern)]:
                res += dfs(desired[len(pattern):])

        memoized[desired] = res
        return res

    res = 0
    for desired in desired_list:
        res += dfs(desired)

    print(res)

if __name__ == "__main__":
    main()
