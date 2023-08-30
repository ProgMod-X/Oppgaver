'''
Bruk for-løkker til å skrive ut
tallene 1 til 15 horisontalt, med et mellomrom mellom tallene
tallene 1 til 15 vertikalt
oddetallene 1 til 15 horisontalt, med et mellomrom mellom tallene
Skriv om løkkene over til  while-løkker.
''' 

for x in range(1,16):
    print(x, end = " ")
    x += 1

for y in range(1,16):
    print(y)
    y += 1

for z in range(1,16):
    if z % 2 != 0:
        print(z, end = " ")

a = 1

while a in range(1,16):
    print(a, end = " ")
    a += 1

b = 1 

for b in range(1,16):
    print(b)
    b += 1
    
c = 1

for c in range(1,16):
    if c % 2 != 0:
        print(c, end = " ")