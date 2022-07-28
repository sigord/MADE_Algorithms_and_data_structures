import sys
UNICODE = "utf-8"


class FenwickTree:
    def __init__(self, array, n):
        self.array = array
        self.size = n
        self.T = []
        for i in range(n):
            current_sum = 0
            for j in range(self.f(i), i + 1):
                current_sum += self.array[j]
            self.T.append(current_sum)

    @staticmethod
    def f(i):
        return i & (i + 1)

    def get(self, i):
        res = 0
        while i >= 0:
            res += self.T[i]
            i = self.f(i) - 1
        return res

    def rsq(self, left, right):
        if left == 0:
            return self.get(right)
        return self.get(right) - self.get(left - 1)

    def add(self, i, x):
        j = i
        while j < self.size:
            self.T[j] += x
            j = j | (j + 1)

    def set(self, i, x):
        d = x - self.array[i]
        self.array[i] = x
        self.add(i, d)


############ ---- Main Block ---- ############

def solve():
    data = sys.stdin.buffer.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    ftree = FenwickTree(a, n)
    for operation in data[2:]:
        args = operation.decode(UNICODE).split()
        if args[0] == 'sum':
            print(ftree.rsq(int(args[1]) - 1, int(args[2]) - 1))
        else:
            ftree.set(int(args[1]) - 1, int(args[2]))


if __name__ == "__main__":
    solve()