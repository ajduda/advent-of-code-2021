with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

top,bottom = s.split('\n\n')

rules = {}
pairs = {}


for line in bottom.split('\n'):
    l,r = line.split(' -> ')
    rules[l] = r

for i in range(0, len(top) - 1):
    pair = top[i:i+2]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1

#print(pairs)

for i in range(0, 40):
    print(f'Starting pass {i}')
    index = 0
    nextPairs = {}
    for pair in pairs.keys():
        amt = pairs[pair]
        #print(pair)
        newPairA = pair[0] + rules[pair]
        newPairB = rules[pair] + pair[1]
        if newPairA in nextPairs:
            nextPairs[newPairA] += amt
        else:
            nextPairs[newPairA] = amt
        if newPairB in nextPairs:
            nextPairs[newPairB] += amt
        else:
            nextPairs[newPairB] = amt
    pairs = nextPairs
    print(pairs)

charCount = {}
charCount[top[0]] = 1
print(charCount)

for k in pairs.keys():
    c = k[1]
    if c in charCount:
        charCount[c] += pairs[k]
    else:
        charCount[c] = pairs[k]

biggest = -10000000000000000
smallest = 10000000000000000

print(charCount)

for k in charCount.keys():
    print(charCount[k])
    if charCount[k] > biggest:
        biggest = charCount[k]
    if charCount[k] < smallest:
        smallest = charCount[k]

print(biggest)
print(smallest)

print(biggest - smallest)

    