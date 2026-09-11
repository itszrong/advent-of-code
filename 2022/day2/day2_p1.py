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
    for round in rounds:
        result += my_mapping[round[-1]]
        if round in win_list:
            result += 6
        elif round in draw_list:
            result += 3
        elif round in lose_list:
            pass
        else:
            raise Exception("Sorry, not following rules") 
    print(result)


if __name__ == "__main__":
    main()
