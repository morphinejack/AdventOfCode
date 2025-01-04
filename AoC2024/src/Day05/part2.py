def check_order(a, ref):
  while len(a) > 0:
    x = a.pop(len(a) - 1)  # remove last element

    # if any remaining values in a should come after x
    if len([y for y in a if y in ref[x]]) > 0:
      return False
  return True

# rearrange order of b according to rules in ref
def correct_order(b, ref, result):
  x = b[len(b) - 1]                  # last element
  y = [n for n in b if n in ref[x]]  # elements in b that should be after x

  if len(y) > 0:         # at least one element that should be after x isn't
    z = y[0]               # get element that should be after x
    b.remove(z)            # remove it from b
    b.append(z)            # append it to end of b, i.e. after x
  else:                  # x is in the correct position
    b.remove(x)            # remove x from b
    result.insert(0, x)    # add x to the corrected list

  # correct the order of what remains in b
  while len(b) > 0:
    correct_order(b, ref, result)

  return result

# read input_data from file
rules = []
pagesets = []
switch = False
with open("input.txt", "r") as file:
  for line in file.readlines():
    line = line.strip()
    if line == "":
      switch = True                     # line break in file
      continue
    if not switch:
      rules.append(line.split('|'))     # first section
    else:
      pagesets.append(line.split(','))  # second section

# create dictionary where k=page and v=list of pages that come after k
rule_tree = {}
for rule in rules:
  k, v = rule
  if k not in rule_tree.keys():
    rule_tree[k] = [v]
  else:
    rule_tree[k].append(v)
  if v not in rule_tree.keys():
    rule_tree[v] = []

total = 0
for pageset in pagesets:
  if not check_order(pageset[:], rule_tree):             # if order is incorrect
    pageset = correct_order(pageset[:], rule_tree, [])   # correct the order
    total += int(pageset[len(pageset) // 2])  # add middle page

print(total)