







def part_one():

    stacks = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

    not_chars = ["[", "]", " ", "\n"]

    data = [[*i] for i in open("t5.txt", 'r').readlines()[:9]] + \
        [i.strip() .split(" ")for i in open("t5.txt", 'r').readlines()[9:]]

    for row in data[:8]:
        [stacks[int(data[8][i])].append(char) \
            for i, char in enumerate(row) if char not in not_chars]

    for row in data[10:]:
        amount, from_, to = int(row[1]), int(row[3]), int(row[-1])
        for _ in range(amount):
            stacks[to].insert(0, (stacks[from_].pop(0)))

    [print(stack[0], end='') for stack in stacks.values()]




def main():
    part_one()

if __name__ == "__main__":
    main()