

with open("t8.txt", 'r') as f:
    rows = [[*i.strip()] for i in f.readlines()]
    columns = [[e[i] for e in rows] for i in range(len(rows))]


def part_one():
    pass


def main():
    

    print(part_one())
    

if __name__ == "__main__":
    main()