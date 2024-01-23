import matplotlib.pyplot as plt

# Lar vekstfaktoren være 50% siden det er over en lang periode har ikke det noe si om halveringstiden er 66 t
def f(kropp):
    return kropp * 0.5 + 10

kropp = 0

x_list = []
y_list = []

for i in range(1000):
    kropp = f(kropp)
    x_list.append(i)
    y_list.append(kropp)

print(f"Virkestoffet i kroppen vil være {kropp} mg etter brukeren har brukt tabletten i en langtidsperiode.")

plt.plot(x_list, y_list)
plt.show()