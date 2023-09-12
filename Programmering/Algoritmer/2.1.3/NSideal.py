'''
Først finner vi gcd til de to tallene, dette vil si den største felles faktor.
Eks. (12, 18). 12 = 2 * 2 * 3, 18 = 2 * 3 * 3, disse to tallene vil ha en felles faktor på 6. 
12 = 6 * 2, 18 = 6 * 3
'''
import math
a = 27
b = 15

def gcd(a, b):
    math.gcd(a, b)
    return a, b

print(math.gcd(a, b))
