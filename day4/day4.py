from collections import Counter

total = 0
with open('input') as f:
    for line in f:
        # print(line)
        room = line.replace('[', '-').replace(']', '').rsplit('-', 2)
        # print(room)
        counter = sorted(sorted(Counter(room[0].replace('-', '')).most_common(), key=lambda letter: letter[0]), reverse=True, key=lambda letter: letter[1])[:5]
        checksum = ''.join([l[0] for l in counter])
        if checksum == room[2].rstrip():
            total += int(room[1])
            print(room[1])
            print(''.join([chr(((ord(l) - 97 + int(room[1])) % 26) + 97) if l != '-' else '-' for l in room[0]]))

print(total)
