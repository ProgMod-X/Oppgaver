'''
Skriv kode for å skrive ut følgende skjermbilde, ved hjelp av én ytre løkke og to indre løkker.
Ikke bruk if…else.

#

-##

--###

---####

--###

-##

#
'''

n = 4  # Antall linjer i midten delen av mønsteret

# Øvre del av mønsteret


while True:
    for i in range(n):
        print('-' * i + '#' * (i + 1))
    
    for i in range(n - 2, -1, -1):
        print('-' * i + '#' * (i + 1))

    break

