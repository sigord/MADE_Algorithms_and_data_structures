import math
EPS = 1e-6
LEFT = 1.0
RIGHT = 10**10
ITN = int(math.log2((RIGHT - LEFT) / EPS)) + 1


def fun(x):
    return x * x + x**0.5


def bin_search(f, y, left, right):

    for _ in range(ITN):
        mid = (left + right) / 2
        if f(mid) >= y:
            right = mid
        else:
            left = mid
    return right


c = float(input())
print(bin_search(fun, c, 0, c))