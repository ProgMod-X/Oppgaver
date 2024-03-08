import matplotlib.pyplot as plt

def deltaY(k, y, w):
    return (k * y) + w

factor = 0.000
change = 1000
balance = 0

correct = False

while correct == False:
    balance = 0
    factor += 0.00001
    for i in range(40):
        balance += deltaY(factor, balance, change)
    if round(balance/10)*10 == 47900:
        correct = True
        
print(balance)
print(round(factor*100,2))