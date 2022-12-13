

def parts(n):

    line = open("t6.txt", 'r').readline()
    return min([idx + 1 for idx in range(n, len(line)) if \
                            len(set(line[idx-(n-1):idx+1])) == n])

def main():
    print(f"part one: {parts(4)}\npart two: {parts(14)}")

if __name__ == "__main__":
    main()