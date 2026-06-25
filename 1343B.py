t = int(input())

for _ in range(t):
  n = int(input())
  a = list(range(2, n+1, 2))
  b = list(range(1, n-1, 2))+ [(3*n-2)//2]
  m = a+b
  
  if n % 4 == 0:
    print("YES \n", *m)
  else:
    print("NO")
