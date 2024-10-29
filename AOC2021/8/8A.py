ans = 0

with open('input.txt') as inp:
    for line in inp:
        lineR = line.split(' | ')[1]
        for s in lineR.strip('\n').split(' '):
            l = len(s)
            if l == 2 or l == 4 or l == 7 or l == 3:
                ans += 1
                #print(s)

print(ans)