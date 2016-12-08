from collections import Counter, defaultdict

# part 1
letters = defaultdict(list)
with open('input') as f:
    for line in f:
        print(list(line.strip()))
        for idx, let in list(enumerate(list(line.strip()))):
            letters[idx] += let

    for k, v in letters.items():
        print(k, Counter(letters[k]).most_common(1))

# part 2
letters = defaultdict(list)
with open('input') as f:
    for line in f:
        # print(list(line.strip()))
        for idx, let in list(enumerate(list(line.strip()))):
            letters[idx] += let
    for k, v in letters.items():
        print(k, Counter(letters[k]).most_common()[:-2:-1])
