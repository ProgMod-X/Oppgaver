rotter = 20000
minsker = 0.9
år = 3

orginal_rotter = rotter
år = 1

while rotter >= (orginal_rotter/2):
    rotter *= minsker 
    år += 1

print("B:")
print("Det vil ta", år, "år før rottepopulasjonen er halvert")