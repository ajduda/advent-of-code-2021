def fold(dots, inst):
    ret = set()
    n = int(inst[2:])
    if inst[0] == 'y':
        for dot in dots:
            if dot[1] < n:
                ret.add(dot)
            else:
                ret.add((dot[0],2*n - dot[1]))
    else:
        for dot in dots:
            if dot[0] < n:
                ret.add(dot)
            else:
                ret.add((2*n - dot[0],dot[1]))
    return ret

with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

top, bottom = s.split('\n\n')
dots = set()
instr = []

for line in top.split('\n'):
    x,y = line.split(',')
    x = int(x)
    y = int(y)
    dots.add((x,y))

for line in bottom.split('\n'):
    word = line.split(' ')[2]
    dots = fold(dots, word)

maxX = -1
maxY = -1

for dot in dots:
    if dot[0] > maxX:
        maxX = dot[0]
    if dot[1] > maxY:
        maxY = dot[1]

for y in range(0,maxY+1):
    s = ''
    for x in range(0,maxX + 1):
        if (x,y) in dots:
            s += '#'
        else:
            s += ' '
    print(s)

