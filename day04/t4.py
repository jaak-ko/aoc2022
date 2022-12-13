
import time

start = time.time()
with open("t4.txt", 'r') as file:
        data = [[e[0].split("-"), e[1].strip().split("-")] 
                for e in [i.split(",") for i in file.readlines()]]


def part_one():

    print(data[0])

    def rule1(i):
        ff, fs, sf, ss = int(i[0][0]), int(i[0][1]), int(i[1][0]), int(i[1][1])
        return True if ff <= sf and fs >= ss or sf <= ff and ss >= fs else False
    
    return list(map(lambda i : 1 if rule1(i) else 0, data)).count(1)

    
def part_two():

    def rule2(i):
        ff, fs, sf, ss = int(i[0][0]), int(i[0][1]), int(i[1][0]), int(i[1][1])
        return False if fs < sf or ss < ff else True

    return list(map(lambda i : 1 if rule2(i) else 0, data)).count(1)
    

def main():

    end = time.time()
    print(f"PART 1: {part_one()} \nPART 2: {part_two()}")
    print(f"{(end-start)*1000:.3f} milliseconds")

if __name__ == "__main__":
    main()