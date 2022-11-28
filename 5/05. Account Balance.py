available_sum = 0

while True:
    
    current_sum = input()
    
    if current_sum == 'NoMoreMoney':
        break
    
    current_sum = float(current_sum)
    
    if current_sum >= 0:
        available_sum += current_sum
        print(f'Increase: {current_sum:.2f}')
    else:
        print('Invalid operation!')
        break
    
print(f'Total: {available_sum:.2f}')

# # var 2 

# inpt = input()
# balance = 0.0
# while inpt != 'NoMoreMoney':
#     amount = float(inpt)
#     if amount < 0:
#         balance += amount
#         print(f'Increase: {current_sum:.2f}')
#         inpt = input()
# print(f'Tatal: {balance:.2f}')