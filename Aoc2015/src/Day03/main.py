def main():
    part_1()
    part_2()

def part_1():
    directions = get_input("input.txt")

    visited = set()  # keep track of visited houses
    x, y = 0, 0  # starting location

    visited.add((x, y))  # deliver first present

    for d in directions:
        if d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        elif d == '>':
            x += 1
        elif d == '<':
            x -= 1

        visited.add((x, y))  # deliver present at new location

    print(len(visited))  # count the unique houses visited

def part_2():
    directions = get_input("input.txt")

    visited = set()
    sx, sy = 0, 0
    rx, ry = 0, 0
    visited.add((sx, sy))
    visited.add((rx, ry))

    token = 0
    for d in directions:
        if (token == 0):
            token = 1
            if d == '^':
                sy += 1
            elif d == 'v':
                sy -= 1
            elif d == '>':
                sx += 1
            elif d == '<':
                sx -= 1
            visited.add((sx, sy))
        else:
            token = 0
            if d == '^':
                ry += 1
            elif d == 'v':
                ry -= 1
            elif d == '>':
                rx += 1
            elif d == '<':
                rx -= 1
            visited.add((rx, ry))

    print(len(visited))




def get_input(file_path:str) -> str:

    with open(file_path, 'r') as f:
        return f.read()


if __name__ == "__main__":
    main()