myNumbers = [] # Glemte å definere listen

for i in range(7):
    myNumbers.append(0)
    
myNumbers[(len(myNumbers)//2)] = 42

numbers = [2,355,6,34,34,56,3,4,534,6,18] # Ukjent liste

myNumbers[0] = numbers[-1]

if numbers[0] > 17:
    myNumbers[(len(myNumbers)-1)] = numbers[0] # Blir lagt inn på feil plass av en eller annen grunn
    
print(myNumbers)