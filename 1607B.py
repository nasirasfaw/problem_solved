t = int(input())

for i in range(t):
    x0, n = map(int, input().split())

    p = 0
    k = n+1
    if n in range(0, k, 4): 
        p += x0
    while  x0%2 == 0:
        if n in range(2, k, 4):
            p += x0+1
        elif n in range(1, k, 4):
            p += x0-n
        elif n in range(3, k, 4):
            p += x0+n+1
        break
        
    while  x0%2 != 0:
        if n in range(2, k, 4):
            p += x0-1
        elif n in range(1, k, 4):
            p += x0+n
        elif n in range(3, k, 4):
            p += x0-(n+1)
        break

    print(p)
