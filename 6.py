import sys

file = sys.argv[1]
with open(file, 'r') as f:
    text = f.readline()


# detect 4 chars, all different - start of packet
def find_marker_nunique(text, n) -> int:
    chars = {}
    start_ptr = end_ptr = 0
    while end_ptr - start_ptr < n:
        current_char = text[end_ptr]
        if current_char in chars:
            # move pointer i to the first char after the dupe
            # do not make faulty assumption that your pointer will
            # not be pushed back by a earlier dupe!
            if chars[current_char] + 1 > start_ptr:
                start_ptr = chars[current_char] + 1
            # change index of duped char to latest spotted
            chars[current_char] = end_ptr
        else:
            # note the index of the unique char
            chars[current_char] = end_ptr
        end_ptr += 1
    return end_ptr


# bvwbjplbgvbhsrlpgdmjqwftvncz
# bvwbj plbgvbhsrlpgdmjqwf tvncz
def part_two(text) -> int:
    begin = find_marker_nunique(text, 4)
    return find_marker_nunique(text[begin:-1], 14) + begin


print('start-of-packet marker found after char #:', find_marker_nunique(text, 4))
print('start-of-message marker after char #:', part_two(text))
