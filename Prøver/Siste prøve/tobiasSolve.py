import matplotlib.pyplot as plt

def dy(y, k, w):
    return k*y + w

t = 0
bak_start = 100_000

y = bak_start
dt = 0.001
y_max = bak_start
y_max_t = 0

t_list = []
y_list = []

while y > 0:
    bak_form = 0.25*dt
    bak_kur = -10000*(t+1)*dt
    y += dy(y, bak_form, bak_kur)
    y_list.append(y)
    t_list.append(t)
    
    if y > y_max:
        y_max = y
        y_max_t = t
        
    t += dt
        
print(f"Det tar {t:0.3f} døgn før infeksjonen er over")
print(f"Det tar {y_max_t:0.3f} døgn før infeksjonen når toppen")

y = bak_start
bak_kur = 0
y2_list = []
t = 0

while t <= t_list[-1]:
    bak_form = 0.25*dt
    y += dy(y, bak_form, bak_kur)
    y2_list.append(y)
    
    t += dt
    
plt.plot(t_list, y_list)
plt.plot(y_max_t, y_max, "o")
plt.plot(t_list, y2_list)
plt.grid()
plt.show()