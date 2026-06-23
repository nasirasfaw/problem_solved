n = int(input())
 
n_bills = 0
 
for d in [100, 20, 10, 5, 1]:
    n_bills += n//d
    n %= d
 
print(n_bills)
