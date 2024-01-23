import matplotlib.pyplot as plt

def f(kropp, factor):
    return kropp * factor + 2.4

maxKropp = 5.5
kropp = 10
factor = 0.75

while kropp > maxKropp:
    kropp = 0
    for i in range(20):
        kropp = f(kropp, factor)
    factor -= 0.00001

print(f"Det må gå {round(factor/0.75*24 + 24)} timer mellom hver gang Mads tar en tablett")