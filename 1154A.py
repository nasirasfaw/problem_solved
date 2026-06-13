nums = list(map(int, input().split()))

nums.sort()

a = nums[-1] - nums[0]
b = nums[-1] - nums[1]
c = nums[-1] - nums[2]

print(a, b, c)

#Random four numbers: x1, x2, x3, x4 that correspond to a+b, a+c, b+c and a+b+c.
#The largest is a+b+c, and note that a=(a+b+c)-(b+c), b=(a+b+c)-(a+c) and c=(a+b+c)-(a+b).
#Take list [x1, x2, x3, x4] and sort it so that x4 is maximum (i.e x4=a+b+c). Then, a=x4-x3, b=x4-x2 and c=x4-x1
