
lists_str_2 = lists_str.replace("   ", ",")

print(lists_str_2)

# prompt: I currently have lists_str_2 as a str with number1, number2 then next line, number3, number4. Add odd numbers should be in a list and all even numbers should be in a separate list can you do this for me

odd_numbers = []
even_numbers = []

# Split the string into lines and then each line into numbers
for line in lists_str_2.strip().split('\n'):
  num1_str, num2_str = line.split(',')
  num1 = int(num1_str)
  num2 = int(num2_str)

  odd_numbers.append(num1)

  even_numbers.append(num2)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

odd_numbers.sort()
even_numbers.sort()
print(odd_numbers)
print(even_numbers)

distance = 0
for i, j in zip(odd_numbers, even_numbers):
  distance += abs(i-j)
print(distance)

# prompt: I want code to see how many times i appears in even_numbers

# Assuming odd_numbers and even_numbers are the lists from the previous step
# If you want to use the first and second numbers lists, replace odd_numbers with first_numbers and even_numbers with second_numbers

# Let's use the lists generated in the previous step: first_numbers and second_numbers
from collections import Counter
first_numbers = odd_numbers
second_numbers = even_numbers
# Create a Counter for second_numbers for efficient counting
second_numbers_counts = Counter(second_numbers)

# Dictionary to store the counts of each number from first_numbers in second_numbers
occurrence_counts = {}

# Iterate through each number in first_numbers
for number in first_numbers:
  # Get the count of this number in second_numbers
  count = second_numbers_counts.get(number, 0)
  # Store the count
  occurrence_counts[number] = count

# Print the occurrence counts
for number, count in occurrence_counts.items():
  print(f"Number {number} appears {count} times in the second numbers list.")

similarity_score = 0
for number, count in occurrence_counts.items():
  similarity_score += number*count
print(similarity_score)
