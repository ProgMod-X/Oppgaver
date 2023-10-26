def a(n):
    if n == 1:
        return 0.5
    else:
        return a(n-1)*0.5
