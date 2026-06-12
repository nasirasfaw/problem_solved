import math
t = int(input())
for i in range(t):
    n= int(input())
    num_ways = math.ceil(n/2-1)
    print(num_ways)
