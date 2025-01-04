import sys


def get_input(path:str):
    with open(path) as f:
        return f.read()


def part1():
    line = get_input("input.txt")
    count = 0
    for p in line:
        if p == '(':
            count = count + 1
        elif p == ')':
            count = count -1
    print(count)

def part2():
    line = get_input("input.txt")
    count = 0
    for i,p in enumerate(line):
        if p == '(':
            count = count + 1
        elif p == ')':
            count = count - 1
        if count == -1:
            print(i+1)
    print(count)


if __name__ == "__main__":
    part1()
    part2()