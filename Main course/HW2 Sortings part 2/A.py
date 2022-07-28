import random
import copy
import sys


def k_order_statistic(arr, start, end, k):

    if (start < 0 or start >= end):
        return

    pivot = arr[random.randint(start, end - 1)]
    lp = start
    rp = end
    while lp <= rp:
        while arr[lp] < pivot:
            lp += 1

        while pivot < arr[rp]:
            rp -= 1

        if (lp <= rp):
            arr[lp], arr[rp] = arr[rp], arr[lp]
            lp += 1
            rp -= 1

    if k < lp:
        k_order_statistic(arr, start, lp - 1, k)

    if k >= lp:
        k_order_statistic(arr, lp, end, k)


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

############ ---- Deepcopy Optimizations ---- ############


_dispatcher = {}


def _copy_list(l, dispatch):
    ret = l.copy()
    for idx, item in enumerate(ret):
        cp = dispatch.get(type(item))
        if cp is not None:
            ret[idx] = cp(item, dispatch)
    return ret


def _copy_dict(d, dispatch):
    ret = d.copy()
    for key, value in ret.items():
        cp = dispatch.get(type(value))
        if cp is not None:
            ret[key] = cp(value, dispatch)

    return ret


_dispatcher[list] = _copy_list
_dispatcher[dict] = _copy_dict


def deepcopy(sth):
    cp = _dispatcher.get(type(sth))
    if cp is None:
        return sth
    else:
        return cp(sth, _dispatcher)

############ ---- Main Block ---- ############


array_len = inp()
a = inlt()

queries = list()

num_of_queries = inp()
for _ in range(num_of_queries):
    queries.append(inlt())


for m in range(num_of_queries):
    copy_a = deepcopy(a)
    k_order_statistic(copy_a,
                      queries[m][0] - 1,
                      queries[m][1] - 1,
                      queries[m][2] - 1 + (queries[m][0] - 1))
    print(copy_a[queries[m][2] - 1 + (queries[m][0] - 1)])