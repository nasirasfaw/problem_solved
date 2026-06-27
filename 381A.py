n = int(input())
a = list(map(int, input().split()))

sereja = dima = 0
i, j = 0, n-1
turn = 0
while i <= j:
    if a[i] >= a[j]:
        x = a[i]
        i += 1
    else:
        x = a[j]
        j -= 1
    if turn == 0:
        sereja += x
    else:
        dima += x
    turn ^= 1
print(sereja, dima)
