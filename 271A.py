n = int(input())

years = []
for i in range(1000, 9020):
    if i > n and len(set(str(i))) == 4:
        years.append(i)
print(years[0])
