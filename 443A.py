s = input()
 
letts = set()
 
for ch in s:
    if ch.isalpha():
        letts.add(ch)
 
print(len(letts))
