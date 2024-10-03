# # 내가 푼 풀이
# n, k = map(int, input().split())
#
# arrayA = list(map(int, input().split()))
# arrayB = list(map(int, input().split()))
#
# for i in range(k):
#     arrayA.sort()
#     arrayB.sort()
#     arrayA[0], arrayB[n-1] = arrayB[n-1], arrayA[0]
#
# print(sum(arrayA))

# 모범 답안
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))