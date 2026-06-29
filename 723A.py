x1, x2, x3 = map(int, input().split())
 
x = [x1, x2, x3]
x.sort()
 
total = (x[1]-x[0]) + (x[2]-x[1])
 
print(total)
