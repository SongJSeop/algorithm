# 내가 푼 풀이
n, k = map(int, input().split())

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

for i in range(k):
    arrayA.sort()
    arrayB.sort()
    arrayA[0], arrayB[n-1] = arrayB[n-1], arrayA[0]

print(sum(arrayA))