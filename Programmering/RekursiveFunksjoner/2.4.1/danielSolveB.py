def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

svar = fibonacci(40)

print(svar)

'''
time python3 danielSolveB.py

102334155

real    0m12.384s
user    0m12.363s
sys     0m0.000s
'''