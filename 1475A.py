#Checking whether an integer has an odd divisor greater than 1.
t = int(input())
 
for i in range(t):
    n = int(input())
 
    while n % 2 == 0:
        n //= 2
 
    if n > 1:
        print("YES")
    else:
        print("NO")
