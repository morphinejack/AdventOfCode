from typing import List

def main():
    part_1()
    part_2()

def part_1():
    matrix: List[List[str]] = []
    words = ["XMAS", "SAMX"]

    with open("input.txt", "r") as file:
        for line in file:
            matrix.append([s for s in line.strip()])

    wordCount = 0
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            wordCount += sum(1 for find in [
                check(words, matrix, x, y, 1, 0, 0),
                check(words, matrix, x, y, 1, 1, 0),
                check(words, matrix, x, y, 0, 1, 0),
                check(words, matrix, x, y, -1, 1, 0)
            ] if find)

    print(wordCount)

# words: search words
# matrix: letter matrix
# x: starting x
# y: starting y
# dX: x axis movement
# dY: y axis movement
# index: checked index in the word
def check(words: List[str], matrix: List[List[str]], x: int, y: int, dX: int, dY: int, index: int) -> bool:
    if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[y]):
        return False

    validWords = [word for word in words if word[index] == matrix[y][x]]
    if len(validWords) > 0:
        if index == max((len(word) for word in validWords)) - 1:
            #mask[y][x] = True
            return True
        else:
            return check(validWords, matrix, x + dX, y + dY, dX, dY, index + 1)
    else:
        return False

def part_2():
    matrix: List[List[str]] = []

    with open("input.txt", "r") as file:
        for line in file:
            matrix.append([s for s in line.strip()])

    letters = set(["M", "S"])
    XmasCount = 0

    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[y]) - 1):
            if matrix[y][x] == "A":
                set1 = set([matrix[y - 1][x - 1], matrix[y + 1][x + 1]])
                set2 = set([matrix[y - 1][x + 1], matrix[y + 1][x - 1]])

                if set1 == set2 == letters:
                    XmasCount += 1

    print(XmasCount)


if __name__ == "__main__":
    main()

