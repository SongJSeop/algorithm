import sys

def binarySearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


N = int(sys.stdin.readline().rstrip())
parts = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
searchParts = list(map(int, sys.stdin.readline().split()))

sortedParts = sorted(parts)
result = 0
for searchPart in searchParts:
    if binarySearch(sortedParts, searchPart, 0, N - 1):
        print("yes", end=" ")
        continue

    print("no", end=" ")