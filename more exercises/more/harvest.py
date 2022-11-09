from math import ceil, floor

# for 1 litter wine --> 2.5kg grape

x_sq_m = int(input())
y_sq_m = float(input())
z_needed_litters_wine = int(input())
workers_number = int(input())

grape_field_total = int(x_sq_m * y_sq_m)
part_for_wine = 40 * grape_field_total / 100 / 2.5
wine_left = part_for_wine - z_needed_litters_wine
wine_per_person = wine_left / workers_number

if part_for_wine >= z_needed_litters_wine:
    print(f"Good harvest this year! Total wine: {floor(part_for_wine)} liters.")
    print(f'{ceil(wine_left)} liters left -> {ceil(wine_per_person)} liters per person.')
elif part_for_wine < z_needed_litters_wine:
    
    wine_needed = z_needed_litters_wine - part_for_wine
    print(f'It will be a tough winter! More {floor(wine_needed)} liters wine needed.')