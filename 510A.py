n, m = list(map(int, input().split()))
mat = [[0]*m for _ in range(n)]
 
for i in range (0, n, 2):
    for j in range(m):
        mat[i][j] = "#"
for i in range(1, n, 2):
    for j in range(m-1):
        mat[i][j] = "."
        mat[i][m-1] = "#" 
for i in range(3, n, 4):
    mat[i].reverse()
for k in mat:
    print(*k, sep="")
