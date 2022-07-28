def mid(some_list):
    return int(len(some_list)/2)

def merge_sort_with_inv(a):
    
    if len(a) == 1:
        return a, 0
    
    l, l_count = merge_sort_with_inv(a[:mid(a)])
    r, r_count = merge_sort_with_inv(a[mid(a):])
    
    lr_merged, count = merge(l,r)
    count += (l_count + r_count)

    return lr_merged, count

def merge(a, b):
    len_a, len_b = len(a), len(b)
    i, j = 0, 0
    inv_count = 0
    c = list()
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inv_count += len(a) - i
    c += a[i:]
    c += b[j:]
    return c, inv_count

inter = int(input())
a = list(map(int, input().split()))

sorted_a, invertions = merge_sort_with_inv(a)
#print(*sorted_a, sep=' ')
print(invertions)