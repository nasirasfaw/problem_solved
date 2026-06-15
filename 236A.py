name = input()

l_name = []

for i in range(len(name)):
    l_name.append(name[i])
    s_name = set(l_name)

if len(s_name) % 2 == 0:
        print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
