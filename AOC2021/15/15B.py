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

"""
for line in grid:
    s = ''
    for c in line:
        s += str(c)
    print(s)
"""
print(len(grid))
print(len(grid[0]))

for y in range(0,len(grid)):
    for x in range(0,len(grid[0])):
        if x == 0 and y == 0:
            continue
        elif x == 0:
            grid[y][x] += grid[y-1][x]
        elif y == 0:
            grid[y][x] += grid[y][x-1]
        else:
            grid[y][x] += min(grid[y-1][x],grid[y][x-1])

print(grid[-1][-1] - grid[0][0])
