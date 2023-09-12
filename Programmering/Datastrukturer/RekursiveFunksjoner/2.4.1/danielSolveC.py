minne = {}
    
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

print(mfibonacci(40))
