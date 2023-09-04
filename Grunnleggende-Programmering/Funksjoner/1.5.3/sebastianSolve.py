'''
Lag en funksjon som returnerer «Fornavn Etternavn» (med mellomrom) når funksjonen får gitt fornavn og etternavn som to parametre. Kall funksjonen toFullName.
'''

def toFullName(fornavn,etternavn):
    return fornavn + " " + etternavn

fornavn,etternavn = str(input("fornavn: ")), str(input("etternavn: ")) 

print(toFullName(fornavn,etternavn))
