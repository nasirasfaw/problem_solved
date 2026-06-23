t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sor = sorted(a)
    s1, s2 = set(sor[1:]), set(sor[:-1])

    if len(s1) < len(s2):
        target = sor[0]
    else:
        target = sor[-1]
    print(a.index(target)+1)
 
