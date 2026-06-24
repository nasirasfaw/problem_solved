from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
                            # a[j]-a[i] = j-i is the same as a[i]-i = a[j]-j
    freq = defaultdict(int)  # If a single num occurs k times in [a[i]-i], then C(k, 2) pairs of the (i, j) 

    count = 0
    for i in range(len(a)):
        d = a[i]-i
        count += freq[d]
        freq[d] += 1
        
    print(count)
