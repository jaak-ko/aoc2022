


with open("t9.txt", 'r') as f:
    data = [[r.strip().split(" ")[0], int(r.strip().split(" ")[1])] for r in f]

moves = {'R': 1, 'L':-1, 
         'U':1, 'D':-1}


def part_one():

    def diagonal_needed(h, t):
        return abs(h[0] - t[0]) == 2 and abs(h[-1] - t[-1]) == 1 or \
               abs(h[0] - t[0]) == 1 and abs(h[-1] - t[-1]) == 2

    def move_tail(h, t):
        diagonal_moves = [[t[0]+1, t[1]+1], [t[0]-1, t[1]-1],
                          [t[0]+1, t[1]-1], [t[0]-1, t[1]+1]]
        axial_moves = [[t[0], t[1]+1],[t[0], t[1]-1], 
                       [t[0]+1, t[1]], [t[0]-1, t[1]]]

        if diagonal_needed(h, t):
            for t_n in diagonal_moves:
                if abs(h[0] - t_n[0]) <= 1 and abs(h[-1] - t_n[-1]) <= 1:
                    return t_n
            
        for t_n in axial_moves:
            if abs(h[0] - t_n[0]) <= 1 and abs(h[-1] - t_n[-1]) <= 1:
                return t_n

    t_visits = set()
    h = [0, 0]
    t = [0, 0]

    t_visits.add(tuple(t))

    for row in data:
        d, amount = row
        for n in range(amount):

            if d in ['R', 'L']:
                h[0] += moves[d]
            else:
                h[-1] += moves[d]

            if abs(h[0] - t[0]) > 1 or abs(h[-1] - t[-1]) > 1:
                t = move_tail(h, t)
                t_visits.add((tuple(t)))

    return len(t_visits)

def main():

    print(f"part one: {part_one()}")

if __name__ == "__main__":
    main()