def insert(s, index, rules):
    c = rules[s[index:index+2]]
    return s[:index+1] + c + s[index+1:]

with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':
    s = s[:-1]

top,bottom = s.split('\n\n')
ans = top

rules = {}

for line in bottom.split('\n'):
    l,r = line.split(' -> ')
    rules[l] = r

for i in range(0, 10):
    index = 0
    while index < len(ans)-1:
        ans = insert(ans,index,rules)
        index += 2

charCount = {}
for c in ans:
    if c in charCount:
        charCount[c] += 1
    else:
        charCount[c] = 1

biggest = -10000000
smallest = 10000000

for k in charCount.keys():
    if charCount[k] > biggest:
        biggest = charCount[k]
    if charCount[k] < smallest:
        smallest = charCount[k]

print(biggest - smallest)

    