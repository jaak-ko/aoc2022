
with open("t10.txt", 'r') as f:
    data = [r.strip().split(" ") for r in f.readlines()]


def part_one():

    def check(cycle): return cycle in [20, 60, 100, 140, 180, 220]

    x = 1
    solution = 0
    cycle = 0
    cycle_checked = False

    for idx, row in enumerate(data):

        if row[0] == "addx":
            for _ in range(2):
                cycle += 1
                cycle_checked = False
                if check(cycle) and not cycle_checked:
                    solution += x * cycle
                    cycle_checked = True
            x += int(row[-1])
        else:
            if check(cycle) and not cycle_checked:
                solution += x * cycle
                cycle_checked = True

            cycle += 1
            cycle_checked = False

    return solution

def part_two():

    x = 1
    cycle = 0
    pixels = ""
    for idx, row in enumerate(data):

        if cycle == 39:
            r = ""
        if row[0] == "addx":
            for _ in range(2):
                pixels += '#'if cycle % 40 in range(x-1, x+2) else '.'
                cycle += 1
            x += int(row[-1])
        else:
            pixels += '#'if cycle % 40 in range(x-1, x+2) else '.'
            cycle += 1

    for idx, c in enumerate([*pixels]):
        print(c, end="") if (idx + 1) % 40 != 0 or idx == 0 else print(c)

def main():

    print(f"part one: {part_one()}")
    print(f"part two:")
    part_two()

if __name__ == "__main__":
    main()