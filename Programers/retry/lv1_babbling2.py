# 프로그래머스 Lv1. 옹알이 (2)

def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for bab in babbling:
        for word in words:
            if word * 2 not in bab:
                bab = bab.replace(word, " ")

        if len(bab.strip()) == 0:
            answer += 1

    return answer


babbling1 = ["aya", "yee", "u", "maa"]
babbling2 = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

print(solution(babbling1))
print(solution(babbling2))
