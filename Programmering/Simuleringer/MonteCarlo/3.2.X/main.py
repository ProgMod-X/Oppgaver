import random
N = 100
n = 0
x = 100
y = 50
teller = 0
temp_teller = 0
x_liste=[]
y_liste=[]
 
def f(a,x,b):
    y = (a*x) + b
    return y
def g(a,y,b):
    x = (y-b)/float(a)
    return x

while n<N:
    # A
    a_x = random.randint(1,x) #Gjør alle til float
    a_y = random.randint(1,x)
    
    # B
    b_x = random.randint(1,x)
    b_y = random.randint(1,x)
    
    # C
    c_x = random.randint(1,x)
    c_y = random.randint(1,x)
    
    # D
    d_x = random.randint(1,x)
    d_y = random.randint(1,x)
   
    # E
    e_x = random.randint(1,x)
    e_y = random.randint(1,x)

    # Linje AB
    d_AB_x = b_x-a_x # Delta X
    d_AB_y = b_y-a_y # Delta Y
    # Stigningstall
    a_AB = d_AB_y/d_AB_x 
    if d_AB_x == 0:
        continue
    b_AB = a_y - a_AB*a_x
    
    if f(a_AB, a_x, b_AB) < d_y:
        temp_teller += 1
    
    # Linje BC
    d_BC_x = c_x-b_x # Delta X
    d_BC_y = c_y-b_y # Delta Y
    # Stigningstall
    a_BC = d_BC_y/d_BC_x 
    if d_BC_x == 0:
        continue
    b_BC = b_y - a_AB*b_x
    
    if f(a_BC, b_x, b_BC) < e_y:
        temp_teller += 1
    
    # Linje CD
    d_CD_x = d_x-c_x # Delta X
    d_CD_y = d_y-c_y # Delta Y
    # Stigningstall
    a_CD = d_CD_y/d_CD_x 
    if d_CD_x == 0:
        continue
    b_CD = c_y - a_CD*c_x
    
    if f(a_CD, c_x, b_CD) < a_y:
        temp_teller += 1
    
    # Linje DE
    d_DE_x = e_x-d_x # Delta X
    d_DE_y = e_y-d_y # Delta Y
    # Stigningstall
    a_DE = d_DE_y/d_DE_x 
    if d_DE_x == 0:
        continue
    b_DE = d_y - a_DE*d_x
    
    if f(a_DE, d_x, b_DE) < b_y:
        temp_teller += 1
    
    # Linje EA
    d_EA_x = a_x-e_x # Delta X
    d_EA_y = a_y-e_y # Delta Y
    # Stigningstall
    a_EA = d_EA_y/d_EA_x 
    if d_EA_x == 0:
        continue
    b_EA = e_y - a_EA*e_x

    
    
    if temp_teller == 5:
        n += 1
    
    #####
    # d_BC_x = 
    
    
    # print()
    
    # #Delta
    # dsx = sx_2-sx_1
    # dsy = sy_2-sy_1
    
    # #Stigning
    # a = dsy/dsx
    # if a == 0:
    #     continue
    # b = sy_1 - a*sx_1
 
    # if f(a, x_1, b) < y_1 and f(a, x_2, b) > y_2 or f(a, x_1, b) > y_1 and f(a, x_2, b) < y_2 or g(a, y_1, b) < x_1 and g(a, y_2, b) > x_1 or g(a, y_2, b) < x_2 and g(a, y_1, b) > x_2:
    #     teller += 1
    # n += 1
odds = (teller/N)*100
print(f"Odds er {odds} %")
print(temp_teller)
