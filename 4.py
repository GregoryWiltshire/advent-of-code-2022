import sys

file = sys.argv[1]

def _range(val):
    val1, val2 = val.split('-')
    return int(val2) - int(val1) + 1


# how many pairs overlap entirely?
# what is an overlap?
# considering the range
# i i+1 ... j-1 j
# if there is a total overlap the following must be true?
# i` >= i
# j` <= j
# this should work but will not work for ranges where the second range is the larger
# so we should try to reorder the ranges with rank = j-i
# if i1 >= i0 and j1 <= j0
def _overlaps_completely(pairs):
    i0, j0 = [int(x) for x in pairs[0].split('-')]
    i1, j1 = [int(x) for x in pairs[1].split('-')]
    return i1 >= i0 and j1 <= j0

# could be done with sets but why do that when you can use range!
def _overlaps(pairs):
    i0, j0 = [int(x) for x in pairs[0].split('-')]
    vals0 = range(i0,j0+1)
    i1, j1 = [int(x) for x in pairs[1].split('-')]
    vals1 = range(i1,j1+1)
    for i in vals1:
        if i in vals0:
            return True

with open(file, 'r') as f:
    lines = [
        sorted(l.split(','), key=_range, reverse=True) for l in f.read().split('\n') if l
    ]

def overlapping_completely_pairs(lines):
    return [
        pairs for pairs in lines if _overlaps_completely(pairs)
    ]

def overlapping_pairs(lines):
    return [
        pairs for pairs in lines if _overlaps(pairs)
    ]

print('part one:', len(overlapping_completely_pairs(lines)))
print('part two:', len(overlapping_pairs(lines)))


