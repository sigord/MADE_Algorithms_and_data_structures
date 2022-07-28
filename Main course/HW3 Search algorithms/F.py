import math
EPS = 1e-4
LEFT = 0.0
RIGHT = 1.0
ITN = int(math.log(((RIGHT - LEFT) / EPS), 3 / 2)) + 1


def fun(vel_in_field, vel_in_forest, point_a, x):

    time = (((1 - point_a)**2 + x**2)**0.5) / vel_in_field + \
           ((point_a**2 + (1 - x)**2)**0.5) / vel_in_forest
    return time


def ternary_search(f, vel_in_field, vel_in_forest, point_a):

    left = LEFT
    right = RIGHT

    for _ in range(ITN):
        mid_l = (left * 2 + right) / 3
        mid_r = (left + right * 2) / 3
        if f(vel_in_field, vel_in_forest, point_a, mid_l) < f(vel_in_field, vel_in_forest, point_a, mid_r):
            right = mid_r
        else:
            left = mid_l

    return right


vel_in_field, vel_in_forest = map(int, input().split())
point_a = float(input())
print(float(ternary_search(fun, vel_in_field, vel_in_forest, point_a)))