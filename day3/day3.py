from collections import deque

possible = 0
with open('input') as f:
    for line in f:
        x = list(map(int,line.split()))
        print(x)
        if x[0] + x[1] > x[2] and x[0] + x[2] > x[1] and x[1] + x[2] > x[0]:
            print('above is possible')
            possible += 1

print(possible)

arr = list()
with open('input') as f:
    for line in f:
        arr.append(list(map(int, line.split())))

for r in range(0, len(arr), 3):
    for y in range(3):
        t = deque()
        for x in range(3):
            t.append(arr[r+x][y])
        
        if t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]:
            possible += 1
        
print(possible)
