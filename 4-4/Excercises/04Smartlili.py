age_lily = int(input())
price_machine = float(input())
toy_price = int(input())

toys_count = 0
money_collected = 0
birthday_money = 0

for i in range(1, age_lily + 1):
    if i % 2 == 1:
        toys_count += 1
    else:
        birthday_money += 10
        money_collected += birthday_money - 1

money_collected += toys_count * toy_price
diff = abs(money_collected - price_machine)
if price_machine > money_collected:
    print(f'No! {diff:.2f}')
else:
    print(f'Yes! {diff:.2f}')
