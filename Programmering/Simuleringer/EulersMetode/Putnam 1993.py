def f(x):
    return (2*x - 3*x**3)

dx = 0.001
x = 0
b = (2/3)**0.5
c = 0.0001
diff = []
clist = []

while c < (1/3)**0.5:
    sum1 = 0
    sum2 = 0
    x = 0
    
    while f(x) < c:
        y = c - f(x)
        sum1 += y*dx
        x += dx
    while f(x) > c:
        sum2 += (f(x) - c)*dx
        x += dx
        
    diff.append(abs(sum2 - sum1))
    clist.append(c)
    c += 0.0001
    
print(clist[diff.index(min(diff))])