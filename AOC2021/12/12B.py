caveStrs = set()

def findEnd(paths, smallCavesAvailable, current, dupUsed, str):
    smallCavesAvailable = smallCavesAvailable.copy()
    if str != '' and current == 'start':
        return 0
    str += current + ','
    if current == 'end':
        #print(str)
        caveStrs.add(str)
        return 1
    if current in smallCavesAvailable:
        smallCavesAvailable.remove(current)
    elif not dupUsed and current.islower():
        dupUsed = True
        #smallCavesAvailable.add(current)
    for path in paths[current]:
        if path.isupper() or path in smallCavesAvailable or not dupUsed:
            findEnd(paths, smallCavesAvailable, path, dupUsed, str)

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

findEnd(paths, smallCaves, 'start', False, '')

print(len(caveStrs))