def minst(x0, x1):
    if x0 < x1:
        return x0
    else:
        return x1


def stoerst(x0, x1):
    if x0 > x1:
        return x0
    else:
        return x1
    
print(minst(4, 2))
print(stoerst(2, 4))