n, l = map(int, input().split())
a = list(map(int, input().split()))
 
a.sort()
d = max(a[0], l-a[-1])
 
for i in range(n-1):
    d = max(d, (a[i+1]-a[i])/2)
 
print(round(d, 10))
