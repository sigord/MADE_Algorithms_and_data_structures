import sys


def solution(n, m, transaction_matrix):
    dp = [[0] * m for _ in range(n)]

    dp[0][0] = transaction_matrix[0][0]

    for i in range(n):
        for j in range(m):
            if i == 0 and j > 0:
                dp[i][j] = dp[i][j - 1] + transaction_matrix[i][j]
            if i > 0 and j == 0:
                dp[i][j] = dp[i - 1][j] + transaction_matrix[i][j]
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + \
                    transaction_matrix[i][j]

    i = n - 1
    j = m - 1

    path = ''

    while i != 0 or j != 0:

        if i == 0:
            j -= 1
            path += 'R'
        elif j == 0:
            i -= 1
            path += 'D'
        elif i > 0 and j > 0:
            if dp[i][j - 1] > dp[i - 1][j]:
                j -= 1
                path += 'R'
            else:
                path += 'D'
                i -= 1

    path = path[::-1]

    return dp[n - 1][m - 1], path


############ ---- Input Optimizations ---- ############
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))

############ ---- Main Block ---- ############


def main():

    transactions_matrix = list()
    n, m = inlt()
    for _ in range(n):
        transactions_matrix.append(inlt())

    max_money, path = solution(n, m, transactions_matrix)
    print(max_money)
    print(path)


if __name__ == "__main__":
    main()