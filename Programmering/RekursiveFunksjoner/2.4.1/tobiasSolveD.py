import time

fibonaccis = {
    0: 0,
    1: 1
}

def mfibonacci(n):
    if n in fibonaccis:
        return fibonaccis[n]
    
    else:
        result = mfibonacci(n-1) + mfibonacci(n-2)
        fibonaccis[n] = result
        return result

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

start = time.time()
print(fibonacci(100))
end = time.time()
print(f"Time to run: {end-start}")

start = time.time()
print(mfibonacci(100))
end = time.time()
print(f"Time to run: {end-start}")