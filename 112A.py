str1 = input()
str2 = input()

if str1.lower() == str2.lower():
    size = 0
elif str1.lower() < str2.lower():
    size = -1
else:
    size = 1
    
print(size)
