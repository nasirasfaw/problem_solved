w = input()

c = 0
s = 0
for i in range(len(w)):
    if w[i] == w[i].upper():
        c += 1
    elif w[i] == w[i].lower():
        s += 1
if c > s:
    print(w.upper())
elif c < s:
    print(w.lower())
elif c == s:
    print(w.lower())
