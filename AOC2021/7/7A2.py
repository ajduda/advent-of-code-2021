with open('test.txt') as inp:
    s = inp.read()

numbers = []
for n in s.split(','):
    if len(n) > 0:
        numbers.append(int(n))

freq = {}
for n in numbers:
    if n not in freq:
        freq[n] = 1
    else:
        freq[n] += 1

n = 0
bestN = -1
for k in freq.keys():
    if freq[k] > n:
        n = freq[k]
        bestN = k

print(bestN)
print(n)