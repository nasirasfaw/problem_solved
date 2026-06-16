s = input()
t = input()
rev = True
for i in range(len(s)):
    if t[i] != s[-1-i] or len(t) != len(s):
        rev = False
        break
 
if rev:
    print("YES")
else:
    print("NO")
