from __future__ import annotations

from collections import defaultdict
from functools import lru_cache


def main():
    with open("day24/data.txt", "r") as f:
        contents = f.read()

    d, gates = parse(contents)

    # Part 1
    part1 = eval_z_number(d)
    print(part1)

    # Part 2
    part2 = find_swapped_wires(d, gates)
    print(part2)


def parse(contents: str):
    a, b = contents.strip().split("\n\n")

    d = {}  # wire -> int OR (op, w1, w2)
    for line in a.splitlines():
        name, val = line.split(": ")
        d[name] = int(val)

    gates = []  # (w1, op, w2, out)
    for line in b.splitlines():
        w1, op, w2, _, out = line.split()
        d[out] = (op, w1, w2)
        gates.append((w1, op, w2, out))

    return d, gates


def eval_z_number(d):
    # evaluate all z?? wires and pack into an integer (z00 = bit0, z01 = bit1, ...)
    z_wires = sorted([k for k in d.keys() if k.startswith("z")])

    @lru_cache(maxsize=None)
    def eval_wire(w: str) -> int:
        v = d[w]
        if isinstance(v, int):
            return v
        op, a, b = v
        x = eval_wire(a)
        y = eval_wire(b)
        if op == "AND":
            return x & y
        if op == "OR":
            return x | y
        if op == "XOR":
            return x ^ y
        raise ValueError(f"Unknown op: {op}")

    out = 0
    for i, zw in enumerate(z_wires):
        out |= (eval_wire(zw) & 1) << i
    return out


def find_swapped_wires(d, gates):
    # Heuristic rules that identify the "bad" / swapped wires for the typical ripple-carry adder structure.
    z_wires = sorted([k for k in d.keys() if k.startswith("z")])
    last_z = z_wires[-1] if z_wires else None

    uses = defaultdict(list)  # wire -> list of (consumer_out, consumer_op)
    for w1, op, w2, out in gates:
        uses[w1].append((out, op))
        uses[w2].append((out, op))

    wrong = set()

    for out, expr in d.items():
        if not isinstance(expr, tuple):
            continue
        op, w1, w2 = expr

        # Rule 1: all z?? wires are XOR except the highest bit (carry out) which is OR
        if out.startswith("z") and out != last_z and op != "XOR":
            wrong.add(out)

        # Rule 2: internal XORs are suspicious (XORs should be closely tied to x/y/z families)
        if op == "XOR":
            if out[0] not in ("x", "y", "z") and w1[0] not in ("x", "y", "z") and w2[0] not in ("x", "y", "z"):
                wrong.add(out)

        # Rule 3: AND gates (except seed carry from x00/y00) should feed OR gates (carry combine)
        if op == "AND" and "x00" not in (w1, w2) and "y00" not in (w1, w2):
            for consumer_out, consumer_op in uses.get(out, []):
                if consumer_op != "OR":
                    wrong.add(out)
                    break

        # Rule 4: XOR outputs should never feed an OR gate in a ripple-carry adder
        if op == "XOR":
            for consumer_out, consumer_op in uses.get(out, []):
                if consumer_op == "OR":
                    wrong.add(out)
                    break

    return ",".join(sorted(wrong))


if __name__ == "__main__":
    main()
