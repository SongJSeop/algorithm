import sys

X = int(sys.stdin.readline().rstrip())

results = [0] * (X + 1)
now = 1
for i in range(2, X + 1):
    canNext = [i-1]
    if i % 5 == 0:
        nextNum = i // 5
        if nextNum == 1:
            results[i] = nextNum
            continue
        canNext.append(nextNum)

    if i % 3 == 0:
        nextNum = i // 3
        if nextNum == 1:
            results[i] = nextNum
            continue
        canNext.append(nextNum)

    if i % 2 == 0:
        nextNum = i // 2
        if nextNum == 1:
            results[i] = nextNum
            continue
        canNext.append(nextNum)

    minCount = 30000
    for nextNum in canNext:
        minCount = min(minCount, results[nextNum])

    results[i] = minCount + 1

print(results[X])