minne = {}
n = 40

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def minnefibonacci(f):
    def inner(n):
        if n not in minne:
            minne[n] = f(n)
        return minne[n]
    return inner

@minnefibonacci
def mfibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return mfibonacci(n-1) + mfibonacci(n-2)

print("Med memoisering: ", mfibonacci(n))
print("Uten: ", fibonacci(n))
