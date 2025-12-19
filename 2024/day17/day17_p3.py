import re

def parse_input(path):
    with open(path, "r") as f:
        contents = f.read()
    parts = contents.split("\n\n")
    regs = list(map(int, re.findall(r"\d+", parts[0])))
    prog = list(map(int, re.findall(r"\d+", parts[1])))
    return regs, prog

def run_prefix_outputs(A0, B0, C0, program, need):
    A, B, C = A0, B0, C0
    ip = 0
    out = []

    def combo(x):
        if 0 <= x <= 3: return x
        if x == 4: return A
        if x == 5: return B
        if x == 6: return C
        raise ValueError("combo operand 7 is reserved")

    while ip < len(program) - 1 and len(out) < need:
        opcode = program[ip]
        operand = program[ip+1]

        if opcode == 0:      # adv
            k = combo(operand)
            A = int(A / (2 ** k))
        elif opcode == 1:    # bxl (literal)
            B ^= operand
        elif opcode == 2:    # bst
            k = combo(operand)
            B = k % 8
        elif opcode == 3:    # jnz (literal)
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:    # bxc
            B ^= C
        elif opcode == 5:    # out
            k = combo(operand)
            out.append(k % 8)
        elif opcode == 6:    # bdv
            k = combo(operand)
            B = int(A / (2 ** k))
        elif opcode == 7:    # cdv
            k = combo(operand)
            C = int(A / (2 ** k))
        else:
            raise ValueError("bad opcode")

        ip += 2

    return out

def find_smallest_A(regs, program):
    B0, C0 = regs[1], regs[2]
    target = program[:]  # required output
    n = len(target)

    # build A in base-8 from the end (most significant digit) to start
    def dfs(pos, base):
        # pos is the start index of the suffix we still need to match
        if pos < 0:
            return base

        suffix = target[pos:]
        need = len(suffix)

        for d in range(8):  # try digits low -> high for smallest A
            A_candidate = base * 8 + d
            out = run_prefix_outputs(A_candidate, B0, C0, program, need)

            if out == suffix:
                ans = dfs(pos - 1, A_candidate)
                if ans is not None:
                    return ans

        return None

    return dfs(n - 1, 0)

def main():
    regs, program = parse_input("day17/data.txt")
    A = find_smallest_A(regs, program)
    print(A)

if __name__ == "__main__":
    main()
