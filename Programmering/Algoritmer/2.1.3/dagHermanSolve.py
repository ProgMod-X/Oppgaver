from math import floor

def antallKvadraterIRektangel(lengde, bredde):
    kortestSide = min(lengde, bredde)
    lengsteSide = max(lengde, bredde)

    if lengsteSide % kortestSide == 0: # Hvis den lengste siden delt på den korteste er et heltall trenger vi ikke å fortsette
        antall = lengsteSide / kortestSide
        return antall
    else:
        nyLengde = kortestSide
        nyBredde = lengsteSide / kortestSide - floor(lengsteSide / kortestSide)
        
        smaaKvadrater = antallKvadraterIRektangel(nyLengde, nyBredde) ** 2

        antall = floor(lengsteSide / kortestSide) + smaaKvadrater
        return antall

a = antallKvadraterIRektangel(49, 21)
print(a)