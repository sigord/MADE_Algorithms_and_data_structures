import sys


def solution(str1, str2):

    len1 = len(str1)
    len2 = len(str2)

    dp = [[None] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0 and j == 0:
                dp[i][j] = 0
                continue
            if i == 0 and j > 0:
                dp[i][j] = j
                continue
            if i > 0 and j == 0:
                dp[i][j] = i
                continue
            if j > 0 and i > 0:
                dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1,
                               dp[i - 1][j - 1] + int(str1[i - 1] != str2[j - 1]))

    return dp[len1][len2]


############ ---- Input Optimizations ---- ############
input = sys.stdin.readline


def inps():
    return(str(input()))


############ ---- Main Block ---- ############


def main():

    str1 = inps()
    str2 = inps()
    str1 = str1[:-1]
    str2 = str2[:-1]
    dist = solution(str1, str2)
    print(dist)


if __name__ == "__main__":
    main()