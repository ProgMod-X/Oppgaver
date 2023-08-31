def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fakultet = 1
        for i in range(2, n + 1):
            fakultet *= i
        return fakultet

print(factorial(3))
