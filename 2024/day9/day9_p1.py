# input = "2333133121414131402"
isOdd = True
counter = 0
array = []
num_dots = 0
for i in range(len(input)):
    if isOdd == True:
        for j in range(int(input[i])):
            array.append(str(counter))
        counter += 1
        isOdd = False
    elif isOdd == False:
        for j in range(int(input[i])):
            array.append(".")
            num_dots += 1
        isOdd = True

print("".join(array))

p1, p2 = 0, len(array)-1
while p1 < p2:
    if array[p1] == ".":
        if array[p2] != ".":
            array[p1], array[p2] = array[p2], array[p1]
            p1 += 1
            p2 -= 1 
        else:
            p2 -=1
    else:
        p1 += 1
# print("".join(array))

checksum = 0
for i, val in enumerate(array):
    if val != ".":
        checksum += i * int(val)
checksum

# input = "2333133121414131402"
isOdd = True
counter = 0
array = []
sizeHash = {}
num_dots = 0
for i in range(len(input)):
    if isOdd == True:
        for j in range(int(input[i])):
            array.append(str(counter))
        counter += 1
        isOdd = False
    elif isOdd == False:

        if int(input[i]): #ignore 0 "."
            if int(input[i]) not in sizeHash:
                sizeHash[int(input[i])] = []
            sizeHash[int(input[i])].append((len(array)+1, len(array)+int(input[i])))

        for j in range(int(input[i])):
            array.append(".")
            num_dots += 1
        isOdd = True

print("".join(array))

p2 = len(array)-1
size, val = 0, array[p2]
while p2 > 0:
    if array[p2] == val:
        if val != ".":
            size += 1
        p2 -= 1
    else:
        smallest_position = float("inf")
        key_to_use = None
        if val != ".":
            for key in sizeHash:
                if key >= size:
                    if smallest_position > sizeHash[key][0][0]:
                        key_to_use = key
                        smallest_position = sizeHash[key][0][0]
            if key_to_use:
                pos_start, pos_end = sizeHash[key_to_use][0][0], sizeHash[key_to_use][0][1]
                if pos_start-1 < p2+1:
                    new_spot = sizeHash[key_to_use].pop(0)
                    if pos_end-pos_start+1 > size:
                        if pos_end-pos_start+1-size not in sizeHash:
                            sizeHash[pos_end-pos_start+1-size] = []
                        sizeHash[pos_end-pos_start+1-size].append((pos_start+size, pos_end))
                        sizeHash[pos_end-pos_start+1-size].sort(key=lambda x: x[0])
                    if len(sizeHash[key_to_use]) == 0:
                        del sizeHash[key_to_use]
                    for i in range(pos_start-1, pos_start-1+size):
                        array[i] = val
                    for i in range(p2+1, p2+size+1):
                        array[i] = "."
        size = 1
        val = array[p2]
        p2 -= 1

print("".join(array))

checksum = 0
for i, val in enumerate(array):
    if val != ".":
        checksum += i * int(val)
checksum
