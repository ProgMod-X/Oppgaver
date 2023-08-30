'''
Skriv kode for å skrive ut følgende skjermbilde.

#

-##

--###

---####

----#####

-----######

------
#######

'''

linjer = 6
hash = 1
strek = 0

for x in range(1,7):
    print("-"*strek, "#"*hash)
    hash += 1
    strek += 1

print("-"*5)
print("#"*5)