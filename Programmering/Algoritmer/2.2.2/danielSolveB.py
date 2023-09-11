print("Hvilken figur?")
valg = int(input("Square = 1\nRectangle = 2\nTriangle = 3\n\n~$ "))

whitelist = [1, 2, 3]

def square(x):
    for i in range(x):
        for j in range(x):
            print("*", end="")
        print("")


def rectangle(x, y):
    for i in range(x):
        for j in range(y):
            print("*", end="")
        print("")


def triangle(x):
    for i in range(x + 1):
        for j in range(i):
            print("*", end="")
        print("")

if valg == 1: 
    x = int(input("x = "))
    print("\nHer er figuren din:")
    square(x)
elif valg == 2:
    x = int(input("x = "))
    y = int(input("y = "))
    rectangle(x, y)
elif valg == 3:
    x = int(input("x = "))
    triangle(x)
elif valg not in whitelist:
    print("\nVelg ett av disse tallene")
    for i in range(len(whitelist)):
        print(whitelist[i], end=" ")
    print("\n")