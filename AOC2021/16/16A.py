def hexToBinStr(b):
    i = int(b,16)
    ret = ''
    if i >= 8:
        i -= 8
        ret += '1'
    else:
        ret += '0'
    if i >= 4:
        i -= 4
        ret += '1'
    else:
        ret += '0'
    if i >= 2:
        i -= 2
        ret += '1'
    else:
        ret += '0'
    if i >= 1:
        i -= 1
        ret += '1'
    else:
        ret += '0'
    if i != 0:
        print('you messed up the hexToBinStr')
        exit()
    return ret


def parse(binStr, index):
    version = int(binStr[index:index+3],2)
    typeID = int(binStr[index+3:index+6],2)
    #print(f'STARTING PARSE: v={version} t={typeID}')
    index += 6
    if typeID == 4:
        valStr = ''
        keepReading = True
        while keepReading:
            keepReading = binStr[index] == '1'
            valStr += binStr[index+1:index+5]
            index += 5
        #print(int(valStr,2))
    else:
        if binStr[index] == '0':  # number of bits in subPackets
            l = int(binStr[index+1:index+16],2)
            index += 16
            target = index + l
            while index < target:
                #print(f'DEBUG: version = {version}, index = {index}, target = {target}')
                r = parse(binStr, index)
                version += r[0]
                index = r[1]
        else:  # number of subpackets
            l = int(binStr[index+1:index+12],2)
            index += 12
            for i in range(0,l):
                r = parse(binStr, index)
                version += r[0]
                index = r[1]
    return (version,index)


with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':  # I'll forever rue the trialing newline
    s = s[:-1]

binString = ''

for c in s:
    binString += hexToBinStr(c)

#print(binString)

print(parse(binString,0)[0])