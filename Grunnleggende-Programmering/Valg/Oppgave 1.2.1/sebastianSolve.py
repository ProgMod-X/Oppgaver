'''
Lag et program som leser inn ett tall, og skriver ut absoluttverdien til tallet. Du kan ikke bruke funksjonen abs().
'''

orginal_verdi = float(input("Tall: "))

#Spør om å inputte et tall 

if orginal_verdi < 0:
    absolut_verdi = -orginal_verdi
    
#Hvis orginalverdien er mindre en null, alstå et negativt tall, gjør programmet den om til et positivt tall
    
else:
    absolut_verdi = orginal_verdi

#Hvis orginalverdien ikke er negativ så kan den bare bli printet 

print("Absolutverdien av", orginal_verdi, "er", "|",absolut_verdi,"|")

#Her prints orignalveriden og absolutverdien