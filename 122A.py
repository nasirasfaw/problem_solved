n = int(input())

lucky = []

for k in range(1, n+1):
    if all(str(k)[i] == "4" or str(k)[i] == "7" for i in range(len(str(k)))):
            lucky.append(k)

if any(n % k == 0 for k in lucky):
    print("YES")
else:
    print("NO")
