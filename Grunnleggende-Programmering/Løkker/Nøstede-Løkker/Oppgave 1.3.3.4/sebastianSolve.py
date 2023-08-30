'''
Skriv et program som viser følgende mønster:

12345

22345

33345

44445

55555
'''

for i in range(1, 6):
    for j in range(1, 6):
        if i <= j:
            print(j, end="")
        else:
            print(i, end="")
    print()
    