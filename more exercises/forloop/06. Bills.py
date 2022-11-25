months = int(input())

electricity = 0
water = 0
internet = 0
other = 0
avg = 0

electricity2 = 0
water2 = 0
internet2 = 0
other2 = 0

for _ in range(1, months + 1):
    el_bill = float(input())
    
    electricity = el_bill
    electricity2 += electricity
    water = 20
    water2 += water
    internet = 15
    internet2 += internet
    other = (electricity + water + internet) + ((electricity + water + internet) * 0.20)
    other2 += other

    avg += electricity + water + internet + other
    
print(f'Electricity: {electricity2:.2f} lv')
print(f'Water: {water2:.2f} lv')
print(f'Internet: {internet2:.2f} lv')
print(f'Other: {other2:.2f} lv')
print(f'Average: {avg / months:.2f} lv')