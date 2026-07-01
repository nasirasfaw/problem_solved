s1 = input()
s2 = input()
s = input()

s3 = s1 + s2

s3, s = sorted(s3), sorted(s)
if s3 == s:
    print("YES")
else:
    print("NO")
