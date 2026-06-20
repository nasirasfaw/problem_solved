a = int(input())
b = int(input())
c = int(input())

s1, s2 = a+b+c, a*b*c
s3, s4 = (a+b)*c, a+b*c
s5, s6 = a*(b+c), a*b+c

print(max(s1, s2, s3, s4, s5, s6))
