expected_sum = int(input())
card_count = 0
cash_count = 0
real_sum = 0
counter = 0
cash = 0
card = 0
data = input()
is_ok = False
while data != 'End':
    money_item = int(data)
 
    if counter % 2 == 0:
        if money_item <= 100:
            cash_count += 1
            real_sum += money_item
            cash += money_item
            print("Product sold!")
        else:
            print("Error in transaction!")
 
    elif counter % 2 != 0:
        if money_item >= 10:
            card_count += 1
            real_sum += money_item
            card += money_item
            print("Product sold!")
        else:
            print("Error in transaction!")
 
    if real_sum >= expected_sum:
        is_ok = True
        break
 
    counter += 1
    #------------------------------------
    data = input()
    # end of loop
if is_ok:
    print(f"Average CS: {f'{cash / cash_count:.2f}'}")
    print(f"Average CC: {f'{card / card_count:.2f}'}")
elif data == 'End':
        print("Failed to collect required money for charity.")
#===========================================================================
# expected_sum = int(input())
# sold_cash = 0
# sold_card = 0
# total_cash = 0
# total_card = 0
# product_count = 0
# while True:
#     if total_cash + total_card >= expected_sum:
#         print(f'Average CS: {total_cash / sold_cash:.2f}')
#         print(f'Average CC: {total_card / sold_card:.2f}')
#         break
#     command = input()
#     if command == 'End':
#         print('Failed to collect required money for charity.')
#         break
#     price = int(command)
#     product_count += 1
#     is_cash_payment = product_count % 2 == 1
#     if price <= 100 and is_cash_payment:
#         total_cash += price
#         sold_cash += 1
#     elif price >= 10 and not is_cash_payment:
#         total_card += price
#         sold_card += 1
#     else:
#         print('Error in transaction!')
#         continue
#     print('Product sold!')        