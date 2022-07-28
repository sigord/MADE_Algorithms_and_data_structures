import sys

A_MOD = 16714589
A1 = 23
A2 = 21563
U1 = 17
U2 = 751
U3 = 2
V1 = 13
V2 = 593
V3 = 5
INF = sys.maxsize


def get_k_power_of_two(k):
    return 1 << k


def get_next_a(prev_a):
    return (A1 * prev_a + A2) % A_MOD


def get_next_u(prev_u, prev_res, query_num, n):
    return ((U1 * prev_u + U2 + prev_res + U3 * query_num) % n) + 1


def get_next_v(prev_v, prev_res, query_num, n):
    return ((V1 * prev_v + V2 + prev_res + V3 * query_num) % n) + 1


def get_array_of_k(n):
    k = [None] * (n + 1)
    k[1] = 0
    for i in range(2, n + 1):
        k[i] = k[i - 1]
        if get_k_power_of_two(k[i] + 1) <= i:
            k[i] += 1
    return k


def solution(n, m, a1, u, v):
    array_of_k = get_array_of_k(n)
    a = [0] * n
    dp = [[INF] * (array_of_k[n] + 1) for _ in range(n)]
    a[0] = a1
    dp[0][0] = a1
    for i in range(1, n):
        a[i] = get_next_a(a[i - 1])
        dp[i][0] = a[i]

    for j in range(1, array_of_k[n] + 1):
        for i in range(n):
            if (i + get_k_power_of_two(j - 1)) < n:
                dp[i][j] = min(dp[i][j - 1], dp[i + get_k_power_of_two(j - 1)][j - 1])

    for q in range(1, m + 1):
        left, right = min(u, v), max(u, v)
        k = array_of_k[right - left + 1]
        res = min(dp[left - 1][k], dp[right - get_k_power_of_two(k)][k])
        if q != m:
            u = get_next_u(u, res, q, n)
            v = get_next_v(v, res, q, n)
    
    return u, v, res

############ ---- Input Optimizations ---- ############

input = sys.stdin.readline

def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))

############ ---- Main Block ---- ############

def main():
    n, m, a1 = inlt()
    u1, v1 = inlt()
    print(*solution(n, m, a1, u1, v1), sep=' ')


if __name__ == "__main__":
    main()