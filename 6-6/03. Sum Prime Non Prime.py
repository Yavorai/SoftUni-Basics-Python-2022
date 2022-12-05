input_line = input()
prime_sum = 0
non_prime_sum = 0

while input_line != 'stop':
    current_num = int(input_line)
    
    if current_num < 0: # негативното не участва в брояча
        print('Number is negative.')
        input_line = input() # все пак да прочете новия ред 
        continue
        
    count = 0
    for i in range(1, current_num + 1):
        # 3 // 1,  3 // 2,  3 // 3
        # 6 // 1,  6 // 2,  6 // 3,  6 // 4,  6 // 5,  6 // 6
        
        if current_num % i == 0:
        # брои само колко делителя има без остатък
        # ако са само 2 е просто 
            count += 1
        
    if count == 2:
        prime_sum += current_num  
    else: 
        non_prime_sum += current_num
        
    input_line = input()
    
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')