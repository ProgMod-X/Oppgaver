import math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = a*b/lcm(a, b)

print(f"The Least Common Multiple of {a} and {b} is {result}")