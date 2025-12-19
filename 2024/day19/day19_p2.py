from functools import lru_cache

def main():
    with open("day19/data.txt", "r") as f:
        contents = f.read()

    parts = contents.split('\n\n')
    patterns = parts[0].split(', ')
    desired_list = parts[1].split('\n')

    @lru_cache(maxsize=100000000)
    def dfs(desired):
        res = 0
        if desired == '':
            return 1
        
        for pattern in patterns:
            if pattern == desired[:len(pattern)]:
                res += dfs(desired[len(pattern):])

        return res

    res = 0
    for desired in desired_list:
        res += dfs(desired)

    print(res)

if __name__ == "__main__":
    main()
