mem = {0: 0, 1: 1}

def mfibonacci(n):
    if n in mem:
        return mem[n]
    else:
        mem[n] = mfibonacci(n - 1) + mfibonacci(n - 2)
        return mem[n]

print(mfibonacci(40))