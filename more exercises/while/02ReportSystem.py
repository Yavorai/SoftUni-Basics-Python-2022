target_amount = int(input())
money_collected = 0
cash_limit_max = 100
card_limit_min = 10
pay_cash = False
sum_cash = 0
count_cash = 0
sum_card = 0
count_card = 0
sum_all = 0
product_price = input()

while product_price != 'End':  # and sum_all<target_amount:
    pay_cash = not pay_cash
    product_price = int(product_price)
    if pay_cash:
        if product_price > cash_limit_max:
            print('Error in transaction!')
        else:
            print('Product sold!')
            sum_cash += product_price
            count_cash += 1
    else:
        if product_price < card_limit_min:
            print('Error in transaction!')
        else:
            print('Product sold!')
            sum_card += product_price
            count_card += 1
    sum_all = sum_cash + sum_card
    if sum_all >= target_amount:
        break
    product_price = input()

if sum_all >= target_amount:
    print(f'Average CS: {(sum_cash / count_cash):.2f}')
    print(f'Average CC: {(sum_card / count_card):.2f}')
elif product_price == 'End':
    print('Failed to collect required money for charity.')
