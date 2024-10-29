with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

grid = []

for line in s.split('\n'):
    grid.append([])
    for c in line:
        grid[-1].append(int(c))


# Copy the grid, ensuring it's a soft copy of soft copies
OG = []
for y in range(0,len(grid)):
    OG.append([])
    for x in range(0,len(grid[y])):
        OG[-1].append(grid[y][x])

#Extend in the x direction
for i in range(1,5):
    for y in range(0, len(OG)):
        for x in range(0, len(OG[0])):
            n = OG[y][x] + i
            while n > 9:
                n -= 9
            grid[y].append(n)

"""
for line in grid:
    s = ''
    for c in line:
        s += str(c)
    print(s)
"""

# Copy the grid, ensuring it's a soft copy of soft copies
OG = []
for y in range(0,len(grid)):
    OG.append([])
    for x in range(0,len(grid[y])):
        OG[-1].append(grid[y][x])

#Extend in the y direction
for i in range(1,5):
    for y in range(0, len(OG)):
        grid.append([])
        for x in range(0, len(OG[0])):
            n = OG[y][x] + i
            while n > 9:
                n -= 9
            grid[-1].append(n)

visited = set()

PQ = []
PQ.append((0,(0,0)))
while len(PQ) > 0:
    PQ.sort()
    (cost,coord) = PQ.pop(0)
    (x,y) = coord

    if (x,y) in visited:
        continue

    print(f'looking at ({x},{y}) which has cost {cost}')

    if x == len(grid[0]) - 1 and y == len(grid) - 1:
        print(cost)
        exit()

    visited.add((x,y))

    if x != 0 and (x-1,y) not in visited:
        PQ.append((grid[y][x-1] + cost,(x-1,y)))
    if y != 0 and (x,y-1) not in visited:
        PQ.append((grid[y-1][x] + cost,(x,y-1)))
    if x != len(grid)-1 and (x+1,y) not in visited:
        PQ.append((grid[y][x+1] + cost,(x+1,y)))
    if y != len(grid[0])-1 and (x,y+1) not in visited:
        PQ.append((grid[y+1][x] + cost,(x,y+1)))

