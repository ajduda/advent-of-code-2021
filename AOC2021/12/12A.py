def findEnd(paths, smallCavesAvailable, current):
    smallCavesAvailable = smallCavesAvailable.copy()
    if current == 'end':
        return 1
    if current in smallCavesAvailable:
        smallCavesAvailable.remove(current)
    ret = 0
    for path in paths[current]:
        if path.isupper() or path in smallCavesAvailable:
            ret += findEnd(paths, smallCavesAvailable, path)
    return ret

with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':  # I forever rue the trailing newline
    s = s[:-1]

smallCaves = set()
paths = {}


for line in s.split('\n'):
    l,r = line.split('-')
    if l.islower():
        smallCaves.add(l)
    if r.islower():
        smallCaves.add(r)
    if l in paths:
        paths[l].append(r)
    else:
        paths[l] = [r]
    if r in paths:
        paths[r].append(l)
    else:
        paths[r] = [l]

#print(paths)
#print(smallCaves)

print(findEnd(paths, smallCaves, 'start'))