def n(a):
    if ((a - 3) % 5) != 0:
        return (f"{a} er ikke i følgen")
        
    else:
        return (a-3)/5 + 1
    
print(n(503))