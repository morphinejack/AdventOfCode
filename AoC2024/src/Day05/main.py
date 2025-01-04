def main():
    bad_updates=part_1()
    part_2(bad_updates)



def part_1() -> list:
    rules, updates = get_input("input.txt")
    ordering = list()
    for rule in rules:
        ordering.append(tuple(rule.split("|")))

    good_updates = list()
    bad_updates = list()
    for update in updates:
        add_it = True
        for order in ordering:
            try:
                minIndex = update.index(order[0])
                maxIndex = update.index(order[1])
            except ValueError:
                continue
            if maxIndex < minIndex:
                add_it = False
                break
        if add_it == True:
            good_updates.append(update)
        else:
            bad_updates.append(update)
    numeric_updates = list()
    for gu in good_updates:
        numeric_updates.append(tuple(map(int, gu.split(','))))
    sum = 0
    for nu in numeric_updates:
        index = int(len(nu)/2)
        sum = sum + nu[index]

    print(sum)
    print(bad_updates)
    return bad_updates

def part_2(bad_updates):
    rules, updates = get_input("input.txt")
    ordering = list()
    for rule in rules:
        ordering.append(tuple(map(int, rule.split('|'))))
    numeric_updates = list()
    for bu in bad_updates:
        numeric_updates.append(tuple(map(int, bu.split(','))))

    print(numeric_updates)
    for index,update in enumerate(numeric_updates):
        for order in ordering:
            try:
                minIndex = update.index(order[0])
                maxIndex = update.index(order[1])
            except ValueError:
                continue
            if (maxIndex < minIndex):
                tuple_to_update = list(numeric_updates[index])
                element = tuple_to_update[maxIndex]
                tuple_to_update[maxIndex] = tuple_to_update[minIndex]
                tuple_to_update[minIndex] = element
                del numeric_updates[index]
                numeric_updates.insert(index,tuple(tuple_to_update))

    sum = 0
    for nu in numeric_updates:
        index = int(len(nu) / 2)
        sum = sum + nu[index]

    print(sum)



def get_input(path:str) -> (list,list):
    rules = list()
    updates = list()
    with open(path) as f:
        for line in f:
            if line.strip() == "":
                for line_2 in f:
                    updates.append(line_2.strip())
            else:
                rules.append(line.strip())

    return (rules, updates)

if __name__ == "__main__":
    main()