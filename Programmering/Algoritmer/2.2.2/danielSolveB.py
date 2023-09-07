x = int(input("Hvor stor vil du at figuren skal være?: "))


def square(x):
    for i in range(x):
        for j in range(x):
            print("*", end=" ")
        print("\n", end="")


def rectangle(x):
    pass


def triangle(x):
    pass

print("Her er figurene dine:")
print(square(x), "\n")
print(rectangle(x), "\n")
print(triangle(x), "\n")