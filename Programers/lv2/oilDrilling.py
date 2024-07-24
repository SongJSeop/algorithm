from collections import deque


def solution(land):
    rowLen, colLen = len(land), len(land[0])
    oilAmount = [0] * colLen
    visited = [[False] * colLen for _ in range(rowLen)]
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(x, y):
        queue = deque()
        queue.append([x, y])
        count = 1
        visited[x][y] = True
        visitCols = {y}

        while queue:
            row, col = queue.popleft()
            for (dx, dy) in delta:
                newX, newY = row + dx, col + dy
                if 0 <= newX < rowLen and 0 <= newY < colLen and land[newX][newY] == 1 and not visited[newX][newY]:
                    queue.append([newX, newY])
                    visited[newX][newY] = True
                    count += 1
                    visitCols.add(newY)

        for visitCol in visitCols:
            oilAmount[visitCol] += count

    for i in range(rowLen):
        for j in range(colLen):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    return max(oilAmount)



land1 = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 1, 1]]
land2 = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print(solution(land1))
print(solution(land2))
