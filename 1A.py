m, n, a = map(int, input().split())
num_flagstones = ((m +a - 1) // a) * ((n +a - 1) // a)
print(num_flagstones) 
