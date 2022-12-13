
scores = {"X": 1, "Y": 2, "Z": 3}

draws = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
losses = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]
wins = [['C', 'X'], ['A', 'Y'], ['B', 'Z']]


def part_one():

    myscore = 0
    for i in open("t2.txt", 'r'):

        situ = [i.strip() for i in i.split(" ")]

        if situ in draws:
            myscore += scores[situ[1]] + 3

        elif situ in losses:
            myscore += scores[situ[1]]
            
        else:
            myscore += scores[situ[1]] + 6

    return myscore

def part_two():


    myscore = 0
    for i in open("t2.txt", 'r'):

        i = [i.strip() for i in i.split(" ")]

        if i[1] == 'X':
            for situ in losses:
                if i[0] in situ:
                    myscore += scores[situ[1]]

        elif i[1] == 'Y':
            for situ in draws:
                if i[0] in situ:
                    myscore += scores[situ[1]] + 3
            
        else:
            for situ in wins:
                if i[0] in situ:
                    myscore += scores[situ[1]] + 6

    return myscore


def main():

    print(part_one())
    print(part_two())

if __name__ == "__main__":
    main()
