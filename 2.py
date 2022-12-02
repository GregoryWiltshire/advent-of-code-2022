A = X = 1 # rock
B = Y = 2 # paper
C = Z = 3 # scissors

BEATS_MAP = {
    2: 1, # paper beats rock
    3: 2, # scissors beats paper
    1: 3, # rock beats scissors
}

import sys 
filename = sys.argv[1]
with open(filename,'r') as f:
    lines = f.read().split('\n')

def scoreA(lines):
    your_score = 0
    opp_score = 0
    for line in lines:
        if line:
            opp_move, your_move = [globals()[val] for val in line.split(' ')]
            your_score += your_move
            opp_score += opp_move
            if BEATS_MAP[your_move] == opp_move:
                your_score += 6
            elif your_move == opp_move:
                your_score += 3
                opp_score += 3
            else:
                opp_score += 6
    print('your final score:', your_score)
    print('opponent final score:', opp_score)


def __determine_move(opp_move, desired_outcome):
    # 2 draw
    if desired_outcome == 2:
        return opp_move
    # 1 lose
    if desired_outcome == 1:
        return BEATS_MAP[opp_move]
    # 3 win
    else:
        return (set(BEATS_MAP.keys()) - set([opp_move, BEATS_MAP[opp_move]])).pop()


def scoreB(lines):
    your_score = 0
    opp_score = 0
    for line in lines:
        if line:
            opp_move, desired_outcome = [globals()[val] for val in line.split(' ')]
            your_move = __determine_move(opp_move, desired_outcome)
            your_score += your_move
            opp_score += opp_move
            if BEATS_MAP[your_move] == opp_move:
                your_score += 6
            elif your_move == opp_move:
                your_score += 3
                opp_score += 3
            else:
                opp_score += 6
    print('your final score:', your_score)
    print('opponent final score:', opp_score)

print('part one:')
scoreA(lines)

print('part two:')
scoreB(lines)
