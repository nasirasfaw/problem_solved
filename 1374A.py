t = int(input())

for i in range(t):
  x, y, n = map(int, input().split())

  max_r = y + ((n-y)//x) * x

  print(max_r)
