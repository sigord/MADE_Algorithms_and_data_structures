def data_char2int(strings, num_of_strings):
    for i in range(num_of_strings):
        strings[i] = [x - (ord('a') - 1) for x in list(map(ord, strings[i]))]


def data_int2char(strings, num_of_strings):
    for i in range(num_of_strings):
        strings[i] = [chr(x + (ord('a') - 1)) for x in strings[i]]


def radix_sort(strings, num_of_strings, lenght_of_strings, k):

    max_digit = max([max(x) for x in strings])

    for i in range(k):

        cnt = [0] * max_digit

        for j in range(num_of_strings):
            elem = strings[j][i] - 1
            cnt[elem] += 1

        count = 0
        for j in range(max_digit):
            tmp = cnt[j]
            cnt[j] = count
            count += tmp

        sorted_s = [[0] * lenght_of_strings] * num_of_strings
        for j in range(num_of_strings):
            elem = strings[j][i] - 1
            sorted_s[cnt[elem]] = strings[j]
            cnt[elem] += 1

        strings = sorted_s

    return strings


num_of_strings, lenght_of_strings, k = map(int, input().split())
strings = list()

for _ in range(num_of_strings):
    strings.append(reversed(list(str(input()))))

data_char2int(strings, num_of_strings)

strings = radix_sort(strings, num_of_strings, lenght_of_strings, k)

data_int2char(strings, num_of_strings)

for i in range(num_of_strings):
    print(*list(reversed(strings[i])), sep='')