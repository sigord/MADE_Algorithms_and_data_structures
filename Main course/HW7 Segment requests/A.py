import sys

############ ---- Input Optimizations ---- ############

input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))

############ ---- Main Block ---- ############


def rsq(l, r, sum_arr):
    if l == 0:
        return sum_arr[r]
    return sum_arr[r] - sum_arr[l - 1]


def main():
    n, x, y, a0 = inlt()
    m, z, t, b0 = inlt()
    prev_a = a0
    sum_arr = [None] * n
    result = 0
    sum_arr[0] = a0

    # create array of sums
    for i in range(1, n):
        a = (x * prev_a + y) % (2**16)
        sum_arr[i] = sum_arr[i - 1] + a
        prev_a = a
    # queries
    for j in range(0, m * 2, 2):
        # left border
        if j == 0:
            # 0 elem
            prev_b = b0
            prev_c = b0 % n
        else:
            # 1 elem
            b = (z * prev_b + t) % (2**30)
            c = b % n
            prev_c = c
            prev_b = b
        # right border
        # 2 elem
        b = (z * prev_b + t) % (2**30)
        c = b % n
        # query
        result += rsq(min(prev_c, c), max(prev_c, c), sum_arr)
        # update
        prev_b = b
        prev_c = c
    print(result)


if __name__ == "__main__":
    main()