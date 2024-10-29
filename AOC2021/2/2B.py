x = 0
y = 0
aim = 0

with open('input.txt') as inp:
    for line in inp:
        d, n = line.split(' ')
        n = int(n)
        if d == 'forward':
            x += n
            y += n * aim
        elif d == 'down':
            aim += n
        else:
            aim -= n

print (x*y)