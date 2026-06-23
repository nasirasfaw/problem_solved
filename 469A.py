n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
k = list(range(1, n+1))

if set(p[1:]) | set(q[1:]) == set(k): #Union of the two sets
    result = "I become the guy."
else:
    result = "Oh, my keyboard!"

print(result)
