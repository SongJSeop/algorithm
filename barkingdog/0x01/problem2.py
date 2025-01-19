# 주어진 길이 N의 int 배열 arr에서 합이 100인 서로 다른 위치의 두 원소가 존재하면 1을, 존재하지 않으면 0을 반환하는 함수를 작성하라. (arr의 각 수는 0 이상 100 이하이고 N은 1000 이하의 자연수)
import random

def solution(arr):
    for num in arr:
        diffNum = 100 - num
        for num2 in arr:
            if num2 == diffNum:
                return 1
    return 0

N = int(input())
print(solution([random.randint(0, 100) for _ in range(N)]))

# 시간복잡도 O(N^2)