def square(x):
    for i in range(x):
        for j in range(x):
            print("*", end="")
        print("\n")


def rectangle(x, y):
    for i in range(x):
        for j in range(y):
            print("*", end="")
        print("\n")


def triangle(x):
    for i in range(x + 1):
        for j in range(i):
            print("*", end="")
        print("\n")
