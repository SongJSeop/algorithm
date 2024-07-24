from collections import deque

answer = 0
n, m = map(int, input().split())
board = []
visited = [[False] * m for _ in range(n)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(n):
    board.append(list(map(int, list(input()))))


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        px, py = queue.popleft()
        for (dx, dy) in delta:
            nx, ny = px + dx, py + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True


for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            answer += 1

print(answer)
