spending_days_limit = 5
consecutive_spending_days = 0
cant_save = False
target_reached = False
target_money = float(input())
init_money = float(input())
total_money = init_money
days_count = 0

while True:
    days_count += 1
    transaction = input()
    transaction_value = float(input())
    if transaction == 'save':
        total_money += transaction_value
        consecutive_spending_days = 0
    elif transaction == 'spend':
        total_money -= abs(transaction_value)
        if total_money < 0:
            total_money = max(0, total_money)
        consecutive_spending_days += 1
    # total_money=max(0, total_money)
    if consecutive_spending_days >= spending_days_limit:
        cant_save = True
        break
    elif total_money >= target_money:
        target_reached = True
        break

if cant_save:
    print('You can\'t save the money.')
    print(days_count)
elif target_reached:
    print(f'You saved the money for {days_count} days.')
