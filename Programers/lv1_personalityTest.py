# # 프로그래머스 Lv1. 성격 유형 검사

def solution(survey, choices):
    answer = ''

    mbtiDict = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
    for i in range(len(survey)):
        if survey[i] in mbtiDict:
            mbtiDict[survey[i]] += (choices[i] - 4)
        else:
            mbtiDict[survey[i][::-1]] += -(choices[i] - 4)
        print(mbtiDict)

    if mbtiDict["RT"] <= 0:
        answer += "R"
    else:
        answer += "T"
    if mbtiDict["CF"] <= 0:
        answer += "C"
    else:
        answer += "F"
    if mbtiDict["JM"] <= 0:
        answer += "J"
    else:
        answer += "M"
    if mbtiDict["AN"] <= 0:
        answer += "A"
    else:
        answer += "N"

    print(mbtiDict)

    return answer



survey1 = ["AN", "CF", "MJ", "RT", "NA"]
choices1 = [5, 3, 2, 7, 5]
print(solution(survey1, choices1))

survey2 = ["TR", "RT", "TR"]
choices2 = [7, 1, 3]
print(solution(survey2, choices2))
