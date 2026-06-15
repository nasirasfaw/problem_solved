s = input()

nums = []
for i in range(len(s)):
    if i % 2 == 0:
        nums.append(int(s[i]))

nums.sort()
s2 = []
for i in nums:
    s2.append(str(i))
    
s3 = "+".join(s2)

print(s3)
