'''
Lag en funksjon som kalkulerer kilojoule energi i mat etter følgende formel.
E = 17⋅P + 38⋅F + 17⋅C

P = protein, F = fett, C = karbohydrater
'''

def kilojoule(P,F,C):
    return 17*P + 38*F + 17*C

