with open('input.txt') as inp:
    s = inp.read()


arr = []
for line in s.split('\n'):
    arr.append([])
    for c in line:
        arr[-1].append(int(c))

ans = 0

#print(arr)
for x in range(0, len(arr[0])):
    for y in range(0, len(arr)):
        if x > 0:
            if arr[y][x] >= arr[y][x-1]:
                continue
        if y > 0:
            if arr[y][x] >= arr[y-1][x]:
                continue
        if x < len(arr[0])-1:
            if arr[y][x] >= arr[y][x+1]:
                continue
        if y < len(arr) - 1:
            if arr[y][x] >= arr[y+1][x]:
                continue
        ans += 1 + arr[y][x]
        #print(f'({x},{y}) = {arr[y][x]}')

print(ans)