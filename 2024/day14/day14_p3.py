import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np

def main():
    with open("day14/data.txt", "r") as f:
        contents = f.read()

    w = 101
    h = 103
    nums_list = []
    entropy_list = []
    for line in contents.split('\n'):
        nums = re.findall(r'-?\d+', line)
        nums_list.append([int(num) for num in nums])
    

    t_total = np.arange(0, 10000)
    overlapping = [0 for t in range(len(t_total))]
    for (i, t) in enumerate(t_total):
        grid = np.zeros((w, h))
        for nums in nums_list:
            position = ((nums[0]+t*nums[2])%w, (nums[1]+t*nums[3])%h)
            if grid[position[0]][position[1]] >= 1:
                overlapping[i] += 1
            grid[position[0]][position[1]] += 1
        marg = np.histogramdd(np.ravel(grid), bins = 256)[0]/grid.size
        marg = list(filter(lambda p: p > 0, np.ravel(marg)))
        entropy = -np.sum(np.multiply(marg, np.log2(marg)))
        entropy_list.append(entropy)


    plt.plot(t_total, entropy_list)
    plt.show()

if __name__ == "__main__":
    main()
