def factorial(n):
    tot = 1
    for i in range(1,n+1):

        tot*=i

    return tot 
print(factorial(3))