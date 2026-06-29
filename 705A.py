n = int(input())

a = ["I hate"]
for i in range(1, n):
    if i%2 != 0:
        a.append("that I love")
    else:
        a.append("that I hate")

speech = " ".join(a)
    
print(f"{speech} it")
