def main():
    with open("day19/data.txt", "r") as f:
        contents = f.read()

    parts = contents.split('\n\n')
    patterns = parts[0].split(', ')
    desired_list = parts[1].split('\n')

    def dfs(patterns, desired):
        if desired == '':
            return True
        
        for pattern in patterns:
            if pattern == desired[:len(pattern)]:
                if dfs(patterns, desired[len(pattern):]):
                    return True

        return False

    res = 0
    for desired in desired_list:
        if dfs(patterns, desired):
            res += 1

    print(res)

if __name__ == "__main__":
    main()
