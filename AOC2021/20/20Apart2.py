def findMaxes(grid):
    x1 = 10000000000000
    x2 = -10000000000000
    y1 = 10000000000000
    y2 = -10000000000000
    for (x,y) in grid:
        if x < x1:
            x1 = x
        if y < y1:
            y1 = y
        if x > x2:
            x2 = x
        if y > y2:
            y2 = y
    return (x1-20,x2+20,y1-20,y2+20)

def printGrid(grid):
    (x1,x2,y1,y2) = findMaxes(grid)
    for y in range(y1,y2):
        s = ''
        for x in range(x1,x2):
            if (x,y) in grid:
                s += '#'
            else:
                s += '.'
        print(s)

with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

# Sets seem easy, though this might slow down a bit

onOff = []

for c in s.split('\n\n')[0]:
    if c == '#':
        onOff.append(True)
    else:
        onOff.append(False)

grid = set()

y = 0
for line in s.split('\n\n')[1].split('\n'):
    x = 0
    for c in line:
        if c == '#':
            grid.add((x,y))
        x += 1
    y += 1

for i in range(0,2):
    print(f'starting iteration {i}')
    print(len(grid))
    printGrid(grid)
    print()
    bounds = findMaxes(grid)
    print(bounds)
    print()
    newGrid = set()
    (x1,x2,y1,y2) = bounds
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            index = 0
            if (x-1,y-1) in grid:
                index += 256
            if (x,y-1) in grid:
                index += 128
            if (x+1,y-1) in grid:
                index += 64
            if (x-1,y) in grid:
                index += 32
            if (x,y) in grid:
                index += 16
            if (x+1,y) in grid:
                index += 8
            if (x-1,y+1) in grid:
                index += 4
            if (x,y+1) in grid:
                index += 2
            if (x+1,y+1) in grid:
                index += 1
            if onOff[index]:
                newGrid.add((x,y))
    grid = newGrid

printGrid(grid)
print(len(grid))

