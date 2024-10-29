with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

players = []

for line in s.split('\n'):
    players.append(int(line[-1]))


scores = [0,0]
rolls = 0
die = 1
currPlayer = 1


while scores[0] < 1000 and scores[1] < 1000:
    currPlayer = 1 - currPlayer
    for i in range(0,3):
        rolls += 1
        players[currPlayer] += die
        die += 1
        if die > 100:
            die = 1
        if players[currPlayer] > 10:
            players[currPlayer] %= 10
        if players[currPlayer] == 0:
            players[currPlayer] = 10
    scores[currPlayer] += players[currPlayer]

print(scores)

print(scores[0] * rolls)
print(scores[1] * rolls)