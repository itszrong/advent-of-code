# Placeholder for day3 part 2
import re

def extract_uncorrupted(input):
    pattern = r"mul\((\d+),(\d+)\)"
    return re.split(pattern, input)

def extract_do_dont(input):
    pattern = r"do\(\)|don't\(\)"
    return re.findall(pattern, input)

def get_dos_donts_indices(numbers_list):
    do_index = []
    dont_index = []
    for i in range(len(numbers_list)):
      j = numbers_list[i]
      if j == ["do()"]:
        do_index.append(i)
      elif j == ["don't()"]:
        dont_index.append(i)
      elif j != ["do()"] and j != ["don't()"] and type(j) == list:
        if j[-1] == ["do()"]:
          do_index.append(i)
        elif j[-1] == ["don't()"]:
          dont_index.append(j)

    return do_index, dont_index

def main():

    with open("day3/data.txt", "r") as f:
        contents = f.read()

    extracted = extract_uncorrupted(contents)
    for i in range(len(extracted)):
      if extracted[i].isdigit() == False:
        extracted[i] = extract_do_dont(extracted[i])

    new_extracted = []
    for i in extracted:
      if i != []:
          new_extracted.append(i)

    do_index, dont_index = get_dos_donts_indices(new_extracted)

    index = 0
    tuples_extracted_and_rest = []
    for j in range(len(new_extracted)):
      i = new_extracted[j]
      if type(i) == list:
        tuples_extracted_and_rest.append(i)
      elif i == new_extracted[-1]:
        break
      else:
        if index % 2 != 0:
          index += 1
        elif i.isdigit() == True and index % 2 == 0:
          tuples_extracted_and_rest.append((i, new_extracted[j+1]))
          index += 1

    bool = True
    sum = 0
    for i in range(len(tuples_extracted_and_rest)):
      j = tuples_extracted_and_rest[i]
      if j == ["do()"]:
        bool = True
      elif j == ["don't()"]:
        bool = False
      else:
        if bool == True:
          sum += int(j[0]) * int(j[1])
          
    print(sum)

if __name__ == "__main__":
    main()
