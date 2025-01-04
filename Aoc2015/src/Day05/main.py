import re

def main():
  part_1()
  part_2()

def part_1():
    strings = get_input("input.txt")
    forbidden = ('ab','cd','pq','xy')
    nice_count = 0
    for s in strings:
        # Check for repeated letters
        if not re.search(r'(\w)\1', s):
              continue
             # Check for disallowed substrings
        if re.search(r'ab|cd|pq|xy', s):
              continue
              # Count vowels
        vowels = re.findall(r'[aeiou]', s)
        if len(vowels) < 3:
          continue
            # If all conditions are satisfied, increment nice count
        nice_count += 1

    print(nice_count)

def part_2():
    nice_count = 0
    strings = get_input("input.txt")
    for s in strings:
        # Check for pair of repeated letters
        if not re.search(r'(\w\w).*\1', s):
            continue
            # Check for letter that repeats with one between
        if not re.search(r'(\w).\1', s):
            continue
            # If both conditions are satisfied, increment nice count
        nice_count += 1

    print(nice_count)

def get_input(path:str) -> list:
    strings = list()
    with open(path) as f:
        strings = f.read().splitlines()

    return strings



if __name__ == '__main__':
    main()