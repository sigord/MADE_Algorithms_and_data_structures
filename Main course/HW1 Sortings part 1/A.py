inter = int(input())
a = list(map(int, input().split()))
 
def insertion_sort(a):
    for i in range(inter):
        j = i
        while j>0 and a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1
 
insertion_sort(a)
print(*a, sep=' ')