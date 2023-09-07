def potens(grunntall, eksponent):
    svar = 1
    for i in range(0,eksponent):
        svar *=grunntall
    return svar 
        

print(potens(4,5))