
def square(a):
    for x in range(a):
        print("*"*a)
        "\n"
    return 



def rectangle(b,c):
    for x in range(b):
        print("*"*c)
        "\n"
    return 





def rtriangle(d):
    x = 0
    while x <= d:
        print("*"*x)
        x += 1
    return 


def circle(e):
    for i in range(-e,e+1):
        for j in range(-e,e+1):
            if i ** 2 + j ** 2 <= e**2:
                print("*", end = " ")
            else:
                print(" ", end=" ")
        print() 
    return



'''
Lag et program som bruker funksjonene du laget. Brukeren skal kunne velge størrelse på de ulike figurene.
Forsøk å utvide programmet ditt med andre figurer (som brukeren kan bestemme størrelsen på)
'''

trekant = int(input("Hvor stor vil du at trekanten skal være? "))
kvadratet = int(input("Hvor stor vil du at kvadratet skal være? "))
rektangel1,rektangel2 = int(input("Hvor lang vil du at den ene siden av rektangelet skal være? ")), int(input("Hvor stor vil du at den andre siden av rektangelet skal være? "))
sirkel = int(input("Hvor stor vil du at sirkelen skal være? "))

print(f"{rtriangle(trekant)}\n\n\n{square(kvadratet)}\n\n\n{rectangle(rektangel1,rektangel2)}\n\n\n{circle(sirkel)}")
