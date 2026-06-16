n = int(input())
 
lucky = []
for i in range(len(str(n))):
  if str(n)[i] == "4" or str(n)[i] == "7":
    lucky.append(i)
if len(lucky) == 4 or len(lucky) == 7:
  print("YES")
else:
  print("NO")
