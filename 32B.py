x = input()

x1 = []
i = 0
while i < len(x):
    if x[i] == ".":
        x1.append(".")
        i += 1
    else:
        x1.append(x[i:i+2])
        i += 2
y1 = []
for y in x1:
    if y == ".":
        y1.append("0")
    if y == "-.":
        y1.append("1")
    if y == "--":
        y1.append("2")
      
y1 = "".join(y1)
print(y1)
