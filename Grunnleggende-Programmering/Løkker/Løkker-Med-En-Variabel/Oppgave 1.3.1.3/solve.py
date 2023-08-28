"""
Forskjellen mellom en for-løkke og en while løkke er at en while løkke gjør noe imens en condition er sant, men en for løkke gjør noe når den er det

En while løkke kan kjøres for evig med True og en for løkke kan itterere lettere gjennom en liste med tall helt til den blir ferdig    
    
"""

# Definerer en range og slutter når den møter den
for i in range(1, 10):
    print(i)
    
print("\n\n")

# Nå deklarerer vi heller en variablel til 1
j = 1

# Også tar vi den til "evig" helt til <= kondisjonen er møtt
while j <= 10:
    print(j)
    j += 1
    