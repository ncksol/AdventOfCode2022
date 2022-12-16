
def calcP1Score(p1, p2):
    if p1 == "A":
        if p2 == "X":
            return 1+3
        elif p2 == "Y":
            return 2+6
        elif p2 == "Z":
            return 3+0
    elif p1 == "B":
        if p2 == "X":
            return 1+0
        elif p2 == "Y":
            return 2+3
        elif p2 == "Z":
            return 3+6
    elif p1 == "C":
        if p2 == "X":
            return 1+6
        elif p2 == "Y":
            return 2+0
        elif p2 == "Z":
            return 3+3
    return 0

def puzzle1(lines):
    score = 0
    for line in lines:
        p = line.strip().split(' ')
        p1 = p[0]
        p2 = p[1]
        score += calcP1Score(p1, p2)
    return score

def calcP2Score(p1, p2):
    if p1 == "A":
        if p2 == "X":
            return 3+0
        elif p2 == "Y":
            return 1+3
        elif p2 == "Z":
            return 2+6
    elif p1 == "B":
        if p2 == "X":
            return 1+0
        elif p2 == "Y":
            return 2+3
        elif p2 == "Z":
            return 3+6
    elif p1 == "C":
        if p2 == "X":
            return 2+0
        elif p2 == "Y":
            return 3+3
        elif p2 == "Z":
            return 1+6
    return 0

def puzzle2(lines):
    score = 0
    for line in lines:
        p = line.strip().split(' ')
        p1 = p[0]
        p2 = p[1]
        score += calcP2Score(p1, p2)
    return score

import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)

with open(os.getcwd() + '/02/input.txt') as f:
  lines = f.readlines()

pu1 = puzzle1(lines)
pu2 = puzzle2(lines)

print(pu1)
print(pu2)