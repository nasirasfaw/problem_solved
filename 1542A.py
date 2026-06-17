t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odds = 0
    evens = 0
    for k in a:
        if k % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    if odds == evens:
        print("YES")
    else:
        print("NO")
