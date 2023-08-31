def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


def binomialkoeffisienten(n, k):
    return (factorial(n))/(factorial(k) * factorial(n-k))

print(binomialkoeffisienten(15, 5))