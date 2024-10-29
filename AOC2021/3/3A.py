freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n = 0
a = ''
b = ''
with open('input.txt') as inp:
    for line in inp:
        length = len(line.strip())
        freq = freq[0:length]
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
print(int(a, 2) * int(b, 2))