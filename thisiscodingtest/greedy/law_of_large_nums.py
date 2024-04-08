n, m, k = map(int, input().split(" "))
numList = list(map(int, input().split(" ")))

numList.sort()
first = numList[n - 1]
second = numList[n - 2]

# count는 가장 큰 숫자(first)가 나오는 횟수
count = int(m / (k + 1)) * k  # 'm / (k + 1)'의 몫만큼 반복하며, 그 반복 하나하나에 k개 만큼 큰 숫자가 들어감
count += m % (k + 1)  # 나머지도 더해줌

result = 0
result += count * first  # 가장 큰 숫자가 더해진 값
result += (m - count) * second  # 두 번재 숫자가 더해진 값
