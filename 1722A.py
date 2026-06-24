t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    r = "Timur"
    if len(s) == len(r) and set(s) == set(r):
        print("YES")
    else:
        print("No") 
