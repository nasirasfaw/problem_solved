n, k = map(int, input().split())
ls = list(range(0, n+1))
c = 2*(240 - k)//5 
maxm = []
for m in ls:
    if m*(m+1) <= c:
        maxm.append(m)


print(max(maxm))
