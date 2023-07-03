# 프로그래머스 Lv1. 숫자 짝궁

def solution(X, Y):
    answer = ''

    numx = {str(n): 0 for n in range(10)}
    numy = {str(n): 0 for n in range(10)}

    for x in X:
        numx[x] += 1

    for y in Y:
        numy[y] += 1

    for k in range(9, -1, -1):
        k = str(k)
        iternum = min(numx[k], numy[k])

        if answer == '' and k == '0' and iternum != 0:
            return "0"

        answer = ''.join([answer, k * iternum])

    if answer == '':
        return "-1"
    else:
        return answer


X1 = "100"
Y1 = "2345"
print(solution(X1, Y1))

X2 = "5525"
Y2 = "1255"
print(solution(X2, Y2))

X3 = "12321"
Y3 = "42531"
print(solution(X3, Y3))
