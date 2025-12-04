# pip install regex
import regex as re
def reg_find(text):
    pattern = r'(\d+)'
    matches = re.findall(pattern, text)
    return matches

matches = [reg_find(line) for line in input_str.split("\n")]
matches[0]

# def check(line, operators):
#     priority_operators = ['*', '/']
#     equation = []
#     sum = 0
#     for i in range(line):
#         if equation != []:
#             if equation[-1] == "*":
#                 equation[-2] = equation[-2] * line[i] 
#                 del equation[-1]
#             elif equation[-1] == "/":
#                 equation[-2] = equation[-2] / line[i] 
#                 del equation[-1]
#             else:
#                 equation.append(int(line[i]))
#         if i <= len(operators):
#             equation.append(operators[i])
    
#     for i in range(len(equation)//2):
#         if i == 0:
#             sum = equation[i]
#         else:
#             if equation[2*i+1] == '+':
#                 sum += equation[2*i]
#             if equation[2*i+1] == '-':
#                 sum -= equation[2*i]
            
#     return sum

# def permutations_recursive(operators, spaces):
#     permutations_list = []
#     order_list = []

#     if spaces == 0:
#         return []
#     if spaces == 1:
#         return [[op] for op in operators]

#     result = []
#     for op in operators:

#         sub_permutations = permutations_recursive(operators, spaces-1)
        
#         for sub_perm in sub_permutations:
#             result.append([op[0] + sub_perm])

#     return result
        
# operators = ['*', '+']
# final_sum = 0
# for line in matches:
#     spaces = len(line) -1
#     operators_order_list = permutations_recursive(operators, spaces)
#     for order in operators_order_list:
#         sum = check(line[1:], order)
#         if sum == line[0]:
#             final_sum += sum


def check(line, operators):
    priority_operators = ['*', '/']
    equation = []
    
    for i in range(len(line)):
        if equation:  # If equation is not empty
            if equation[-1] == "*":
                equation[-2] = equation[-2] * int(line[i]) 
                del equation[-1]
            elif equation[-1] == "/":
                if int(line[i]) == 0:  # Check for division by zero
                    return None
                equation[-2] = equation[-2] / int(line[i]) 
                del equation[-1]
            else:
                equation.append(int(line[i]))
        else:
            equation.append(int(line[i]))
            
        if i < len(operators):
            equation.append(operators[i])
    
    # Now handle addition and subtraction
    sum = equation[0]
    for i in range(1, len(equation), 2):
        if i + 1 < len(equation):
            if equation[i] == '+':
                sum += equation[i + 1]
            elif equation[i] == '-':
                sum -= equation[i + 1]
    
    return sum

def permutations_recursive(operators, spaces):
    if spaces == 0:
        return [[]]
    if spaces == 1:
        return [[op] for op in operators]

    result = set()
    for op in operators:
        sub_permutations = permutations_recursive(operators, spaces-1)
        for sub_perm in sub_permutations:
            result.add(tuple([op] + sub_perm))  # Convert to tuple

    return [list(perm) for perm in result]  # Convert back to lists

# Main execution
operators = ['*', '+']
final_sum = 0

for line in matches:
    spaces = len(line) - 2
    operators_order_list = permutations_recursive(operators, spaces)
    
    for order in operators_order_list:
        result = check(line[1:], order)
        if result is not None and result == int(line[0]):
            final_sum += result

print(f"Final sum: {final_sum}")

from itertools import product

def check(line, operators):
    priority_operators = ['*', '/']
    equation = []
    
    for i in range(len(line)):
        if equation:  # If equation is not empty
            if equation[-1] == "*":
                equation[-2] = equation[-2] * int(line[i]) 
                del equation[-1]
            elif equation[-1] == "/":
                if int(line[i]) == 0:  # Check for division by zero
                    return None
                equation[-2] = equation[-2] / int(line[i]) 
                del equation[-1]
            else:
                equation.append(int(line[i]))
        else:
            equation.append(int(line[i]))
            
        if i < len(operators):
            equation.append(operators[i])
    
    # Now handle addition and subtraction
    sum = equation[0]
    for i in range(1, len(equation), 2):
        if i + 1 < len(equation):
            if equation[i] == '+':
                sum += equation[i + 1]
            elif equation[i] == '-':
                sum -= equation[i + 1]
    
    return sum

# Main execution
operators = ['*', '+']
final_sum = 0
solutions_found = 0

for line_idx, line in enumerate(matches):
    target = int(line[0])
    numbers = line[1:]
    
    spaces = len(numbers) - 1
    operators_order_list = list(product(operators, repeat=spaces))
    
    line_solved = False
    for order in operators_order_list:
        result = check(numbers.copy(), list(order))
        if result is not None and result == target:
            final_sum += result
            solutions_found += 1
            print(f"Line {line_idx}: {numbers} with {order} = {result} (target: {target})")
            line_solved = True
            break
    
    if not line_solved:
        print(f"Line {line_idx}: No solution found for {numbers} -> target {target}")

print(f"Final sum: {final_sum}")
print(f"Solutions found: {solutions_found}")
print(f"Total lines: {len(matches)}")

from itertools import product

def check_left_to_right(line, operators):
    """Evaluate expression left-to-right (no operator precedence)"""
    if len(line) != len(operators) + 1:
        return None
    
    result = int(line[0])
    
    for i, op in enumerate(operators):
        if op == '+':
            result += int(line[i + 1])
        elif op == '*':
            result *= int(line[i + 1])
    
    return result

# Main execution
operators = ['*', '+']
final_sum = 0

for line in matches:
    target = int(line[0])
    numbers = line[1:]
    
    spaces = len(numbers) - 1
    operators_order_list = list(product(operators, repeat=spaces))
    
    for order in operators_order_list:
        result = check_left_to_right(numbers, list(order))
        if result == target:
            final_sum += target
            break  # Found a solution for this line

print(f"Final sum: {final_sum}")

from itertools import product

def check_left_to_right(line, operators):
    """Evaluate expression left-to-right (no operator precedence)"""
    if len(line) != len(operators) + 1:
        return None
    
    result = int(line[0])
    
    for i, op in enumerate(operators):
        if op == '+':
            result += int(line[i + 1])
        elif op == '*':
            result *= int(line[i + 1])
        elif op == '||':
            result = int(str(result) + str(line[i + 1]))
    
    return result

# Main execution
operators = ['*', '+', '||']
final_sum = 0
solutions_found = 0

for line_idx, line in enumerate(matches):
    target = int(line[0])
    numbers = line[1:]
    
    spaces = len(numbers) - 1
    operators_order_list = list(product(operators, repeat=spaces))
    
    line_solved = False
    for order in operators_order_list:
        result = check_left_to_right(numbers.copy(), list(order))
        if result is not None and result == target:
            final_sum += result
            solutions_found += 1
            # print(f"Line {line_idx}: {numbers} with {order} = {result} (target: {target})")
            line_solved = True
            break
    
    # if not line_solved:
    #     print(f"Line {line_idx}: No solution found for {numbers} -> target {target}")

print(f"Final sum: {final_sum}")
print(f"Solutions found: {solutions_found}")
print(f"Total lines: {len(matches)}")
