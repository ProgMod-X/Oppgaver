'''
Lag en funksjon som returnerer «Fornavn Etternavn» (med mellomrom) når funksjonen får gitt 
fornavn og etternavn som to parametre. Kall funksjonen to_full_name.
'''



def to_full_name(fornavn, etternavn):
    return fornavn + " " + etternavn

fornavn, etternavn = str(input("fornavn: ")), str(input("etternavn: "))

print(to_full_name(fornavn, etternavn))