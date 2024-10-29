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
    index += 6
    if typeID == 4:
        valStr = ''
        keepReading = True
        while keepReading:
            keepReading = binStr[index] == '1'
            valStr += binStr[index+1:index+5]
            index += 5
        val = int(valStr,2)
    else:
        packet = []
        if binStr[index] == '0':  # number of bits in subPackets
            l = int(binStr[index+1:index+16],2)
            index += 16
            target = index + l
            while index < target:
                r = parse(binStr, index)
                packet.append(r[0])
                index = r[1]
        else:  # number of subpackets
            l = int(binStr[index+1:index+12],2)
            index += 12
            for i in range(0,l):
                r = parse(binStr, index)
                packet.append(r[0])
                index = r[1]
        #print(packet)
        if typeID == 0: # sum
            val = sum(packet)
        elif typeID == 1: # product
            val = 1
            for p in packet:
                val *= p
        elif typeID == 2:
            val = min(packet)
        elif typeID == 3:
            val = max(packet)
        elif typeID == 5:
            if packet[0] > packet[1]:
                val = 1
            else:
                val = 0
        elif typeID == 6:
            if packet[0] < packet[1]:
                val = 1
            else:
                val = 0
        elif typeID == 7:
            if packet[0] == packet[1]:
                val = 1
            else:
                val = 0
        else:
            print('you broke it')
            exit()

    return (val,index)


with open('input.txt') as inp:
    s = inp.read()

if s[-1] == '\n':  # I'll forever rue the trialing newline
    s = s[:-1]

binString = ''

for c in s:
    binString += hexToBinStr(c)


print(parse(binString,0)[0])