t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    best = 0
    current = 0
    for x in a:
        if x == 0:
            current += 1
            best = max(best, current)
        else: 
            current = 0 
    print(best)
