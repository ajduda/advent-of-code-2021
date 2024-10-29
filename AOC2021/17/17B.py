with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

s = s.split('..')
x1 = int(s[0].split('=')[1])
x2 = int(s[1].split(',')[0])
y1 = int(s[1].split('=')[1])
y2 = int(s[2])

ans = 0

for yInit in range(-500,500):
    for xInit in range(0,100):
        dy = yInit
        dx = xInit
        x = 0
        y = 0
        i = 0
        #print(f'dy = {dy}  dx={dx}')
        while True:
            #print(f'i = {i}  x={x}  y = {y}')
            x += dx
            y += dy
            dy -= 1
            if dx > 0:
                dx -= 1
            if dx < 0:
                dx += 1
            if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                ans += 1
                break
            #print(f'x:{x}  y:{y}  x1:{x1}  x2:{x2}  y1:{y1}  y2:{y2}')
            if x > x2 or y < y1:
                break

print(ans)