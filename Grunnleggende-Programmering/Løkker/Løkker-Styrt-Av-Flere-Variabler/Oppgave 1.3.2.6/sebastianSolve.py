'''
På en øy har det brutt ut en sykdom i rottepopulasjonen. Det er per i dag 20000 rotter på øya, men populasjonen minker med 10% hvert år.

A) Hvor mange rotter er det på øye om 3 år?

B) Hvor mange år tar det før rottepopulasjonen er halvert?
'''

start_antall = 20000 
endring = 0.9
år = 3

#A) 

antall_rotter = start_antall * endring ** år

print("Etter",år, "år har vi", round(antall_rotter),"rotter")

#B)

år = 0
total_populasjon = 20000
halvert = 10000
endring = 0.9

while total_populasjon > halvert:
    total_populasjon *= endring
    år += 1 

print("Vi må vente", år, "år før vi får", round(halvert),"rotter")
