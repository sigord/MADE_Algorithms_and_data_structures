def solve():

    def z_fun(string):
        n = len(string)
        z = [0] * n
        l = 0
        r = 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while ((i + z[i]) < n) and (string[z[i]] == string[i + z[i]]):
                z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        return z

    string = input()

    result = z_fun(string)

    print(*result[1:])

if __name__ == "__main__":
    solve()