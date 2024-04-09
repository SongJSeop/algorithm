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

# 책 모범 답안
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
