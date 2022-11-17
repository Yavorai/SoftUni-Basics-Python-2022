season = input()  # each 4 months
km_per_month = float(input())
money = 0

if season == 'Spring' or season == 'Autumn':

    if km_per_month <= 5000:
        money = km_per_month * 0.75
    elif km_per_month > 5000 and km_per_month <= 10000:
        money = km_per_month * 0.95
    elif km_per_month > 10000 and km_per_month <= 20000:
        money = km_per_month * 1.45

elif season == 'Summer':

    if km_per_month <= 5000:
        money = km_per_month * 0.90
    elif km_per_month > 5000 and km_per_month <= 10000:
        money = km_per_month * 1.10
    elif km_per_month > 10000 and km_per_month <= 20000:
        money = km_per_month * 1.45
        
elif season == 'Winter':
    
    if km_per_month <= 5000:
        money = km_per_month * 1.05    
    elif km_per_month > 5000 and km_per_month <= 10000:
        money = km_per_month * 1.25
    elif km_per_month > 10000 and km_per_month <= 20000:
        money = km_per_month * 1.45


money = (money * 4) * 0.90
print(f'{money:.2f}')