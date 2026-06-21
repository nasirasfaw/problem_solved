t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    num_moves = 0
    neg = []
    zeros = []
    for k in a:
        if k == -1:
            neg.append(k)
        if k == 0:
            zeros.append(k)

    if len(neg) % 2 == 0:
        num_moves += len(zeros)
    elif len(neg) % 2 != 0:
        num_moves += len(zeros) + 2

    print(num_moves)
