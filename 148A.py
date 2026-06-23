k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
 
count = 0
 
for i in range(1, d+1):
    if any(i % j == 0 for j in [k, l, m, n]):
        count += 1
print(count)
