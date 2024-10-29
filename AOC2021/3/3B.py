def findMost(arr, index, default):
    zero = 0
    one = 0
    for a in arr:
        if a[index] == '0':
            zero += 1
        else:
            one += 1
    print(f'0: {zero}   1: {one}')
    if zero == one:
        return default
    if zero > one:
        return '0'
    return '1'


freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n = 0
a = ''
b = ''
nums = []
with open('input.txt') as inp:
    for line in inp:
        length = len(line.strip())
        freq = freq[0:length]
        nums.append(line.strip())
        for i in range(0, length):
            if line[i] == '1':
                freq[i] += 1
        n += 1
    for x in freq:
        if x * 2 > n:
            a += '1'
            b += '0'
        else:
            a += '0'
            b += '1'

temp1 = nums.copy()
i = 0
while len(temp1) > 1:
    print(temp1)
    keep = findMost(temp1, i, '1')
    print(keep)
    temp2 = []
    for val in temp1:
        if val[i] == keep:
            temp2.append(val)
    temp1 = temp2.copy()
    i += 1

o2 = temp1[0]
print(o2)

temp1 = nums.copy()
i = 0
while len(temp1) > 1:
    print(temp1)
    keep = findMost(temp1, i, '1')
    if keep == '1':
        keep = '0'
    else:
        keep = '1'
    print(keep)
    temp2 = []
    for val in temp1:
        if val[i] == keep:
            temp2.append(val)
    temp1 = temp2.copy()
    i += 1
co2 = temp1[0]

print(o2)
print(co2)
print(int(o2,2)*int(co2,2))