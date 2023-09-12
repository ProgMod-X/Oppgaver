'''
hvis lengden er for eksempel 12 og bredden er 18
så tar vi den korteste siden
deretter subtraherer vi den lengste siden med den korteste siden
dette, visuelt sett, lager kvadratene. Deretter blir kvadratene mindre og mindre
'''

a = 12
b = 18

while True:
    if a == b:
        break
    elif a < b:
        b -= a
    elif a > b:
        a -=b

print(a)