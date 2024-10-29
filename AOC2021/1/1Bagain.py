l = []
with open('input') as inp:
    for line in inp:
        l.append(int(line))
#print(l)

ans = 0

for i in range(4, len(l)):
    if l[i] > l[i-4]:
        ans += 1

print(ans)