import sys


def solution(n, seq):

    prev = [0 for _ in range(n)]
    dp = [0 for _ in range(n)]

    for i in range(n):
        prev[i] = -1
        dp[i] = 1
        for j in range(i):
            if seq[i] > seq[j]:
                if dp[i] - 1 < dp[j]:
                    prev[i] = j
                    dp[i] = dp[j] + 1

    last = 0
    len_ = dp[0]
    for i in range(n):
        if len_ < dp[i]:
            last = i
            len_ = dp[i]

    sub_seq = list()
    while last >= 0:
        cur = seq[last]
        sub_seq.append(cur)
        last = prev[last]

    sub_seq = reversed(sub_seq)

    return len_, sub_seq


############ ---- Input Optimizations ---- ############
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))

############ ---- Main Block ---- ############


def main():

    n = inp()
    seq = inlt()

    len_, sub_seq = solution(n, seq)
    print(len_)
    print(*sub_seq)


if __name__ == "__main__":
    main()