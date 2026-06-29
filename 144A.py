n = int(input())
a = list(map(int, input().split()))

mx, mn = max(a), min(a)
i1, i2 = a.index(mx), a.index(mn)
i3 = len(a)-1 - a[::-1].index(mn)
count = i1 + len(a)-1-i3
if i3 < i1:
    count -= 1
print(count)
