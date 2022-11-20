# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на товарите за превоз – цяло число в интервала [1...1000]
# •	За всеки един товар на отделен ред – тонажа на товара – цяло число в интервала [1...1000]
n_loads = int(input())
total_weight = 0
# ton_price = 0
loads_van = 0
loads_truck = 0
loads_train = 0
for i in range(0, n_loads):
    load = int(input())
    total_weight += load
    # •	До 3 тона – микробус (200 лева на тон)
    # •	От 4 до 11 тона – камион (175 лева на тон)
    # •	12 и повече тона – влак (120 лева на тон)
    if load >= 12:
        loads_train += load
        # ton_price = 120
    elif load >= 4:
        loads_truck += load
        # ton_price = 175
    else:
        loads_van += load
        # ton_price = 200
total_price = loads_train * 120 + loads_truck * 175 + loads_van * 200
avg_price = total_price / total_weight
print(f'{avg_price:.2f}')
print(f'{(loads_van / total_weight * 100):.2f}%')
print(f'{(loads_truck / total_weight * 100):.2f}%')
print(f'{(loads_train / total_weight * 100):.2f}%')
