# 프로그래머스 Lv1. 나머지가 1이 되는 수 찾기

def solution(n):
    answer = 0
    i = 1
    while True:
        if n % i == 1:
            answer = i
            break
        i += 1
    return answer


n1 = 10
print(solution(n1))
n2 = 12
print(solution(n2))
