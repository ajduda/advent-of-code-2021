with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]


onOff = []

for c in s.split('\n\n')[0]:
    if c == '#':
        onOff.append(True)
    else:
        onOff.append(False)

temp = []

for line in s.split('\n\n')[1].split('\n'):
    temp.append([])
    for c in line:
        temp[-1].append(c == '#')

grid = []
for y in range(0,600):
    grid.append([])
    for x in range(0,600):  # giga padding, only needing 360000 elements!
        grid[-1].append(False)


for y in range(250, 250+len(temp)):
    for x in range(250,250+len(temp[y-250])):
        grid[y][x] = temp[y-250][x-250]

for i in range(0,50):
    print(f'starting iteration {i}')
    newGrid = [[]]
    for x in range(0, len(grid[0])):
        newGrid[-1].append(i%2==0 and onOff[0]) # bounds stuff
    for y in range(1, len(grid)-1):
        newGrid.append([])
        newGrid[-1].append(i%2==0 and onOff[0]) # bounds stuff
        for x in range(1, len(grid[y])-1):
            index = 0
            if grid[y-1][x-1]:
                index += 256
            if grid[y-1][x]:
                index += 128
            if grid[y-1][x+1]:
                index += 64
            if grid[y][x-1]:
                index += 32
            if grid[y][x]:
                index += 16
            if grid[y][x+1]:
                index += 8
            if grid[y+1][x-1]:
                index += 4
            if grid[y+1][x]:
                index += 2
            if grid[y+1][x+1]:
                index += 1
            newGrid[-1].append(onOff[index])
        newGrid[-1].append(i%2==0 and onOff[0]) # bounds stuff

    newGrid.append([])
    for x in range(0, len(grid[0])):
        newGrid[-1].append(i%2==0 and onOff[0]) #bounds stuff
    grid = newGrid

ans = 0
for y in range(0,len(grid)):
    for x in range(0,len(grid[y])):
        if grid[y][x]:
            ans += 1
print(ans)