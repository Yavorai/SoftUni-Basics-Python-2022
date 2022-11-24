number_of_moves = int(input())

result = 0
#total_result = 0
counter = 0

number_1 = 0
number_2 = 0
number_3 = 0
number_4 = 0
number_5 = 0
number_6 = 0

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for _ in range(1, number_of_moves + 1):
    num_interval = int(input())
    counter += 1
    if num_interval < 0 or num_interval > 50:
        number_1 += counter
        result /= 2
        one = (number_1 * 100) / number_of_moves
    elif num_interval <= 9:
        number_2 += counter
        result += num_interval * 0.20  
        two = (number_2 * 100) / number_of_moves
        
    elif num_interval <= 19:
        number_3 += counter
        result += num_interval * 0.30
        three = (number_3 * 100) / number_of_moves
        
    elif num_interval <= 29:
        number_4 += counter
        result += num_interval * 0.40
        four = (number_4 * 100) / number_of_moves
        
    elif num_interval <= 39:
        number_5 += counter
        result += 50             
        five = (number_5 * 100) / number_of_moves
         
    elif num_interval <= 50:
        number_6 += counter
        result += 100
        six = (number_6 * 100) / number_of_moves
        
    counter = 0
    
print(f'{result:.2f}')
print(f'From 0 to 9: {two:.2f}%')
print(f'From 10 to 19: {three:.2f}%')
print(f'From 20 to 29: {four:.2f}%')
print(f'From 30 to 39: {five:.2f}%')
print(f'From 40 to 50: {six:.2f}%')
print(f'Invalid numbers: {one:.2f}%')