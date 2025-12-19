import re
import string

def main():
    with open("day17/data.txt", "r") as f:
        contents = f.read()

    parts = contents.split("\n\n")
    registers = re.findall(r'\d+',  parts[0])
    registers = [int(i) for i in registers]
    program = re.findall(r'\d+',  parts[1])
    program = [int(i) for i in program]

    ops = {
        0: 'adv',
        1: 'bxl',
        2: 'bst',
        3: 'jnz',
        4: 'bxc',
        5: 'out',
        6: 'bdv',
        7: 'cdv',
    }


    def find(program, registers):
        i = 0
        output = []
        while i < len(program):
            # if len(output) > len(program):
            #     return []

            op = ops[program[i]]
            l_op = program[i+1]

            if program[i+1] >= 7:
                raise Exception("Not implemented")
            elif program[i+1] <= 3:
                combo = l_op
            else:
                combo = registers[l_op-4]

            #0
            if op == 'adv':
                registers[0] = int(registers[0] / (2**combo))
            #1
            elif op == 'bxl':
                registers[1] ^= l_op
            #2
            elif op == 'bst':
                registers[1] = combo % 8
            #3
            elif op == 'jnz':
                if registers[0] != 0:
                    i = program[i+1]
                    continue
            #4
            elif op == 'bxc':
                registers[1] ^= registers[2]
            #5
            elif op == 'out':
                output.append(combo % 8)
            #6
            elif op == 'bdv':
                registers[1] = int(registers[0] / (2**combo))
            #7
            elif op == 'cdv':
                registers[2] = int(registers[0] / (2**combo))

            i += 2

        return output

    try_list = [216549846240877]
    print(len(program))
    for i in try_list:
        registers = [i, 0, 0]
        output = find(program, registers)
        print(i, output)
        if output == program:
            print('found i', i)
            break

if __name__ == "__main__":
    main()