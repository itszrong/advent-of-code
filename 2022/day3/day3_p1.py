import string

def main():
    with open("day3/data.txt", "r") as f:
        contents = f.read()

    lines = contents.splitlines()
    result = 0
    priorities = list(string.ascii_lowercase+string.ascii_uppercase)
    for line in lines:
        if len(line)%2 != 0:
            print('odd')
        x = line[0:int(len(line)/2)]
        y = line[int(len(line)/2):]
        for i in x: 
            if i in y:
                result += (priorities.index(i)+1)
                break
                
    print(result)


if __name__ == "__main__":
    main()
