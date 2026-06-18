t= int(input())
 
for i in range(t):
  a, b = map(int, input().split())
  
  d = abs(b-a)
  if d % 10 == 0:
    count = d//10        # count is number of steps to make a == b
  else:
    count = d//10 + 1 
 
  print(count)
