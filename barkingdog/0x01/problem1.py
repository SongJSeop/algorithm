#N 이하의 자연수 중에서 3의 배수이거나 5의 배수인 수를 모두 합한 값을 반환하는 함수를 작성하라. (N은 10만 이하의 자연수)
num = int(input())

total = 0
for i in range(1, num + 1):
	if i % 3 == 0 or i % 5 == 0:
		total += i

print(total)

# 시간복잡도 O(N)