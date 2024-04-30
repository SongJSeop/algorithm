# 내가 푼 풀이
hour = int(input())

count = 0
for i in range(hour+1):
    if '3' in str(i):
        count += 3600
    else:
        count += 1575

print(count)
