

elves = []
elf = []
idx = 0
for i in open("t1.txt", mode='r'):
    if i.strip() != "":
        elf.append(int(i.strip()))
        continue
    elves.append(sum(elf))
    elf = []
    idx += 1

print("1: ", max(elves))
print("2: ", sum(sorted(elves)[-3:]))

