import sys


def solution(n, k, transactions):
    dp = [0 for _ in range(n + 1)]
    money = [0 for _ in range(n + 1)]

    dp[1] = 0
    max_sub = 0

    for i in range(2, n + 1):
        max_sub = i - 1
        if (i - k) > 1:
            max_ = i - k
        else:
            max_ = 1

        j = max_
        while j < i:
            if dp[max_sub] < dp[j]:
                max_sub = j
            j += 1

        money[i] = max_sub
        dp[i] = dp[max_sub] + transactions[i]

    count = 0
    num = n

    path = list()
    path.append(num)

    while num > 1:
        num = money[num]
        path.append(num)
        count += 1

    path = reversed(path)

    return dp[n], count, path


############ ---- Input Optimizations ---- ############

input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))

############ ---- Main Block ---- ############


def main():

    n, k = inlt()
    transactions = inlt()
    transactions = [0, 0] + transactions + [0]
    max_money, num_of_jumps, path = solution(n, k, transactions)
    print(max_money)
    print(num_of_jumps)
    print(*path)


if __name__ == "__main__":
    main()