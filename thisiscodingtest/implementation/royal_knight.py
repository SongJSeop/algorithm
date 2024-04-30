# 내가 푼 풀이
def validatePosition(column, row):
    return (97 <= column <= 104) and (1 <= row <= 8)


position = input()
column, row = ord(position[0]), int(position[1])

canMove = 0
moveList = [
    (column - 2, row - 1),
    (column - 2, row + 1),
    (column + 2, row - 1),
    (column + 2, row + 1),
    (column - 1, row - 2),
    (column + 1, row - 2),
    (column - 1, row + 2),
    (column + 1, row + 2)
]

for move in moveList:
    if validatePosition(move[0], move[1]):
        canMove += 1

print(canMove)