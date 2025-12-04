import regex
def extract_uncorrupted(input):
  """
  Extracts 'mul(X,Y)' patterns where X and Y are numbers from the input string.

  Args:
    input: The input string.

  Returns:
    A list of strings matching the pattern.
  """
  # Use regex to find all occurrences of "mul(X,Y)" where X and Y are digits
  pattern = r"mul\((\d+),(\d+)\)"
  pattern_do = r"do()"
  pattern_dont = r"don't()"
  return regex.split(pattern, input)

def extract_do_dont(input):
  """
  Extracts 'mul(X,Y)' patterns where X and Y are numbers from the input string.

  Args:
    input: The input string.

  Returns:
    A list of strings matching the pattern.
  """
  # Use regex to find all occurrences of "mul(X,Y)" where X and Y are digits
  pattern = r"do\(\)|don't\(\)"
  return regex.findall(pattern, input)

extracted = extract_uncorrupted(input)
for i in range(len(extracted)):
  if extracted[i].isdigit() == False:
    extracted[i] = extract_do_dont(extracted[i])
print(extracted)

print(extracted)

new_extracted = []
for i in extracted:
  if i != []:
      new_extracted.append(i)

print(new_extracted)

def get_dos_donts_indices(numbers_list):
  """
  Extracts 'mul(X,Y)' patterns where X and Y are numbers from the input string.

  Args:
    input: The input string.

  Returns:
    A list of strings matching the pattern.
  """
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

do_index, dont_index = get_dos_donts_indices(new_extracted)
print(do_index)
print(dont_index)

print(new_extracted)

index = 0
tuples_extracted_and_rest = []
for j in range(len(new_extracted)):
  i = new_extracted[j]
  if type(i) == list:
    tuples_extracted_and_rest.append(i)
    # print('list')
  elif i == new_extracted[-1]:
    break
  else:
    if index % 2 != 0:
      index += 1
      # print('odd')
    elif i.isdigit() == True and index % 2 == 0:
      tuples_extracted_and_rest.append((i, new_extracted[j+1]))
      index += 1
      # print('even')
print(tuples_extracted_and_rest)

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
