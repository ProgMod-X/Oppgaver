# Forskjellen på en while-løkke og en for-løkke er at en while løkke har en utvendig variabel som den sjekker frem til 
# et spesifikt condition er møtt. 
# I motsetning til en while-løkke, har en for-løkke en innebygd variabel som den automatisk vil gå gjennom

# Her er en basic while-løkke som teller til 10
i = 1

while i <= 10:
    print(i)
    i += 1
    
print("------------------------------")    
# Med en for-løkke kan vi gjøre dette med en innebygd variabel

for i in range(11): # Merk at "in range" er eksklusiv, og inkluderer ikke det siste tallet, altså fungerer denne koden som "while i < 11:"
    print(i)

print("------------------------------")  
# I tillegg til å telle med en for-løkke, kan vi også gå gjennom en liste.

# Her er en basic while-løkke som går gjennom en liste
list = ["Dette", "er", "en", "liste"]
current_index = 0

while current_index < len(list):
    print(list[current_index])
    current_index += 1
    
print("------------------------------")
# Her er en basic for-løkke som går gjennom en liste
list = ["Dette", "er", "en", "liste"]

for i in list:
    print(i)
    
print("------------------------------")  

# Som man kan se, kan en for-løkke betydelig forkorte et program hvor man skal telle eller gå gjennom en liste. 
# Dette hjelper oss å holde programmet simpelt, slik at det er lett å forstå.