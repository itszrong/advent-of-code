import string

def main():
    with open("day3/data.txt", "r") as f:
        contents = f.read()

    lines = contents.splitlines()
    result = 0
    priorities = list(string.ascii_lowercase+string.ascii_uppercase)
    for i in range(int(len(lines)/3)):
        for c in lines[3*i]: 
            if c in lines[3*i+1] and c in lines[3*i+2]:
                result += (priorities.index(c)+1)
                break
                
    print(result)


if __name__ == "__main__":
    main()
