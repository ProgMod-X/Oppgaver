medicine_in_body = 100
time = 0
k = 0.000001

target_medicine_in_body = 80
target_time = 24

while medicine_in_body > target_medicine_in_body:
    time = 0
    medicine_in_body = 0
    while time < target_time:
        medicine_in_body += -k * medicine_in_body + 5
        time += 1
    k += 0.000001
print(round(time), round(medicine_in_body), round(k, 6))