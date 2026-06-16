n = int(input())
s = input()
a = 0
d = 0
for i in range(n):
    if s[i] == "A":
        a += 1
    elif s[i] == "D":
        d += 1

if a == d:
    print("Friendship")
elif a > d:
    print("Anton")
else:
    print("Danik")
