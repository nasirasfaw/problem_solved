t = int(input())

for i in range(t):
    n = int(input())

    d = [int(j) for j in str(n)]
    rounds = []
    for i in range(len(d)):
        rounds.append(d[i]*10**(len(d)-1-i))

    rounds = [k for k in rounds if k != 0]
    print(len(rounds))
    print(*rounds)
