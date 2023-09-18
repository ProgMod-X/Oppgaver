def s(n):
    k = 1/2
    if n == 1:
        return 1/2
    else:
        return 1/2 * ((k**n - 1)/(k - 1))
    
print(s(100))