s = input()
w = "hello"
 
j = 0
for i in range(len(s)):
    if s[i] == w[j]:
        j += 1
        if j == len(w):
            break
 
if j == len(w):
    print("YES")
else:
    print("NO")
