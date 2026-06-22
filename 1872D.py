from math import gcd
t = int(input())

for t in range(t):
    n, x, y = map(int, input().split())
    
    d = gcd(x, y)
    m = x*y//gcd(x, y)
    p = n//x - n//m
    q = n//y - n//m

    px = p*(2*n-p+1)//2
    py = q*(q+1)//2

    print(px - py)
