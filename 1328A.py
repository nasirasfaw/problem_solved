t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a > b and a % b != 0:
        print(b - (a % b))
    elif a >= b and a % b == 0:
        print(0)
    elif a < b:
        print(b - a)
