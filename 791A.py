import math
a, b = map(int, input().split())

x = (math.log(b/a))//(math.log(3/2))

print(int(x+1))
