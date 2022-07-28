import sys
HUNDRED = 100
MAXINT = sys.maxsize

class solution():

    def __init__(self, n, prices):

        self.prices = prices
        self.n = n
        self.dp = [[-1] * (n + 1) for _ in range(n + 2)]
        self.used = []

    def DP(self, i, j):
        if j > i:
            return MAXINT
        else:
            cost = self.prices[i]
            result = None
            if j <= 0:
                if i >= 1:
                    if cost <= HUNDRED:
                        dif = min(
                            self.DP(
                                i - 1,
                                j + 1),
                            self.DP(
                                i - 1,
                                j) + cost)
                        result = dif
                    else:
                        return self.DP(i - 1, j + 1)
                else:
                    return 0
            else:
                if self.dp[i][j] != -1:
                    return self.dp[i][j]
                if cost > HUNDRED:
                    dif = min(
                        self.DP(
                            i - 1,
                            j + 1),
                        self.DP(
                            i - 1,
                            j - 1) + cost)
                    result = dif
                else:
                    dif = min(self.DP(i - 1, j + 1), self.DP(i - 1, j) + cost)
                    result = dif

            self.dp[i][j] = result
            return result

    def free_days(self, i, j):
        if j < i:
            cost = self.prices[i]
            if j <= 0:
                if i >= 1:
                    if cost > HUNDRED:
                        self.used.append(i)
                        self.free_days(i - 1, j + 1)
                    else:
                        if self.DP(i, j) == self.DP(i - 1, j + 1):
                            self.used.append(i)
                            self.free_days(i - 1, j + 1)
                        else:
                            self.free_days(i - 1, j)
            else:
                if cost <= HUNDRED:
                    if self.DP(i - 1, j + 1) == self.DP(i, j):
                        self.used.append(i)
                        self.free_days(i - 1, j + 1)
                    else:
                        self.free_days(i - 1, j)
                else:
                    if self.DP(i - 1, j + 1) == self.DP(i, j):
                        if self.n == 3:
                            self.used.append(i-1)
                        else:
                            self.used.append(i)
                        self.free_days(i - 1, j + 1)
                    else:
                        self.free_days(i - 1, j - 1)

    def main_sol(self):
        k1 = 0
        k2 = 0
        sum_cost = MAXINT

        for i in range(self.n + 1):
            if sum_cost >= self.DP(self.n, i):
                sum_cost = self.DP(self.n, i)
                k1 = i

        self.free_days(self.n, k1)

        k2 = len(self.used)

        return sum_cost, k1, k2, self.used


############ ---- Input Optimizations ---- ############
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


############ ---- Main Block ---- ############


def main():

    n = inp()
    prices = list()
    for _ in range(n):
        prices.append(inp())

    prices = [0] + prices
    sol = solution(n, prices)
    sum_cost, k1, k2, days_for_coupon = sol.main_sol()
    days_for_coupon = reversed(days_for_coupon)
    print(sum_cost)
    print(k1, ' ', k2, sep='')
    print(*days_for_coupon, sep='\n')


if __name__ == "__main__":
    main()