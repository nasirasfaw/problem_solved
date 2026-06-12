n = int(input())
sum_x = 0
sum_y = 0
sum_z = 0
for i in range(n):
    xi, yi, zi = map(int, input().split())
    sum_x +=xi
    sum_y += yi
    sum_z += zi
if sum_x == 0 and sum_y == 0 and sum_z == 0:
    print("YES")
else: 
    print("NO")
