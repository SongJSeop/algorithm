from datetime import datetime


# 내가 푼 풀이
def validatePosition(column, row):
    return (97 <= column <= 104) and (1 <= row <= 8)


position = input()
startTime = datetime.now()
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
print(datetime.now() - startTime)

# 책 모범 답안
# input_data = input()
# startTime = datetime.now()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# steps = [
#     (-2, -1), (-1, -2), (1, -2), (2, -1),
#     (2, 1), (1, 2), (-1, 2), (-2, 1)
# ]
#
# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#
#     if (1 <= next_row <= 8) and (1 <= next_column <= 8):
#         result += 1
#
# print(result)
# print(datetime.now() - startTime)
