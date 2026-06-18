n = int(input())
 
current = 0
maxs = []
for i in range(n):
  a, b = map(int, input().split())
  maximum = current - a + b
  maxs.append(maximum)
  current -= a
  current += b
print(max(maxs))
