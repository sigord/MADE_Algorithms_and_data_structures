import math
LEFT = 1
RIGHT = 10**8
EPS = 1
ITN = int(math.log2((RIGHT - LEFT) / EPS)) + 1


def fun(list_of_lengths, number_of_ropes, x):

    sum_equal_elem = 0
    for i in range(number_of_ropes):
        sum_equal_elem += int(list_of_lengths[i] / x)
    return sum_equal_elem


def bin_search(f, list_of_lengths, number_of_ropes, number_of_cabins):

    left = LEFT
    right = RIGHT

    for _ in range(ITN):
        mid = int((left + right) / 2)
        if f(list_of_lengths, number_of_ropes, mid) < number_of_cabins:
            right = mid
        else:
            left = mid
    return right - 1


number_of_ropes, number_of_cabins = map(int, input().split())
list_of_lengths = list()
for _ in range(number_of_ropes):
    list_of_lengths.append(int(input()))

print(bin_search(fun, list_of_lengths, number_of_ropes, number_of_cabins))