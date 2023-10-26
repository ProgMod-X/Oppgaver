factorials = {
    0: 1,
    1: 1
}

def mfibonacci(n):
    if n in factorials:
        return factorials[n]
    
    else:
        result = mfibonacci(n-1) + mfibonacci(n-2)
        factorials[n] = result
        return result