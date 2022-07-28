a = list(map(int, input().split()))

cnt = [0]*(max(a)+1)

for i in range(len(a)):
    cnt[a[i]] += 1

i = 0
for j in range(len(cnt)):
    while cnt[j] > 0:
        a[i] = j
        i += 1
        cnt[j] -= 1

print(*a, sep=' ')