



def square(sidelengde):
    streng = ""
    for rad in range(1,sidelengde+1):
        for kolonne in range(1,sidelengde+1):
            streng += "*"
        streng += "\n"
        

    return streng
print(square(8))



def rectangle(sidelengde,toplengde):
    streng = ""
    for rad in range(1,sidelengde+1):
        for kolonne in range(1,toplengde+1):
            streng += "*"
        streng += "\n"
    return streng

print(rectangle(4,5))


def rtriangle(d):
    streng = ""
    for i in range(1,d+1):
            streng += "*"*i
            streng += "\n"

    return streng





#trekant = int(input("Hvor stor vil du at trekanten skal være? "))
#kvadratet = int(input("Hvor stor vil du at kvadratet skal være? "))
#rektangel1,rektangel2 = int(input("Hvor lang vil du at den ene siden av rektangelet skal være? ")), int(input("Hvor stor vil du at den andre siden av rektangelet skal være? "))
#sirkel = int(input("Hvor stor vil du at sirkelen skal være? "))
#pyramide = int(input("pyramide: ")) 



def pyramid(høyde):
    bredde = (2 * høyde) - 1  
    for i in range(1, høyde + 1):
        stjerner = 2 * i - 1
        mellomrom = (bredde - stjerner) // 2
        rad = " " * mellomrom + "*" * stjerner + " " * mellomrom
        print("\t",rad)
    return " "

print(f"{pyramid(6)}{square(11)}{rectangle(6,9)}{circle(5)}{circle(5)}{circle(5)}{circle(5)}")
#print(f"{pyramid(pyramide)}{square(kvadratet)}{rectangle(rektangel1,rektangel2)}")
#{rectangle(rektangel1,rektangel2)}\n\n\n\n{circle(sirkel)}\n\n{circle(sirkel)}\n\n{circle(sirkel)}\n\n{circle(sirkel)}")
