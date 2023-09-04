a = float(input("Hva er a? "))
b = float(input("Hva er b? "))
square = 0

def mk(a, b):
    if a >= b:
        c = b
    else:
        c = a

    kvadrat = c**2
    
    if (a * b) % kvadrat == 0:
        global square
        square = kvadrat
        return
    else:
        if c == a:
            mk(c, (b % c))
        else:
            mk(c, (a % c))

mk(a, b)
print(f"Størst mulig kvadrat med {a} * {b} = {square}")
