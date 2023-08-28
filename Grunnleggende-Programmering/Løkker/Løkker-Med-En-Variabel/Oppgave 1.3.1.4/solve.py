# For-løkker

# 1-15 horisontalt
for i in range(1, 16):
    # Bruker end=" " for å gjøre de til horisontale
    print(i, end=" ")
# Printer bare ny linje når ferdig i rekke
print()

# 1-15 vertikalt
for i in range(1, 16):
    print(i)

# 1-15 bare i oddetall
for i in range(1, 16, 2): # Bruker ", 2" for å hoppe over annen hver
    # Formaterer til horisontalt
    print(i, end=" ")
# Printer bare ny linje når ferdig i rekke
print()


# While løkker

# 1-15 horisontalt
i = 1
while i <= 15:
    # Bruker end=" " for å gjøre de til horisontale
    print(i, end=" ")
    i += 1
# Printer bare ny linje når ferdig i rekke
print()

# 1-15 vertikalt
i = 1
while i <= 15:
    print(i)
    i += 1

# 1-15 bare i oddetall
i = 1
while i <= 15:
    # Bruker modulus for å se når tallet IKKE går opp med å dele det på 2
    if i % 2 != 0:
        # Bruker end=" " for å gjøre de til horisontale
        print(i, end=" ")
    i += 1
# Printer bare ny linje når ferdig i rekke
print()

