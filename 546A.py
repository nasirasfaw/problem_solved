k, n, w = map(int, input().split())

b = w*(w+1)//2

x = k*b - n 

if x > 0:
    print(x)
else:
    print(0)
