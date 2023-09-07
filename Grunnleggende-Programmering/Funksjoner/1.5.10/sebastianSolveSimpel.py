'''
Multiplikasjon introduseres ofte som gjentatt addisjon.

5 ⋅ 3 = 3 + 3 + 3 + 3 + 3 = 15

Når vi multipliserer kun to tall som over, har faktorene egne navn. Den venstre faktoren kalles multiplikand og den høyre multiplikator. Men, den kommutative lov sier at "faktorenes orden er likegyldig", og vi har dermed at 5 ⋅ 3 = 3 ⋅ 5 = 15.

Skriv et program som bruker en løkke og addisjon til å beregne produktet av to tall.
'''

def multipliser(multiplikand, multiplikator):
    svar   = 0
    teller = 0
    while teller < multiplikand:
        svar   += multiplikator
        teller += 1
        return svar

produkt = multipliser(3,5)
print(produkt)
