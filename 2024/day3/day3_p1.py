import re

def extract(input):
    pattern = r"mul\((\d+),(\d+)\)"
    return re.findall(pattern, input)

def main():

    with open("day3/data.txt", "r") as f:
        contents = f.read()

    res = 0
    extracted = extract(contents)
    for (x, y) in extracted:
        res += int(x)*int(y)
  
    print(res)

if __name__ == "__main__":
    main()
