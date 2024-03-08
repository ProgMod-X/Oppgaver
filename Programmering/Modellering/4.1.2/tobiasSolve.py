import scipy.optimize as so
import matplotlib.pyplot as plt
import numpy as np

data_år = [1970, 1980, 1990, 2000, 2010]

data_x = [(år - 1970) for år in data_år]
data_y = [4.6, 6.2, 7.6, 8.2, 9.5]

plt.plot(data_x, data_y, "o")

def S(x, a, b):
    return a*x + b

konstanter = so.curve_fit(S, data_x, data_y)[0]

a = konstanter[0]
b = konstanter[1]

print(f"S(x) = {a}*x + {b}")

x = np.linspace(data_x[0],  50,  1000)

print(f"Hver person i Norge vil spise {S(50, a, b)*1000:0.2f} gram sjokolade i gjennomsnitt i løpet av 2020")


plt.plot(x, S(x, a, b), color="r")
plt.show()


# Stigningstallet forteller oss hvor mange mer kilo sjokolade en gjennomsnittlig nordmann spiser for hvert år som går

