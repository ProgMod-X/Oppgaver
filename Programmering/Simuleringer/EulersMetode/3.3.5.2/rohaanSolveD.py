medicine_in_body = 0
time = 0
k = 0.037569
dose = 5

target_medicine_in_body = 150
target_time = 48

while medicine_in_body < target_medicine_in_body:
    time = 0
    medicine_in_body = 0
    while time < 24:
        medicine_in_body += -k * medicine_in_body + 5
        time += 1
    while time < target_time:
        medicine_in_body += -k * medicine_in_body + dose
        time += 1
    dose += 0.0001
print(round(time), round(medicine_in_body), round(dose, 6))
