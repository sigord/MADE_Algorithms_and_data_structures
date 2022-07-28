import sys


def lower_bound(arr, key):
    left = -1
    right = len(arr)
    while left < right - 1:
        mid = int((left + right) / 2)
        if arr[mid] >= key:
            right = mid
        else:
            left = mid
    return right


############ ---- Input Optimizations ---- ############

input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))

############ ---- Main Block ---- ############


lenght_of_array = inp()
arr = inlt()
lenght_of_queries = inp()

arr.sort()

result = list()

for _ in range(lenght_of_queries):
    query = inlt()
    result.append(lower_bound(arr, query[1] + 1) - lower_bound(arr, query[0]))

print(*result)