
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z']

def part_one():

    commons = []
    score = 0
    
    for line in open("t3.txt", 'r'):
        line_1, line_2 = line[:len(line)//2], line[len(line)//2:]
        commons.append(set(set(line_1)&set(line_2)).pop())
    
    for a in commons:
        score += alpha.index(a)+1 if a in alpha else \
            [c.upper() for c in alpha].index(a) + 27

    return score

def part_two():

    score = 0

    with open("t3.txt", 'r') as f:
        lines = f.read().split("\n")

    commons = []
    i = 0

    while i < len(lines):

        f, s, t= lines[i], lines[i+1], lines[i+2]
        commons.append(set(set(f)&set(s)&set(t)).pop())

        i += 3

    for a in commons:
        score += alpha.index(a)+1 if a in alpha else \
            [c.upper() for c in alpha].index(a) + 27

    return score

def main():

    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()