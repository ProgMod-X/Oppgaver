import time

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
start = time.time()

print(fibonacci(40))

end = time.time()

print(f"Time to run: {end - start}")