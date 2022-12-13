

with open("t8.txt", 'r') as f:
    data = [list(map(int, [*i.strip()])) for i in f.readlines()]


def part_one(): 

    def check_visibility(x, y):
        
        return 1 if any(
            [
                all([data[y][i] < data[y][x] for i in range(x)]),
                all([data[y][i] < data[y][x] for i in range(x+1, len(data[y]))]),
                all([data[i][x] < data[y][x] for i in range(y)]),
                all([data[i][x] < data[y][x] for i in range(y+1, len(data))])
            ]
            ) else 0

    visibles = 0
    for y in range(1, len(data)-1):
        for x in range(1, len(data[y])-1):
            visibles += check_visibility(x, y)

    return visibles + 2*((len(data[0])-1) + (len(data)-1))


def part_two():

    def calc_scenic_score(x, y):

        scenic_score = 1
        for i in range(1, x + 1):
            if data[y][x-i] >= data[y][x] or x - i == 0:
                scenic_score *= i
                break

        for i in range(1, len(data[y]) - x):
            if data[y][x+i] >= data[y][x] or x + i == len(data[y])-1:
                scenic_score *= i
                break

        for i in range(1, y + 1):
            if data[y-i][x] >= data[y][x] or y - i == 0:
                scenic_score *= i
                break

        for i in range(1, len(data) - y):
            if data[y+i][x] >= data[y][x] or y + i == len(data)-1:
                scenic_score *= i
                break

        return scenic_score


    scores = set()
    for y in range(1, len(data)-1):
        for x in range(1, len(data[y])-1):
            scores.add(calc_scenic_score(x, y))

    return max(scores)

def main():
    

    print(f"part one: {part_one()}\npart two: {part_two()}")
    

if __name__ == "__main__":
    main()