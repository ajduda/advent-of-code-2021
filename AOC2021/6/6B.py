with open('input.txt') as inp:
    s = inp.read()

fish = {}  # fish[x] = y means that there are y fish that have x days until a new fish is born
for n in s.split(','):
    m = int(n)
    if m not in fish:
        fish[m] = 1
    else:
        fish[m] += 1
print(fish)

for i in range(0, 256):
    newfish = {}
    for x in range(0,9):
        newfish[x] = 0
    for f in fish.keys():
        n = fish[f]
        if f == 0:
            newfish[8] += n
            newfish[6] += n
        else:
            newfish[f-1] += n
    fish = newfish
    #print(f'after {i+1} days: {fish}')

ans = 0

for k in fish:
    ans += fish[k]

print(ans)