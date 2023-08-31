'''
C:
Bruk tre nøstede løkker til å finne alle tresifrete tall abc der summen av sifrene er lik produktet av sifrene.
'''

for x in range(0,10):
    for y in range(1,10):
        for i in range(0,11):
            if x*y*i==x+y+i:
                print(x*100+y*10+i, end = " ")