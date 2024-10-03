# 내가 푼 풀이
n = int(input())

array = []
for i in range(n):
    array.append(input().split())
    array[i][1] = int(array[i][1])


def sortStandard(data):
    return data[1]


array.sort(key=sortStandard)
for tup in array:
    print(tup[0], end=" ")
