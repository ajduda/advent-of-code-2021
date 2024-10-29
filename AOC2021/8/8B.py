def segToNum(s, known):
    on = set()
    for c in s:
        on.add(known[c])

    if on == {0,1,2,4,5,6}:
        return 0
    if on == {2,5}:
        return 1
    if on == {0,2,3,4,6}:
        return 2
    if on == {0,2,3,5,6}:
        return 3
    if on == {1,2,3,5}:
        return 4
    if on == {0,1,3,5,6}:
        return 5
    if on == {0,1,3,4,5,6}:
        return 6
    if on == {0,2,5}:
        return 7
    if on == {0,1,2,3,4,5,6}:
        return 8
    if on == {0,1,2,3,5,6}:
        return 9
    


allChars = 'abcdefg'
ans = 0

with open('input.txt') as inp:
    s = inp.read()

for line in s.split('\n'):
    segments = []  # order of segments: top, top left, top right, mid, bot left, bot right, bot
    known = {}
    for i in range(0,7):
        segments.append('abcdefg')
    
    for elem in line.split(' '):
        if len(elem) == 2:  # 1 found
            on = [2,5]
            off = [0,1,3,4,6]
        elif len(elem) == 3:  # 7 found
            on = [0,2,5]
            off = [1,3,4,6]
        elif len(elem) == 4:  # 4 found
            on = [1,2,3,5]
            off = [0,4,6]
        elif len(elem) == 5:  # 2,3,5 found
            on = [0,3,6]
            off = []
        elif len(elem) == 6:  # 0,6,9 found
            on = [0,1,5,6]
            off = []
        else: # 8 found, gives no info, or | found, ignore
            continue

        # removeChars will be ~elem, basically
        removeChars = allChars
        for c in elem:
            removeChars = removeChars.replace(c,'')
        
        # We know things not in the element can't be in an on position
        for i in on:
            for c in removeChars:
                if c in segments[i]:
                    segments[i] = segments[i].replace(c,'')

        # We know things in the element can't be in other on positions
        for i in off:
            for c in elem:
                if c in segments[i]:
                    segments[i] = segments[i].replace(c,'')

        # If a segment only has one option, it is known and can be removed as an option from the other segments
        for i in range(0,7):
            if len(segments[i]) == 1:
                known[segments[i]] = i
                for j in range(0,7):
                    if i != j:
                        if segments[i] in segments[j]:
                            segments[j] = segments[j].replace(segments[i],'')

        #print(segments)

    if len(known) < 7:
        print(f'LINE BAD: {line}')

    n = ''
    for elem in line.split(' | ')[1].split(' '):
        n += str(segToNum(elem, known))

    ans += int(n)
print(ans)


