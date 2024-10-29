seenPositions = {}
weights = {}

TARGET = 21

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            n = i+j+k
            if n in weights:
                weights[n] += 1
            else:
                weights[n] = 1

def simulate(p1Pos, p2Pos, p1Score, p2Score, isP1Turn):  # returns number of wins
    if isP1Turn:
        ret = [0,0]
        for k in weights.keys():
            newPos = p1Pos + k
            newPos %= 10
            if newPos == 0:
                newPos = 10
            newScore = p1Score + newPos
            if newScore >= TARGET:
                ret[0] += weights[k]
            else:
                r = simulate(newPos, p2Pos, newScore, p2Score, False)
                ret[0] += r[0] * weights[k]
                ret[1] += r[1] * weights[k]
        return ret
    else:
        ret = [0,0]
        for k in weights.keys():
            newPos = p2Pos + k
            newPos %= 10
            if newPos == 0:
                newPos = 10
            newScore = p2Score + newPos
            if newScore >= TARGET:
                ret[1] += weights[k]
            else:
                r = simulate(p1Pos, newPos, p1Score, newScore, True)
                ret[0] += r[0] * weights[k]
                ret[1] += r[1] * weights[k]
        return ret






with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

players = []

for line in s.split('\n'):
    players.append(int(line[-1]))


weights = {}
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            n = i+j+k
            if n in weights:
                weights[n] += 1
            else:
                weights[n] = 1

ans = simulate(players[0],players[1],0,0,True)

print(max(ans))