s1, s2, s3, s4 = map(int, input().split())
s = set([s1, s2, s3, s4])

if len(s) == 4:
    print(0)
elif len(s) == 3:
    print(1)
elif len(s) == 2:
    print(2)
elif len(s) == 1:
    print(3)
