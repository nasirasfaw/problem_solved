s = input()

if len(s) == 1 and s.islower():
    print(s.upper())
elif s[0].islower() and s[1:].isupper():
    print(s[0].upper()+s[1:].lower())
elif s.isupper():
    print(s.lower())
else:
    print(s)
