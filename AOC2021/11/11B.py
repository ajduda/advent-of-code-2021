with open('input.txt') as inp:
    s = inp.read()

grid = []
for line in s.split('\n'):
    grid.append([-10000000000])
    for c in line:
        grid[-1].append(int(c))
    grid[-1].append(-10000000000)

grid.insert(0,[])
grid.append([])
for i in range(0, len(grid[1])):
    grid[0].append(-10000000000)
    grid[-1].append(-10000000000)

i = 0
while True:
    #print(f'Step {i} starting')
    flashed = set()

    for y in range(1,len(grid)-1):
        for x in range(1,len(grid[0])-1):
            grid[y][x] += 1

    again = True
    while again:
        again = False
        for y in range(1,len(grid)-1):
            for x in range(1,len(grid[0])-1):
                if (x,y) not in flashed and grid[y][x] >= 10:
                    flashed.add((x,y))
                    again = True
                    for v in range(-1,2):
                        for w in range(-1,2):
                            grid[y+w][x+v] += 1

    allOn = True
    for y in range(1,len(grid)-1):
        for x in range(1,len(grid[0])-1):
            if grid[y][x] > 9:
                grid[y][x] = 0
            else:
                allOn = False

    i += 1
    if allOn:
        print(i)
        exit()

    #print(f'grid after step {i+1}')
    #print(grid)


