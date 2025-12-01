import re
from collections import deque, Counter, defaultdict
import shutil

input = open("data.txt", "r").read()

stones_map = re.findall(r'\d+', input)
stones_map = Counter(stones_map)

print(stones_map)

for j in range(75):

    new_map = defaultdict(int)
    for stone in stones_map:

        if stone == "0":
            new_map["1"] += int(stones_map[stone])
        elif not stone:
            new_map["1"] += int(stones_map[stone])
        elif len(stone) % 2 == 0:
            left = stone[:len(stone)//2]    
            right = stone[len(stone)//2:]
            while left and len(left) > 0 and left[0] == "0":
                left = left[1:]
            while right and len(right) > 0 and right[0] == "0":
                right = right[1:]
            new_map[left] += int(stones_map[stone])
            new_map[right] += int(stones_map[stone])
        else:
            new_map[str(int(stone)*2024)] += int(stones_map[stone])
        
    stones_map = new_map

# print(data)
print(sum(stones_map.values()))