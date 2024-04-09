# 내가 푼 풀이
n, m = map(int, input().split())

numbers = []

for row in range(n):
    numberRow = list(map(int, input().split()))
    numbers.append(numberRow)

result = 1
for row in numbers:
    smallNum = min(row)
    if result < smallNum:
        result = smallNum

print(result)