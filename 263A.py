a= list(map(int, input().split()))
b= list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split())) 
e = list(map(int, input().split()))

m = [a, b, c, d, e]

for i in range(5):
    for j in range(5):
        if m[i][j] == 1:
            num_steps = abs(i-2) + abs(j-2) 

print(num_steps)
