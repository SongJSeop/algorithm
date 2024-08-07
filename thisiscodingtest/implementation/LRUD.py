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

# 책 모범 답안
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)