def main():
    part_1()
    part_2()


def get_boundaries(instruction: str):
    boundaries = instruction.strip().split(" through ")

    first_limit = boundaries[0].split(",")
    second_limit = boundaries[1].split(",")

    x1 = int(first_limit[0])
    y1 = int(first_limit[1])
    x2 = int(second_limit[0])
    y2 = int(second_limit[1])

    return x1,y1,x2,y2

def part_1():
    rows = 1000
    cols = 1000
    lights = [[0 for _ in range(cols)] for _ in range(rows)]

    instructions_set = get_input("input.txt")
    for instruction in instructions_set:
        i = instruction.find("toggle")
        if (i >= 0): #toggle
            instruction = instruction[(i+6):]
            x1,y1,x2,y2 = get_boundaries(instruction)
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] ^= 1

            continue
        i = instruction.find("turn off")
        if (i >= 0): #turn off
            instruction = instruction[(i+8):]
            x1,y1,x2,y2 = get_boundaries(instruction)
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = 0

            continue
        i = instruction.find("turn on")
        if (i >= 0):
            instruction = instruction[(i+8):]
            x1, y1, x2, y2 = get_boundaries(instruction)
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = 1

            continue

    sum = 0
    for i in range(rows):
        for j in range(cols):
            if lights[i][j] == 1:
                sum = sum + 1

    print(sum)


def part_2():
    rows = 1000
    cols = 1000
    lights = [[0 for _ in range(cols)] for _ in range(rows)]

    instructions_set = get_input("input.txt")
    for instruction in instructions_set:
        i = instruction.find("toggle")
        if (i >= 0):  # toggle
            instruction = instruction[(i + 6):]
            x1, y1, x2, y2 = get_boundaries(instruction)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] = lights[x][y] + 2

            continue
        i = instruction.find("turn off")
        if (i >= 0):  # turn off
            instruction = instruction[(i + 8):]
            x1, y1, x2, y2 = get_boundaries(instruction)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if lights[x][y] > 0 : lights[x][y] = lights[x][y] - 1

            continue
        i = instruction.find("turn on")
        if (i >= 0):
            instruction = instruction[(i + 8):]
            x1, y1, x2, y2 = get_boundaries(instruction)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] = lights[x][y] + 1

            continue

    sum = 0
    for i in range(rows):
        for j in range(cols):
                sum = sum + lights[i][j]

    print(sum)


def get_input(path:str) -> list():
    with open(path, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()