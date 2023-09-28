myNumbers = [] # Glemte å definere listen

for i in range(7):
    myNumbers.append(0)
    
myNumbers[(len(myNumbers)//2)] = 42

numbers = [18,355,6,34,34,56,3,4,534,6,3] # Ukjent liste

myNumbers[0] = numbers[-1]

if numbers[0] > 17:
    myNumbers[(len(myNumbers)-1)] = numbers[0]
    
print(myNumbers)