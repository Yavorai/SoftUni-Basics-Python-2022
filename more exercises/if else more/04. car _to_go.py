budget = float(input())
season = input()
car_type = ''
class_type = ''
if season == 'Summer':
    if budget <= 100:
        class_type = 'Economy class'
        budget = budget - budget * 0.65
        car_type = 'Cabrio'
    elif budget > 100 and budget <= 500:
        class_type = 'Compact class'
        budget = budget - budget * 0.55
        car_type = 'Cabrio'
    elif budget > 500:
        class_type = 'Luxury class'
        budget = budget - budget * 0.10
        car_type = 'Jeep'
elif season == 'Winter':
    if budget <= 100:
        class_type = 'Economy class'
        budget = budget - budget * 0.35
        car_type = 'Jeep'
    elif budget > 100 and budget <= 500:
        class_type = 'Compact class'
        budget = budget - budget * 0.20
        car_type = 'Jeep'
    elif budget > 500:
        class_type = 'Luxury class'
        budget = budget - budget * 0.10
        car_type = 'Jeep'
print(f'{class_type}')
print(f'{car_type} - {budget:.2f}')
