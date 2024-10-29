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
        if x1 == x2 or y1 == y2:
            lines.append(((x1,y1),(x2,y2)))

#print(lines)

for line in lines:
    #print(f'line: {line}')
    if line[0][0] == line[1][0]:
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
    else:
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

ans = 0
for k in pointsAtVal.keys():
    if pointsAtVal[k] > 1:
        ans += 1

print(ans)

"""for y in range(0,10):
    s = ''
    for x in range(0,10):
        if (x,y) in pointsAtVal:
            s += str(pointsAtVal[(x,y)])
        else:
            s += '.'
    print(s)"""