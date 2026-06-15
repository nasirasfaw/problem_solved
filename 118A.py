s = input()

v = ['a', 'e', 'i', 'o', 'u', 'y']

s1 = []
for i in range(len(s)):
    if s[i].lower() not in v:
        s1.append(s[i])

s1 = ".".join(s1)

print("." + s1.lower())
