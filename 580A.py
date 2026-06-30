n = int(input())
a = list(map(int, input().split()))

groups = []
start = 0
for i in range(1, len(a)):
    if a[i] < a[i-1]:
        groups.append(a[start:i])
        start = i
groups.append(a[start:])
maxm = max(len(x) for x in groups)
    
print(maxm)
