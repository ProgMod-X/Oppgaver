def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print("")
    print("---------------------------")
        
def rectangle(x, y):
    for i in range(y):
        for j in range(x):
            print("*", end="")
        print("")
    print("---------------------------")
        
def triangle(n):
    for i in range(n + 1):
        for j in range(i):
            print("*", end="")
        print("")
    print("---------------------------")

    
square(int(input("Square size: ")))
rectangle(int(input("Rectangle x: ")), int(input("Rectangle y: ")))
triangle(int(input("Triangle size: ")))
