rotter = 20000
minsker = 0.9
år = 3

# A 
a = rotter * (minsker) ** år

print("A:")
print(round(a, 1))

# B

orginal_rotter = rotter
år = 1

while rotter >= (orginal_rotter/2):
    rotter *= minsker 
    år += 1

print("B:")
print("Det vil ta", år, "år før rottepopulasjonen er halvert")