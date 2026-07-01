n = int(input())
a = list(map(int, input().split()))

ev = []
od = []
for i in range(n):
    if a[i] % 2 == 0:
        ev.append(a[i])
    else:
        od.append(a[i])
if len(ev) == 1:
    print(a.index(ev[0])+1)
else:
    print(a.index(od[0])+1)
