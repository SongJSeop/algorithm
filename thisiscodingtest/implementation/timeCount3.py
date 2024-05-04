# 내가 푼 풀이
hour = int(input())

count = 0
for i in range(hour+1):
    if '3' in str(i):
        count += 3600
    else:
        count += 1575

print(count)

# 책 모범 답안
# h = int(input())
#
# count = 0
# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
#
# print(count)
