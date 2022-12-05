starting_interval = int(input())
final_interval = int(input())
magic_number = int(input())

combination_counter = 0
condition = False

for a in range(starting_interval, final_interval + 1):
    for b in range(starting_interval, final_interval + 1):
        
        combination_counter += 1
        
        if a + b == magic_number:
            print(f'Combination N:{combination_counter} ({a} + {b} = {magic_number})')
            condition = True
            
    if condition:
        break       
    
if not condition:
    print(f'{combination_counter} combinations - neither equals {magic_number}')
    