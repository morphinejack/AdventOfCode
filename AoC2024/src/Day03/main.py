import re
def main():
    part_1()
    part_2()


def find_multiply_pairs(line:str) -> int:
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, line)
    matches = [(int(x), int(y)) for x, y in matches]

    prod = 0
    for match in matches:
        res = match[0] * match[1]
        prod = prod + res

    return prod

def part_1():
    inp = get_input("input.txt")
    prod = find_multiply_pairs(inp)

    print(prod)


def part_2():
    inp = get_input("input.txt")
    lines = inp.split("don't()")
    mul_result = 0
    mul_result = find_multiply_pairs(lines[0])

    for n in range(1, len(lines)):
        i = lines[n].find("do()")
        do_string = lines[n][i:]

        mul_result = mul_result + find_multiply_pairs(do_string)

    print(mul_result)


def get_input(path:str) -> str:
    with open(path, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()