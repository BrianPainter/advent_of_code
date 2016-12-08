

pos = [1, 1]
keypad1 = [['1', '2', '3'],
           ['4', '5', '6'],
           ['7', '8', '9']]
keypad2 = [['X', 'X', '1', 'X', 'X'],
           ['X', '2', '3', '4', 'X'],
           ['5', '6', '7', '8', '9'],
           ['X', 'A', 'B', 'C', 'X'],
           ['X', 'X', 'D', 'X', 'X']]
print('first code:')
with open('input') as f:
    for line in f:
        for move in line:
            if move == 'R' and pos[1] < 2:
                pos[1] += 1
            elif move == 'L' and pos[1] > 0:
                pos[1] -= 1
            elif move == 'U' and pos[0] > 0:
                pos[0] -= 1
            elif move == 'D' and pos[0] < 2:
                pos[0] += 1
        print(keypad1[pos[0]][pos[1]])

print('second code:')
pos = [2, 0]
with open('input') as f:
    for line in f:
        for move in line:
            if move == 'R' and pos[1] < 4 and keypad2[pos[0]][pos[1]+1] != 'X':
                pos[1] += 1
            elif move == 'L' and pos[1] > 0 and keypad2[pos[0]][pos[1]-1] != 'X':
                pos[1] -= 1
            elif move == 'U' and pos[0] > 0 and keypad2[pos[0]-1][pos[1]] != 'X':
                pos[0] -= 1
            elif move == 'D' and pos[0] < 4 and keypad2[pos[0]+1][pos[1]] != 'X':
                pos[0] += 1
        print(keypad2[pos[0]][pos[1]])
