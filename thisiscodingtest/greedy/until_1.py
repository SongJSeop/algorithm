# 내가 푼 풀이
n, k = map(int, input().split())

count = 0
while n != 1:
    if n % k == 0:
        n /= k
        count += 1
        continue
    n -= 1
    count += 1

print(count)

# 책 모범 답안
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)  # result에 n을 k로 나눈 나머지가 더해짐 (어차피 빼야함)
    n = target  # n엔 나누어 떨어지는 수만 남음

    if n < k:  # 나눌 수 없다면 반복 중지
        break

    result += 1
    n //= k

result += (n - 1)  # n - 1번 어차피 빼야하므로
print(result)
