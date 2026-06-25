t = int(input())
 
for i in range(t):
  n = int(input())
  a = list(map(int, input().split()))
    
  a.sort()
 
  b = []
  for i in range(len(a)):
    if abs(a[i]-a[i-1]) <= 1:
      b.append(a[i-1])
  if abs(len(a)-len(b)) <= 1:
    print("YES")
  else:
    print("NO")
