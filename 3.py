import sys

file = sys.argv[1]
with open(file, 'r') as f:
    sacks = f.read().splitlines()

# a-z 1-26
#A-Z 27-52
def priority(s: str) -> int:
    if s.isupper():
        return (ord(s) - ord('A')) %26 + 1 + 26
    if s.islower():
        return (ord(s) - ord('a')) %26 + 1

# first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.
def compartments(sack):
    n = len(sack)//2
    return sack[:n], sack[n:]

def part_one():
    accumulator = 0
    for sack in sacks:
        comp_1, comp_2 = compartments(sack)
        # find the sum of the priorites
        # of items that appear in each sack compartment

        # elves failed to follow this rule for exactly one item type per rucksack
        # so there is only one duplicate in each rucksack
        misplaced_item = set(comp_1).intersection(set(comp_2)).pop()
        accumulator += priority(misplaced_item)
    return accumulator

print('Part One:')
print(part_one())

def part_two():
    accumulator = 0
    grouped_sacks =  [sacks[i*3:i*3 +3] for i in range(0, len(sacks)//3)]
    for sack_group in grouped_sacks:
        badge = set.intersection(*[set(s) for s in sack_group]).pop()
        accumulator += priority(badge)
    return accumulator

print('Part Two:')
print(part_two())
