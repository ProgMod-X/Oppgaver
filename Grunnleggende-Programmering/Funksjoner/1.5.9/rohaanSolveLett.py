def potens(a ,b):
    sum = a
    if b == 0:
        return 1
    else:
        for i in range(b - 1):
            sum *= a
        return sum

print(potens(3, 0))