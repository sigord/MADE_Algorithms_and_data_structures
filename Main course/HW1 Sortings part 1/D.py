import random

def quicksort(a, start, end):
    if (start < 0 or start >= end):
        return
    
    pivot = a[random.randint(start, end-1)]
    lp = start
    rp = end
    while lp <= rp:
        while a[lp] < pivot:
            lp += 1

        while pivot < a[rp]:
            rp -= 1
        
        if (lp <= rp):
            a[lp], a[rp] = a[rp], a[lp]
            lp += 1
            rp -= 1

    quicksort(a, start, lp-1)
    quicksort(a, lp, end)

inter = int(input())
a = list(map(int, input().split()))
quicksort(a, 0, len(a)-1)
print(*a, sep=' ')