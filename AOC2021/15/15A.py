with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

grid = []

for line in s.split('\n'):
    grid.append([])
    for c in line:
        grid[-1].append(int(c))

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