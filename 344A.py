n = int(input())
chars = []
for i in range(n):
    chars.append(input())
 
counts = 1
 
for i in range(n-1):
    if chars[i] != chars[i+1]:
        counts += 1 
print(counts)
