n, x, y = map(int, input().split())
left = 0
right = (n - 1) * max(x, y)
while left < right - 1:
    mid = int((left + right) / 2)
    if n - 1 > (mid // x + mid // y):
        left = mid
    else:
        right = mid
print(min(x, y) + right)