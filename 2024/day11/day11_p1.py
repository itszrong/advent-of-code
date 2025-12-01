import re
from collections import deque

input = open("data.txt", "r").read()

data = re.findall(r'\d+', input)
data = deque(data)

for _ in range(25):
    for i in range(len(data)):
        stone = data.popleft()
        if stone == "0":
            data.append("1")
        elif not stone:
            data.append("1")
        elif len(stone) % 2 == 0:
            left = stone[:len(stone)//2]    
            right = stone[len(stone)//2:]
            while left and len(left) > 0 and left[0] == "0":
                left = left[1:]
            while right and len(right) > 0 and right[0] == "0":
                right = right[1:]
            data.append(left)
            data.append(right)
        else:
            data.append(str(int(stone)*2024))

# print(data)
print(len(data))