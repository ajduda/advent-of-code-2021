def wins(board, calledSoFar):
    # row checks
    for y in board:
        win = True
        for x in y:
            if x not in calledSoFar:
                win = False
        if win:
            print('Row Win Found')
            return True

    #column checks:
    for x in range(0,5):
        win = True
        for y in range(0,5):
            if board[y][x] not in calledSoFar:
                win = False
        if win:
            print('Column Win Found')
            return True
    return False
    #diag checks LMAO NO DIAG CHECKS
    """win = True
    for x in range(0, 5):
        if board[x][x] not in calledSoFar:
            win = False
    if win:
        print('DiagA Win Found')
        return True

    win = True
    for x in range(0, 5):
        if board[x][4-x] not in calledSoFar:
            win = False
    if win:
        print('DiagB Win Found')
    return win #last check"""

with open('input.txt') as inp:
    s = inp.read()

boards = s.split('\n\n')
calledTemp = boards[0]
boardsTemp = boards[1:]

called = []
for n in calledTemp.split(','):
    called.append(int(n))

boards = []
i = 0
for b in boardsTemp:
    #print('DEBUG 1')
    #print(b)
    boards.append([])
    y = 0
    for line in boardsTemp[i].split('\n'):
        #print('DEBUG 2')
        #print(line)
        if len(line) == 0:
            continue
        boards[i].append([])
        x = 0
        for n in line.split(' '):
            if len(n) == 0:
                continue
            #print('DEBUG 3')
            #print(n)
            boards[i][y].append(int(n))
            x += 1
        y += 1
    i += 1

calledSoFar = []
numCalled = 0

winnerFound = False

print(len(boards))
print('ABOVE VALUE LMAO')

while len(boards) > 0:
    calledSoFar.append(called[numCalled])
    numCalled += 1
    boardsToRemove = []
    for board in boards:
        if wins(board, calledSoFar):
            boardsToRemove.append(board)
    for board in boardsToRemove:
        boards.remove(board)
        lastBoard = board


print(lastBoard)
print(calledSoFar)

lastCalled = calledSoFar[-1]
total = 0
for line in lastBoard:
    for val in line:
        if val not in calledSoFar:
            total += val

print(total)
print(lastCalled)


print(total*lastCalled)