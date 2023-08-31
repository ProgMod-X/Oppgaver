'''
B:
Bruk tre nøstede løkker til å skrive ut alle tresifrede tall
'''


for x in range(0,10):
    for y in range(1,10):
        for i in range(0,11):
            print(x*100+y*10+i, end = " ")