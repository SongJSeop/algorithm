# # 프로그래머스 Lv1. 신고 결과 받기

def solution(id_list, report, k):
    answer = []

    attackerDict1 = {attacker: 0 for attacker in id_list}
    attackerDict2 = {victim: set() for victim in id_list}
    reportDict = {reporter: 0 for reporter in id_list}

    report = set(report)
    for rep in report:
        victim, attacker = rep.split()
        attackerDict2[attacker].add(victim)
        attackerDict1[attacker] += 1

    for attacker in attackerDict1:
        if attackerDict1[attacker] >= k:
            for victim in attackerDict2[attacker]:
                reportDict[victim] += 1

    for num in reportDict.values():
        answer.append(num)

    return answer


id_list1 = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k1 = 2
print(solution(id_list1, report1, k1))

id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3
print(solution(id_list2, report2, k2))
