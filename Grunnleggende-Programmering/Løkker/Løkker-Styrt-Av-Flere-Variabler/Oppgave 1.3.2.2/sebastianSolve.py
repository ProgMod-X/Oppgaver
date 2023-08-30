'''

Lag et program som multipliserer tallene fra 1 opp til og med et valgt siffer.
''' 

tall = int(input("Tall: "))

x = 1
total = 1

for x in range(0,tall):
    x += 1
    total *= x
#    print(x)
print(total)