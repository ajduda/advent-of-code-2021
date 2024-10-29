with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

s = s.split('..')
x1 = int(s[0].split('=')[1])
x2 = int(s[1].split(',')[0])
y1 = int(s[1].split('=')[1])
y2 = int(s[2])

print(x1)
print(x2)
print(y1)
print(y2)

bestY=0
currY = 0
foundY = True
keepChecking = 0
while foundY or keepChecking < 50:
    foundY = False
    y = 0
    dy = currY + 1
    currY += 1
    print(f'trying dy={dy}')
    while y >= y1:
        #print(f'y = {y}  y1={y1}  y2={y2}')
        y += dy
        dy -= 1
        if y <= y2 and y >= y1:
            print(f'bestY = {currY}')
            foundY = True
            bestY = currY
            break
    if not foundY:
        keepChecking += 1

print(bestY)
print((bestY*(bestY+1))//2)