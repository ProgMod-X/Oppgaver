def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print("\n")
        
def rectangle(x, y):
    for i in range(y):
        for j in range(x):
            print("*", end="")
        print("\n")
        
def triangle(n):
    for i in range(n + 1):
        for j in range(i):
            print("*", end="")
        print("\n")
        
square(3)
rectangle(4,2)
triangle(6)