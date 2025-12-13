import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def main():
    with open("day14/data.txt", "r") as f:
        contents = f.read()

    w = 101
    h = 103
    nums_list = []
    for line in contents.split('\n'):
        nums = re.findall(r'-?\d+', line)
        nums_list.append([int(num) for num in nums])
    

    fig = plt.figure()
    t_total = 1000
    grids = []
    for t in range(6446,6447):
        grid = np.zeros((h, w))
        for nums in nums_list:
            position = ((nums[0]+t*nums[2])%w, (nums[1]+t*nums[3])%h)
            grid[position[1]][position[0]] += 1
        grids.append(grid)

    im = plt.imshow(grids[0], animated=True)

    def updatefig(frame):
        im.set_array(grids[frame])
        return (im,)
    
    ani = animation.FuncAnimation(fig, updatefig, frames=len(grids), interval=1000, blit=True)
    plt.show()

if __name__ == "__main__":
    main()
