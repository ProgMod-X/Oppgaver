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


function = int(input("Hvilken funksjon vil du benytte?\nsquare(0), rectangle(1), triangle(2): "))

if function == 0:
    x = int(input("Hva er x? "))
    square(x)
elif function == 1:
    x = int(input("Hva er x? "))
    y = int(input("Hva er y? "))
    rectangle(x, y)
elif function == 2:
    x = int(input("Hva er x? "))
    triangle(x)