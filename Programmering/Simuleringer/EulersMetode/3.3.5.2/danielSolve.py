import matplotlib.pyplot as plt

def model(A):
    k = 0.01
    y = k * A * (1 - A / 800)
    return y

A = 158

# Tidspunkter for simulering (10 år)
t_values = []
A_values = []

# Simuler utviklingen over 10 år
dt = 0.1
t = 0
while t <= 10:
    t_values.append(t)
    A_values.append(A)

    # Bruk Eulers metode for å oppdatere A
    y = model(A) * dt
    A += y

    t += dt

# Plot grafen
plt.plot(t_values, A_values)
plt.xlabel('Tid (år)')
plt.ylabel('Antall ansatte')
plt.title('Utvikling i antall ansatte over 10 år')
plt.grid(True)
plt.show()
