def main():
    part_1()
    part_2()

def is_increasing(numbers: list) -> bool:
    return all((x < y) for x, y in zip(numbers, numbers[1:]))

def is_decreasing(number:list) -> bool:
    return all(x > y for x, y in zip(number, number[1:]))

def check_rules(report:list) -> bool:
    curr_diff = report[1] - report[0]

    for idx in range(len(report) - 1):
        new_diff = report[idx + 1] - report[idx]
        if new_diff == 0 or abs(new_diff) > 3 or (new_diff > 0) != (curr_diff > 0):
            return False
        curr_diff = new_diff

    return True

def part_1():
    safe_reports = 0
    lines = get_input("input.txt")

    for item in lines:
        numbers = item.split(" ")
        numbers = [int(x) for x in numbers]
        if is_increasing(numbers) or is_decreasing(numbers):
            if (check_rules(numbers)):
                safe_reports += 1

    print(safe_reports)




def part_2():
    safe_reports_with_damp = 0
    lines = get_input("input.txt")

    for item in lines:
        numbers = item.split(" ")
        numbers = [int(x) for x in numbers]
        if check_rules(numbers):
            safe_reports_with_damp += 1
        else:
            for i in range(len(numbers)):
                if check_rules(numbers[:i] + numbers[i + 1 :]):
                    safe_reports_with_damp += 1
                    break

    print(safe_reports_with_damp)


def get_input(file_path: str) -> list() :
    lines = ()
    with open(file_path, 'r') as file:
        return file.read().splitlines()




if __name__ == '__main__':
    main()

