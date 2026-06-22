t = int(input())
 
for i in range(t):
  a, b, k = map(int, input().split())
  p = 0
  if k % 2 == 0:
      p += (a-b)*k//2
  else:
      p += (a-b)*(k-1)//2 + a
 
  print(p)
