n1 = input()
n2 = input()

n3 = ""
for i in range(len(n1)):
    if n1[i] != n2[i]:
        n3 += "1"
    else:
        n3 += "0"

print(n3)
