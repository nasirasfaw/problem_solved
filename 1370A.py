# Among all pairs of distinct numbers (k, m), 1 <= k, m <= n, the pair with maximum gcd is
# either gcd(n, n//2) = n//2 or gcd(n-1, (n-1)//2) = (n-1)//2
t = int(input())
for _ in range(t):
    n = int(input())
    if n%2 == 0:
        maxm = n//2 
    else:
        maxm = (n-1)//2
    print(maxm)
