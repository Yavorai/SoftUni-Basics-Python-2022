from math import floor

number_of_balls = int(input())
total_points = 0
counter_red = 0
counter_orange = 0
counter_yellow = 0
counter_white = 0
counter_black = 0
other_color_counter = 0

for _ in range(1, number_of_balls + 1):
    current_color = input()
    
    if current_color == 'red':
        total_points += 5
        counter_red += 1
    elif current_color == 'orange':
        total_points += 10
        counter_orange += 1
    elif current_color == 'yellow':
        total_points += 15
        counter_yellow += 1
    elif current_color == 'white':
        total_points += 20
        counter_white += 1
    elif current_color == 'black':
        total_points = floor(total_points / 2)
        counter_black += 1
    else:    
        other_color_counter += 1    
        
        
print(f'Total points: {total_points}')
print(f'Red balls: {counter_red}')
print(f'Orange balls: {counter_orange}')
print(f'Yellow balls: {counter_yellow}')
print(f'White balls: {counter_white}')
print(f'Other colors picked: {other_color_counter}')
print(f'Divides from black balls: {counter_black}')