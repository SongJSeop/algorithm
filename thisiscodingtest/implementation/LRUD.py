# 내가 푼 풀이
n = int(input())
directions = input().split()

x, y = 1, 1
for direction in directions:
    if direction == "L":
        if y == 1:
            continue
        y -= 1
    elif direction == "R":
        if y == n:
            continue
        y += 1
    elif direction == "U":
        if x == 1:
            continue
        x -= 1
    elif direction == "D":
        if x == n:
            continue
        x += 1

print(x, y)