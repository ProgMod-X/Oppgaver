def multiplikasering(multiplikand, multiplikator):
    svar = 0
    teller = 0
    
    while teller < multiplikand:
       svar   += multiplikator
       teller += 1
       return svar
    
produkt = multiplikasering(3, 5)
print(produkt)
