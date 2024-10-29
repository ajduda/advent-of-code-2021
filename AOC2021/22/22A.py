with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

on = set()

for line in s.split('\n'):
    l,r = line.split(' ')
    x,y,z = r.split(',')
    x = x[2:]
    y = y[2:]
    z = z[2:]
    x1,x2 = x.split('..')
    y1,y2 = y.split('..')
    z1,z2 = z.split('..')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    z1 = int(z1)
    z2 = int(z2)
    if x1 < -50 or x1 > 50 or y1 < -50 or y2 > 50 or z1 < -50 or z2 > 50:
        continue
    if l == 'on':
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    on.add((x,y,z))
    elif l == 'off':
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    if (x,y,z) in on:
                        on.remove((x,y,z))
    else:
        print('error')
        exit()

print(len(on))