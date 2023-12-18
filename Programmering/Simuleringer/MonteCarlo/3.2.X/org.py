import random
N = 100
n = 0
x = 100
y = 50
teller = 0
x_liste=[]
y_liste=[]
 
def f(a,x,b):
    y = (a*x) + b
    return y
def g(a,y,b):
    x = (y-b)/float(a)
    return x
 
while n<N:
    # Lys
    x_1 = random.randint(1,x) #Gjør alle til float
    x_2 = random.randint(1,x)
    y_1 = random.randint(1,y)
    y_2 = random.randint(1,y)
    # Slice
    sx_1 = random.randint(1,x)
    sy_1 = random.randint(1,y)
    sx_2 = random.randint(1,x)
    sy_2 = random.randint(1,y)
    
    #Delta av linjer
    dsx = sx_2-sx_1
    dsy = sy_2-sy_1
    #Stigning
    a = dsy/dsx
    if a == 0:
        continue
    b = sy_1 - a*sx_1
 
    if f(a, x_1, b) < y_1 and f(a, x_2, b) > y_2 or f(a, x_1, b) > y_1 and f(a, x_2, b) < y_2 or g(a, y_1, b) < x_1 and g(a, y_2, b) > x_1 or g(a, y_2, b) < x_2 and g(a, y_1, b) > x_2:
        teller += 1
    n += 1
odds = (teller/N)*100
print(f"Odds er {odds} %")