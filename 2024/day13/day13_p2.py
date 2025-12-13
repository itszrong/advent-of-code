import re

def main():
    with open("day13/data.txt", "r") as f:
        contents = f.read()

    parts = contents.split("\n\n")

    tokens = 0
    for part in parts:
        x = []
        y = []
        lines = part.split('\n')
        for (i, line) in enumerate(lines):
            nums = re.findall(r"\d+", line)
            x.append(int(nums[0]))
            y.append(int(nums[1]))
            if i == 2:
                x[2] += 10000000000000
                y[2] += 10000000000000
        b = (x[0]*y[2]-x[2]*y[0])/(-x[1]*y[0]+y[1]*x[0])
        a = (x[2]-x[1]*b)/x[0]
        if a%1 == 0 and b%1 == 0:
            tokens += 3*a + b
    
    print(int(tokens))

if __name__ == "__main__":
    main()
