from math import sqrt


a = float(input("Hva er x-verdien til S? "))
b = float(input("Hva er y-verdien til S? "))
s = float(input("Hva er x-verdien til P? "))
t = float(input("Hva er y-verdien til P? "))
r = float(input("Hva er radiusen til sirkelen? "))


d = sqrt((s - a)**2 + (t - b)**2)

if d < r:
    print("Punktet ligger innenfor sirkelen")
elif d == r:
    print("Punktet ligger på sirkelen")
else:
    print("Punktet ligger utenfor sirkelen")