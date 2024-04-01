n, m, k = map(int, input().split(" "))
numList = list(map(int, input().split(" ")))

numList.sort()
first = numList[n - 1]
second = numList[n - 2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
