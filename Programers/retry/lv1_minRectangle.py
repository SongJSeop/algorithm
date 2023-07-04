# 프로그래머스 Lv1. 최소직사각형

def solution(sizes):
    W = 0
    H = 0
    for size in sizes:
        w = max(size[0], size[1])
        h = min(size[0], size[1])
        W = max(W, w)
        H = max(H, h)

    return W * H


sizes1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes1))
sizes2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes2))
sizes3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes3))
