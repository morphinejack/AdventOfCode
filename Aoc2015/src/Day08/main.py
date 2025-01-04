sum_of_escaped_characters = 0
with open("input.txt", "r") as file:
    for line in file:
        char_count = len(line) - 2
        sum_of_escaped_characters += char_count

sum_of_chars = 0
with open("input.txt", "r",encoding='unicode_escape') as file:
    for line in file:
        # Get the number of characters in the line
        char_count = len(line)-2
        sum_of_chars += char_count

print(sum_of_escaped_characters - sum_of_chars)