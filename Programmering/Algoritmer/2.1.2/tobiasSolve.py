# For å finne ut om et punkt ligger utenfor, på, eller inni sirkelen, kan vi bruke vektorregning.
# For å gjøre dette finner vi lengden mellom x punktene (sirkel og punkt) og gjør det samme med y punktene.
# Deretter bruker vi pytagoras setning til å finne hypotenusen, altså lengden til sentrum.
# Hvis denne lengden er mindre enn radius (målt fra sentrum), vil punktet være innenfor sirkelen
# Hvis lengden er mer er den utenfor, og like mye som sentrum vil den være på sirkelen

cX = int(input("X-koordinat C: "))
cY = int(input("Y-koordinat C: "))
cR = int(input("Radius C: "))

pX = int(input("X-koordinat P: "))
pY = int(input("Y-koordinat P: "))

dist = ((pX-cX)**2 + (pY-cY)**2)**0.5

if dist < cR:
    print("Point is inside of the circle")
elif dist > cR:
    print("Point is outside of the circle")
else:
    print("Point is on the circle")