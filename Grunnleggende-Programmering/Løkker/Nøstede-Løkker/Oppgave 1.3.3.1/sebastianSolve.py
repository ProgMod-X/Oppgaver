'''
Skriv et program som bruker nøstede løkker til å vise følgende mønster:

**********
*********
********
*******
******
*****
****
***
**
*
'''



antall = 10


while antall >= 0:
    for x in range(1,10):
        print("*"*antall)
        
        antall -= 1
        
