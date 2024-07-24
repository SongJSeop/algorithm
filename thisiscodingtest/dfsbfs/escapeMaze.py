from collections import deque

n, m = map(int, input().split())
board = [list(map(int, list(input()))) for i in range(n)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for (dx, dy) in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

    return board[n - 1][m - 1]


print(bfs(0, 0))