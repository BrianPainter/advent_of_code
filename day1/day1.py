from collections import Counter
movements = 'R3, R1, R4, L4, R3, R1, R1, L3, L5, L5, L3, R1, R4, L2, L1, R3, L3, R2, R1, R1, L5, L2, L1, R2, L4, R1, L2, L4, R2, R2, L2, L4, L3, R1, R4, R3, L1, R1, L5, R4, L2, R185, L2, R4, R49, L3, L4, R5, R1, R1, L1, L1, R2, L1, L4, R4, R5, R4, L3, L5, R1, R71, L1, R1, R186, L5, L2, R5, R4, R1, L5, L2, R3, R2, R5, R5, R4, R1, R4, R2, L1, R4, L1, L4, L5, L4, R4, R5, R1, L2, L4, L1, L5, L3, L5, R2, L5, R4, L4, R3, R3, R1, R4, L1, L2, R2, L1, R4, R2, R2, R5, R2, R5, L1, R1, L4, R5, R4, R2, R4, L5, R3, R2, R5, R3, L3, L5, L4, L3, L2, L2, R3, R2, L1, L1, L5, R1, L3, R3, R4, R5, L3, L5, R1, L3, L5, L5, L2, R1, L3, L1, L3, R4, L1, R3, L2, L2, R3, R3, R4, R4, R1, L4, R1, L5'
angle = 90
direction = {0: 'R', 90: 'U', 180: 'L', 270: 'D'}
totals = {'R': 0, 'U': 0, 'L': 0, 'D': 0, 'DIST': 0, 'x': 0, 'y': 0}
visits = []

for move in movements.split(', '):
    move_dir = move[0]
    move_dist = int(move[1:])

    if move_dir == 'R':
        angle = (angle - 90) % 360
    else:
        angle = (angle + 90) % 360

    totals[direction.get(angle)] += int(move_dist)
    totals['x'] = totals['R'] - totals['L']
    totals['y'] = totals['U'] - totals['D']
    totals['DIST'] = abs(totals['x']) + abs(totals['y'])
    # loc = (totals['R'] - totals['L'], totals['U'] - totals['D'])
    # if loc in visits:
    #     print(loc)
    # else:
    #     visits.append(loc)

    print(totals)
print(visits)
print([k for k, v in Counter(visits).items() if v > 1])

seen = list()
for place in visits:
    if place[0] == 9:
        print(place)
    seen.append(place)

# print(visits)
