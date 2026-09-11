def main():
    with open("day2/data.txt", "r") as f:
        contents = f.read()

    rounds = contents.splitlines()
    result = 0
    op_mapping = {'A': 1, 'B': 2, 'C': 3}
    my_mapping = {'X': 1, 'Y': 2, 'Z': 3}
    win_list = ['A Y', 'B Z', 'C X']
    lose_list = ['A Z', 'B X', 'C Y']
    draw_list = ['A X', 'B Y', 'C Z']

    def find_my_move(state_list, state):
        i = op_mapping[round[0]]-1
        my_move = state_list[i][-1]
        return my_mapping[my_move] + state

    for round in rounds:
        if round[-1] == 'X':
            result += find_my_move(lose_list, 0)
        elif round[-1] == 'Y':
            result += find_my_move(draw_list, 3)
        elif round[-1] == 'Z':
            result += find_my_move(win_list, 6)
        else:
            raise Exception("Sorry, not following rules") 
    print(result)


if __name__ == "__main__":
    main()