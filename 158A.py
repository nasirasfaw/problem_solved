n, k = map(int, input().split())
c = list(map(int, input().split()))
c.sort()
counts = 0
for i in range(len(c)):
    if c[i] > 0 and c[i] >= c[n-k]:
        counts += 1
print(counts)
