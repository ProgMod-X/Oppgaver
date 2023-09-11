'''
Skriv en funksjon factorial(n) som beregner og returnerer n! basert på logikken over.

Test funksjonen din med ulike verdier for n og sammenlign med svaret du får i CAS.
'''

n = int(input())

def factorial(n):
    m = 1
    while n > 0:
        m *= n
        n -= 1
    return m

print(factorial(n))