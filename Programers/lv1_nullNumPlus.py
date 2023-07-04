# 프로그래머스 Lv1. 없는 숫자 더하기

def solution(numbers):
    answer = 0

    for i in range(1, 10):
        if i not in numbers:
            answer += i

    return answer


numbers1 = [1,2,3,4,6,7,8,0]
print(solution(numbers1))
numbers2 = [5,8,4,0,6,7,9]
print(solution(numbers2))
