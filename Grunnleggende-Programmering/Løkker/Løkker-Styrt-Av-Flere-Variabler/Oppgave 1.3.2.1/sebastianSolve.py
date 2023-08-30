'''
Lag et program som summerer tallene fra 0 opp til og med et valgt siffer.
'''

tall = int(input("Tall: "))

x = 0
total = 0

for x in range(0,tall):
    x += 1
    total += x
#    print(x)
print(total)