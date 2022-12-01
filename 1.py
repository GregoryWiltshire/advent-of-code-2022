# instantiate current max to invalid val
current_max = -1
max_idx = None
elf_idx = 1
accumulator = 0
# instantiate index 0 to invalid val
elves = [-1]

with open('1.txt','r') as f:
    while line := f.readline():
        stripped = line.strip()
        # set the elves[elf_idx] = accumulator, clear accumulator and incr elf_idx
        if not stripped:
            elves.append(accumulator)
            if accumulator > current_max or current_max is None:
                current_max = accumulator
                max_idx = elf_idx
            accumulator = 0
            elf_idx +=1
        else:
            accumulator += int(stripped)
print('elf', 'total_calories')
print(max_idx, current_max)

print('top', '3')

print(sum(list(reversed(sorted(elves)))[0:3]))

print()
