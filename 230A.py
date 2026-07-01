s, n = map(int, input().split())
db = []
for _ in range(n):
    x, y = map(int, input().split())
    db.append([x, y])
db.sort()
st = s
i = 0
while i < n:
    if st > db[i][0]:
        st += db[i][1]
        i += 1
    else:
        break
if st > db[n-1][0]:
    print("YES")
else:
    print("NO")
