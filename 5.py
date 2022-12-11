import sys

file = sys.argv[1]
with open(file, 'r') as f:
    lines = f.read().split('\n')


def parse_line(line):
    # [start:stop:step]
    # '[N] [C]    '
    s = line[1::2]
    # 'N C  '
    return list(s[::2])
    # 'NC '


# returns index of first moveset
def populate(stack, lines) -> int:
    i = 0
    for line in lines:
        # terminating condition to find the line with the stack #s
        parsed = parse_line(line)
        if parsed == [str(i) for i in range(1, len(parsed)+1)]:
            return i + 2
        for i, item in enumerate(parsed):
            # no
            if item != ' ':
                stack[i].append(item)


def mv(stk, n, frm, to, CM9001=False):
    if CM9001:
        s = [stk[frm-1].pop() for _ in range(n)]
        for e in s[::-1]:
            stk[to-1].append(e)
    else:
        for _ in range(n):
            stk[to-1].append(stk[frm-1].pop())


def parse_move(move):
    return [int(m) for m in move.split(' ')[1::2]]


stack = [[] for _ in range(len(parse_line(lines[0])))]
moves_idx = populate(stack, lines)
# reverse the lists so LIFO
stk1 = [c[::-1] for c in stack]
stk2 = [c[::-1] for c in stack]

moves = lines[moves_idx:-1]
for move in moves:
    if move:
        n, frm, to = parse_move(move)
        mv(stk1, n, frm, to)
        mv(stk2, n, frm, to, CM9001=True)


print('part one:', ''.join([c.pop() for c in stk1]))

print('part two:', ''.join([c.pop() for c in stk2 if c]))
