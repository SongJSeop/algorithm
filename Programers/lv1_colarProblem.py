# 프로그래머스 Lv1. 콜라 문제

def solution(a, b, n):
    answer = 0
    left = n
    while left >= a:
        plus = left // a
        answer += plus * b
        left = left % a + plus * b

    return answer


a1 = 2
b1 = 1
n1 = 20
print(solution(a1, b1, n1))

a2 = 3
b2 = 1
n2 = 20
print(solution(a2, b2, n2))
