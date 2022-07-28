# def swap(a, x, y):
#     temp = a[x]
#     a[x] = a[y]
#     a[y] = temp

# def ceil(num):
#     i = (-1 if num<0 else 1)
#     return int(i*(-(-(num*i)//1)))

def mid(some_list):
    return int(len(some_list)/2)

def merge_sort(a):
    
    if len(a) == 1:
        return a
    
    l = merge_sort(a[:mid(a)])
    r = merge_sort(a[mid(a):])
    return merge(l,r)

def merge(a, b):
    len_a, len_b = len(a), len(b)
    i, j = 0, 0
    c = [None] * (len_a + len_b)
    while (i + j) < (len_a + len_b):
        if j == len_b or (i < len_a and a[i] < b[j]):
            c[i+j] = a[i]
            i += 1
        else:
            c[i+j] = b[j]
            j += 1
    return c

inter = int(input())
a = list(map(int, input().split()))

print(*merge_sort(a), sep=' ')