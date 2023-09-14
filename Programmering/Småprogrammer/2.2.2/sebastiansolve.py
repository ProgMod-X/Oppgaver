

def square(a):
    for x in range(a):
        print("\t","*"*a)

    return 



def rectangle(b,c):
    for x in range(b):
        print("\t ","*"*c)
    return 




'''
def rtriangle(d):
    x = 0
    while x <= d:
        print("*"*x)
        x += 1
    return 
'''

def circle(e):
    for i in range(-e,e+1):
        for j in range(-e,e+1):
            if i ** 2 + j ** 2 <= e**2:
                print("*", end = " ")
            else:
                print(" ", end=" ")

        print() 
    return






#trekant = int(input("Hvor stor vil du at trekanten skal være? "))
#kvadratet = int(input("Hvor stor vil du at kvadratet skal være? "))
#rektangel1,rektangel2 = int(input("Hvor lang vil du at den ene siden av rektangelet skal være? ")), int(input("Hvor stor vil du at den andre siden av rektangelet skal være? "))
#sirkel = int(input("Hvor stor vil du at sirkelen skal være? "))
#pyramide = int(input("pyramide: ")) 
'''
print(f"{rtriangle(trekant)}\{square(kvadratet)}\n\n\n{rectangle(rektangel1,rektangel2)}\n\n\n{circle(sirkel)}")
'''



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
