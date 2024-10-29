l = []
with open('input') as inp:
    for line in inp:
        l.append(int(line))
#print(l)

ans = 0
x = 0
cumsum = [l[0],l[1],l[2]]
prev = sum(cumsum)

for i in range(3, len(l)):
    cumsum[x%3] = l[i]
    x += 1
    if sum(cumsum) > prev:
        ans += 1
    prev = sum(cumsum)

print(ans)