import re

def main():
    with open("day5/data.txt", "r") as f:
        contents = f.read()

    crates, moves = contents.split('\n\n')

    crate_rows = crates.splitlines()
    grid = []
    for row in crate_rows:
        grid.append(list(row))
            
    num_stacks = grid[-1][-2]
    stacks = [[] for i in range(int(num_stacks))]
    for i in range(len(grid[0])):
        if grid[-1][i] != ' ':
            for j in reversed(range(len(grid)-1)):
                if grid[j][i] == ' ':
                    break
                stacks[int(grid[-1][i])-1].append(grid[j][i])

    for move in moves.splitlines():
        move_nums = re.findall(r'\d+', move)
        move_nums = [int(x) for x in move_nums]
        move_nums[1] -= 1
        move_nums[2] -= 1
        to_move_list = []
        for i in range(move_nums[0]):
            if len(stacks[move_nums[1]]) == 1:
                to_move_list.append(stacks[move_nums[1]][0])
                stacks[move_nums[1]] = []
            else:
                to_move_list.append(stacks[move_nums[1]].pop())
        stacks[move_nums[2]] = stacks[move_nums[2]] + to_move_list
        
    print(''.join(([stack[-1] for stack in stacks])))

if __name__ == "__main__":
    main()
