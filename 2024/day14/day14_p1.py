import re
import math
def main():
    with open("day14/data.txt", "r") as f:
        contents = f.read()

    positions = []
    w = 101
    h = 103
    t = 100
    for line in contents.split('\n'):
        nums = re.findall(r'-?\d+', line)
        nums = [int(num) for num in nums]
        position = ((nums[0]+t*nums[2])%w, (nums[1]+t*nums[3])%h)
        positions.append(position)

    quadrants = [0 for i in range(4)]

    for (i, j) in positions:
        if i < w//2 and j < h//2:
            quadrants[0] += 1
        if i > w//2 and j < h//2:
            quadrants[1] += 1
        if i < w//2 and j > h//2:
            quadrants[2] += 1
        if i > w//2 and j > h//2:
            quadrants[3] += 1

    print(math.prod(quadrants))

if __name__ == "__main__":
    main()
