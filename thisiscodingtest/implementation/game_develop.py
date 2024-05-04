# 내가 푼 풀이
def turn():
    if direction == 0:
        return 3
    return direction - 1


def checkCanMoveTo(toX, toY):
    return (
            (0 <= toX < row) and
            (0 <= toY < column) and
            (gameMap[toX][toY] != 1) and
            ((toX, toY) not in alreadyMoved)
    )


def checkCantMoveNow():
    return not (
            checkCanMoveTo(x - 1, y) or
            checkCanMoveTo(x + 1, y) or
            checkCanMoveTo(x, y - 1) or
            checkCanMoveTo(x, y + 1)
    )


def isBehindOcean():
    behindX, behindY = x - dxdy[direction][0], y - dxdy[direction][1]
    return gameMap[behindX][behindY] == 1


def checkGameBreak():
    global x
    global y
    if checkCantMoveNow():
        if isBehindOcean():
            return True
        x, y = x - dxdy[direction][0], y - dxdy[direction][1]
        return checkGameBreak()
    else:
        return False


row, column = map(int, input().split())
x, y, direction = map(int, input().split())

gameMap = []
for i in range(0, row):
    gameMap.append(list(map(int, input().split())))

dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
alreadyMoved = [(x, y)]
while True:
    direction = turn()
    newX, newY = x + dxdy[direction][0], y + dxdy[direction][1]
    if checkCanMoveTo(newX, newY):
        x, y = newX, newY
        alreadyMoved.append((x, y))
        if checkGameBreak():
            break

print(len(alreadyMoved))