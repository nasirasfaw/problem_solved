from math import ceil
n = int(input())
s = list(map(int, input().split()))

n1, n2, n3, n4 = s.count(1), s.count(2), s.count(3), s.count(4)

num_cars = 0

num_cars += n4

num_cars += n3

n1 = max(0, n1-n3)

num_cars += n2//2

if n2 % 2:
    num_cars += 1
    n1 = max(0, n1-2)

num_cars += ceil(n1/4)

print(num_cars)
