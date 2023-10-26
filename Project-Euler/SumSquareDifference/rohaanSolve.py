def sumOfSquares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i**2
    return sum

def squareOfSumOfNaturalNumbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum**2

print(squareOfSumOfNaturalNumbers(100) - sumOfSquares(100))