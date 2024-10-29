x = 0
y = 0

with open('input.txt') as inp:
    for line in inp:
        d, n = line.split(' ')
        n = int(n)
        if d == 'forward':
            x += n
        elif d == 'down':
            y += n
        else:
            y -= n

print (x*y)