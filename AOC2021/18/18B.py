def printNice(l):
    if l is not None:
        print(str(l).replace(' ',''))

def parse(line, index=0):  # returns ret, index
    ret = []
    index += 1
    while line[index] != ']':
        if line[index] == '[':
            r = parse(line,index)
            ret.append(r[0])
            index = r[1]
        elif line[index] == ',':
            pass
        else:  # Should just be numbers left?
            #Because of antics in doExplodes, gotta make sure multidigit numbers are caught correctly
            rIndex = index
            while line[rIndex].isdigit():
                rIndex += 1
            ret.append(int(line[index:rIndex]))
            index = rIndex-1
        index += 1
    return (ret, index)


# As horrible as this is, I think string manipulation is the way to go here :/
def doExplodes(snailFish):
    line = str(snailFish)
    line = line.replace(' ','')
    depth = 0
    i = 0
    while i < len(line):
        if line[i] == '[':
            depth += 1
        elif line[i] == ']':
            depth -= 1
        elif line[i] == ',':
            pass
        else:  # number found
            if depth == 5:   # I don't normally comment on how awful my code looks, but this is not normal
                temp = line[i:]
                temp = temp.split(']')[0]
                l,r = temp.split(',')
                l = int(l)
                r = int(r)
                lIndex = i-1
                while lIndex >= 0 and not line[lIndex].isdigit():
                    lIndex -= 1
                rIndex = i
                while line[rIndex] != ']':
                    rIndex += 1
                while rIndex < len(line) and not line[rIndex].isdigit():
                    rIndex += 1
                # We have the correct indexes (somehow), do math time
                if lIndex >= 0:
                    a = lIndex  # I'm not sure if numbers can be more than 1 digit, 
                    b = lIndex  # but I'm not going to risk it
                    while line[a].isdigit():
                        a -= 1
                    a += 1
                    while line[b].isdigit():
                        b += 1
                    leftNum = l + int(line[a:b])
                    tempLen = len(line)
                    line = line[:a] + str(leftNum) + line[b:]
                    rIndex += len(line) - tempLen  # Make sure you adjust rindex if things change
                    i += len(line) - tempLen  # and i too so I can find what to remove
                if rIndex < len(line):
                    a = rIndex  # I'm not sure if numbers can be more than 1 digit, 
                    b = rIndex  # but I'm not going to risk it
                    while line[a].isdigit():
                        a -= 1
                    a += 1
                    while line[b].isdigit():
                        b += 1
                    rightNum = r + int(line[a:b])
                    line = line[:a] + str(rightNum) + line[b:]
                # Now for the fun part, remove that OG part and replace with a 0
                a = i
                b = i
                while line[a] != '[':
                    a -= 1
                #if line[a-1] == ',':
                #    a -= 1
                while line[b] != ']':
                    b += 1
                #if line[b+1] == ',':
                #    b += 1
                line = line[:a] + '0' + line[b+1:]
                snailFish = parse(line)[0]  # I forgot parse returns 2 things :(
                return (True, snailFish)
        i += 1
    return (False, snailFish)


def doSplits(snailFish):
    line = str(snailFish)
    line = line.replace(' ','')
    for i in range(0, len(line)-1):
        if line[i].isdigit() and line[i+1].isdigit():
            a = i
            b = i
            while line[b].isdigit():
                b += 1
            n = int(line[a:b])
            pair = f'[{n // 2},{(n // 2) + (n % 2)}]'
            line = line[:a] + pair + line[b:]
            snailFish = parse(line)[0]
            return (True, snailFish)

    return (False, snailFish)



def magnitude(snailFish):
    if type(snailFish) is type(7):
        return snailFish
    else:
        return 3*magnitude(snailFish[0]) + 2*magnitude(snailFish[1])


with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':  # I'll forever rue the trailing newline
    s = s[:-1]

snailFish = None

lines = []

for line in s.split('\n'):
    lines.append(line)

best = -1
for i in range(0, len(lines)):
    print(f'i == {i}')
    for j in range(0, len(lines)):
        if i == j:
            continue
        snailFish = parse(lines[i])[0]     # I had an error where everyhing from here to 171 was
        explodes = True                    # back an indent and I'm silly
        splits = True
        while explodes or splits:
            explodes = doExplodes(snailFish)
            snailFish = explodes[1]
            explodes = explodes[0]
            if explodes:  # Explode until we can't, before we split
                continue
            splits = doSplits(snailFish)
            snailFish = splits[1]
            splits = splits[0]
        snailFish = [snailFish]
        snailFish.append(parse(lines[j])[0])
        explodes = True
        splits = True
        while explodes or splits:
            explodes = doExplodes(snailFish)
            snailFish = explodes[1]
            explodes = explodes[0]
            if explodes:  # Explode until we can't, before we split
                continue
            splits = doSplits(snailFish)
            snailFish = splits[1]
            splits = splits[0]
        m = magnitude(snailFish)
        if m > best:
            #print(lines[i])
            #print(lines[j])
            #print(m)
            best = m

print(best)