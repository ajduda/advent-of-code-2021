def tri(n):
    return n*(n+1)//2

with open('input.txt') as inp:
    s = inp.read()

numbers = []
for n in s.split(','):
    if len(n) > 0:
        numbers.append(int(n))

a = min(numbers)
b = max(numbers)

best = 999999999
pos = -1
for i in range(a, b+1):
    val = 0
    for n in numbers:
        if n > i:
            val += tri(n - i)
        else:
            val += tri(i - n)

    if val < best:
        best = val
        pos = i

print(pos)
print(best)