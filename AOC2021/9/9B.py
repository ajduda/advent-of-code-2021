def floodfill(arr, x, y):
    if arr[y][x] == -1 or arr[y][x] == 9:
        return 0
    arr[y][x] = -1
    ret = 1 # This square
    if x > 0:
        ret += floodfill(arr, x-1, y)
    if y > 0:
        ret += floodfill(arr, x, y-1)
    if x < len(arr[0])-1:
        ret += floodfill(arr, x+1, y)
    if y < len(arr) - 1:
        ret += floodfill(arr, x, y+1)
    return ret


with open('input.txt') as inp:
    s = inp.read()


arr = []
for line in s.split('\n'):
    arr.append([])
    for c in line:
        arr[-1].append(int(c))

ans = 0

areas = []

for y in range(0, len(arr)):
    for x in range(0, len(arr[0])):
        areas.append(floodfill(arr, x, y))

areas.sort()
print(areas[-3])
print(areas[-2])
print(areas[-1])
print(areas[-3] * areas[-2] * areas[-1])