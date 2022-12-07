
with open("t7.txt", 'r') as f:
    data = [r.strip() for r in f]


class Directory:

    def __init__(self, name, parent):
        self.__name = name
        self.__size = 0
        self.__subs = []
        self.__parent = parent
    
    def get_name(self):
            return self.__name
    
    def get_parent(self):
            return self.__parent

    def get_sub(self, sub_name):
            return next(s for s in self.get_subs() if s.get_name() == sub_name)

    def get_subs(self):
            return self.__subs

    def get_size(self):
        return self.__size

    def add_sub(self, sub):
        self.__subs.append(sub)

    def update_size(self, amount):
        self.__size += amount

    def calc_size(self):
        size = self.get_size()

        if not self.get_subs():
            return size
        for sub in self.get_subs():
            size += sub.calc_size()

        return size
        
    def __str__(self):
        return f"{self.__name}"



def part_one():

    dirs = []
    
    current = Directory(data[0].split(" ")[-1], "mutsis")
    dirs.append(current)

    for i in range(1, len(data)):
        row = data[i].split(" ")

        if row[-1] == "ls":
            continue

        elif row[1] == "cd":
            if row[-1] == "..":
                current = current.get_parent()
            else:
                current = current.get_sub(row[-1])
        elif row[0] == "dir":
            new = Directory(row[-1], current)
            current.add_sub(new)
            dirs.append(new)

        elif row[0].isnumeric():
            current.update_size(int(row[0]))

    for a in dirs:
        print(a, a.calc_size())

    return sum([a.calc_size() for a in dirs if a.calc_size() <= 100000])
    
    

def main():

    print(part_one())


if __name__ == "__main__":
    main()