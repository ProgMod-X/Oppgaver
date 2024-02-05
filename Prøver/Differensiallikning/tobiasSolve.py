import math
import matplotlib.pyplot as plt

def df(y, t):
    return ((10 + 9*math.sin((math.pi/6)*t) - ((1/6)*y)))*dt

# Oppgave C + E

dt = 0.01
y = 0
t = 0
max_change = 0
max_change_time = 0
x_list = []
y_list = []

while t < 48:
    y += df(y, t)
    x_list.append(t)
    y_list.append(y)
    if df(y, t) > max_change:
        max_change = df(y, t)
        max_change_time = t
    t += dt
    
print("----------------------------")
print(f"Vannmengden økte raskest etter {round(max_change_time, 2)} måneder, da økte den med {round(max_change / dt, 3)} millioner kubikkmeter per måned")
    

plt.plot(x_list, y_list)
plt.xlabel("Tid i måneder")
plt.ylabel("Millioner kubikkmeter")
plt.grid()
plt.show()

# Oppgave D

# Jeg mener at reservoaret burde ha plass til omtrent 80 millioner kubikkmeter
# Dette er fordi grafen viser at det vil være maksimalt litt over 75 millioner kubikkmeter i reservoaret
# Da får vi en liten sikkerhetsmargin i tilfelle det blir ekstra mye regn, i tillegg ti alt vi får beholde alt det forventede vannet

# Oppgave F

benyttelse = 100
start_mengde = y
for i in range(1000):
    y = start_mengde
    t = 48
    while t < 96:
        y += df(y, t) - benyttelse*dt
        if y < 20:
            break
        t += dt
    if y > 20:
        break
    benyttelse -= 0.1

print("----------------------------")
print(f"Nabokommunen kan benytte seg av maksimalt {round(benyttelse, 3)} millioner kubikkmeter per måned")