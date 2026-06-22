t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    if a < max(b, c) and a > min(b, c):
        print(a)
    if b < max(a, c) and b > min(a, c):
        print(b)
    if c < max(a, b) and c > min(a, b):
        print(c)
