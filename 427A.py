n = int(input())
a = list(map(int, input().split()))

officers = 0
untreated = 0

for i in range(len(a)):
    if a[i] > 0:
        officers += a[i]
    elif a[i] == -1:
        if officers > 0:
            officers -= 1
        else:
            untreated += 1
print(untreated)
