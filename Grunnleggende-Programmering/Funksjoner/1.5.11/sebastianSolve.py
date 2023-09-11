

def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


def binominal(n,k):
    x = (factorial(n))/((factorial(k)*factorial(n-k)) * factorial(n-k))
    return x

print(binominal(34,7))



