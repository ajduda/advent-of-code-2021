lines = []
pointsAtVal = {}
with open('input.txt') as inp:
    for line in inp:
        l,r = line.split(' -> ')
        x1, y1 = l.split(',')
        x2, y2 = r.split(',')
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        lines.append(((x1,y1),(x2,y2)))

#print(lines)

for line in lines:
    #print(f'line: {line}')
    if line[0][0] == line[1][0]:  # vertical
        x = line[0][0]
        if line[0][1] < line[1][1]:
            step = 1
        else:
            step = -1
        for y in range(line[0][1], line[1][1] + step, step):
            #print(f'x: {x}  y: {y}')
            if (x, y) not in pointsAtVal:
                pointsAtVal[(x,y)] = 1
            else:
                pointsAtVal[(x,y)] += 1
    elif line[0][1] == line[1][1]:  # Horizontal
        y = line[0][1]
        if line[0][0] < line[1][0]:
            step = 1
        else:
            step = -1
        for x in range(line[0][0], line[1][0] + step, step):
            if (x, y) not in pointsAtVal:
                pointsAtVal[(x,y)] = 1
            else:
                pointsAtVal[(x,y)] += 1
    else:  # Diagonal
        x1, y1 = line[0]
        x2, y2 = line[1]
        if x1 < x2:
            xstep = 1
        else:
            xstep = -1
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        steps = x1 - x2
        if steps < 0:
            steps *= -1
        steps += 1
        x = x1
        y = y1
        for i in range(0, steps):
            if (x, y) not in pointsAtVal: 
                pointsAtVal[(x,y)] = 1
            else:
                pointsAtVal[(x,y)] += 1
            x += xstep
            y += ystep       

ans = 0
for k in pointsAtVal.keys():
    if pointsAtVal[k] > 1:
        ans += 1

print(ans)