t = int(input())

for i in range(t):
    n = int(input())
    eff = list(map(int, input().split()))
    sum_eff = sum(eff[:])

    eff_miss = -sum_eff

    print(eff_miss)

#Fot two teams x_1 and x_2, if x_1 scores y_1 goals and x_2 scores y_2 scores, then 
# efficiency of x_1, e_1 = y_1 - y_2 wheras e_2 = y_2 - y_1 so that their total eff, e_1 + e_2 = 0.
#Similarly, for n teams, the total eff: e_1 + e_2 + e_3 + ... + e_n = 0.
#Therefore, if eff of all the n-1 teams are given, eff of the missing one team can be obtained.
