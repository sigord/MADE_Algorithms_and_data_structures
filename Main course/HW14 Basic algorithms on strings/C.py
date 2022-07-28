def solve():

    def pref_fun(string):
        n = len(string)
        prefix = [0] * n

        for i in range(1, n):
            j = prefix[i - 1]
            while (j > 0) and (string[i] != string[j]):
                j = prefix[j - 1]
            if string[i] == string[j]:
                j += 1
            prefix[i] = j

        return prefix

    def KMP(p, t):
        len_p = len(p)
        len_t = len(t)
        pref = pref_fun(p + "#" + t)
        result = []

        for i in range(len_p, (len_p + len_t + 1)):
            if pref[i] == len_p:
                result.append((i - len_p * 2 + 1))
        
        return result

    substr = input()
    string = input()


    result = KMP(substr, string)

    print(len(result))
    print(*result)
     

if __name__ == "__main__":
    solve()