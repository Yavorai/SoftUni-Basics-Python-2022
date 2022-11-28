account_balance = 0
transaction = input()
while transaction != 'NoMoreMoney':
    x = float(transaction)
    if x < 0:
        print('Invalid operation!')
        break
    account_balance += x
    print(f'Increase: {x:.2f}')
    transaction = input()

print(f'Total: {account_balance:.2f}')
