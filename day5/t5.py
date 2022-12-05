
stacks1 = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
stacks2 = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
not_chars = ["[", "]", " ", "\n"]


# create data for part 1
data1 = [[*i] for i in open("t5.txt", 'r').readlines()[:9]] + \
    [i.strip() .split(" ")for i in open("t5.txt", 'r').readlines()[9:]]

for row in data1[:8]:
    [stacks1[int(data1[8][i])].append(char) \
        for i, char in enumerate(row) if char not in not_chars]


#create data for part 2
data2 = [[*i] for i in open("t5.txt", 'r').readlines()[:9]] + \
    [i.strip() .split(" ")for i in open("t5.txt", 'r').readlines()[9:]]

for row in data2[:8]:
    [stacks2[int(data2[8][i])].append(char) \
        for i, char in enumerate(row) if char not in not_chars]


def part_one():

    for row in data1[10:]:
        amount, from_, to = int(row[1]), int(row[3]), int(row[-1])
        for _ in range(amount):
            stacks1[to].insert(0, (stacks1[from_].pop(0)))

    [print(stack[0], end='') for stack in stacks1.values()]


def part_two():

    for row in data2[10:]:
        amount, from_, to = int(row[1]), int(row[3]), int(row[-1])
        to_move = stacks2[from_][:amount]
        del stacks2[from_][:amount]
        stacks2[to][0:0] = to_move

    print()
    [print(stack[0], end='') for stack in stacks2.values()]



def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()