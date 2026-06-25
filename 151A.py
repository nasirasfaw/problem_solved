n, k, l, c, d, p, nl, np = map(int, input().split())

drinks = (k*l)//nl 
lime = (c*d)
salt = p//np

max_no_toasts = min(drinks, lime, salt)//n

print(max_no_toasts)
