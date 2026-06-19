n = int(input())
 
k = n//2
 
if n % 2 == 0:
  f = k*(k+1) - k**2
else:
  f = k*(k+1) - (k+1)**2
 
print(f)
