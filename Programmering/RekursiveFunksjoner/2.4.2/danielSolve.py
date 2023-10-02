def a(n):
    if n > 0:
        result = n + a(n-1)
        print(result)
    else: 
        result = 0
    return result

a(5)
