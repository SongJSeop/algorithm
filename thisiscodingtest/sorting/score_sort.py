# 내가 푼 풀이
n = int(input())

array = []
for i in range(n):
    array.append(input().split())
    array[i][1] = int(array[i][1])


def sortStandard(data):
    return data[1]


array.sort(key=sortStandard)
for tup in array:
    print(tup[0], end=" ")

# # 모범 답안
# n = int(input())
#
# array = []
# for i in range(n):
#     input_data = input().split()
#     array.append((input_data[0], int(input_data[1])))
#
# array = sorted(array, key=lambda student: student[1])
#
# for student in array:
#     print(student[0], end=" ")
