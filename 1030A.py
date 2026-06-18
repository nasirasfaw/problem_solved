n = int(input())
 
b = list(map(int, input().split()))
 
if any(b[k] == 1 for k in range(n)):
    print("HARD")
else:
    print("EASY")
