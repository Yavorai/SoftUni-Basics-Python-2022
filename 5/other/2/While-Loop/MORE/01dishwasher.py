detergent_bottles = int(input())
qty_detergent = detergent_bottles * 750  # ml
i = 0
dish_count = 0
pot_count = 0
x = input()
while x != 'End':
    y = int(x)
    i += 1
    if i % 3 == 0:
        consumption_rate = 15  # ml
        pot_count += y
    else:
        consumption_rate = 5  # ml
        dish_count += y

    qty_detergent -= consumption_rate * y
    if qty_detergent < 0:
        break
    x = input()

if qty_detergent < 0:
    print(f'Not enough detergent, {abs(qty_detergent)} ml. more necessary!')
else:
    print(f'Detergent was enough!')
    print(f'{dish_count} dishes and {pot_count} pots were washed.')
    print(f'Leftover detergent {qty_detergent} ml.')
