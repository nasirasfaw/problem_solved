n = int(input())
 
m = list(map(int, input().split()))
 
for i in range(len(m)):
    m[i] = abs(m[i])
    
m.sort()
 
print(m[0])
