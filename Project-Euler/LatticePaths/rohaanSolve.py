def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum

def binomialCoefficient(n, k):
    return (factorial(n))/((factorial(n - k)) * factorial(k))

print(int(binomialCoefficient(40, 20)))