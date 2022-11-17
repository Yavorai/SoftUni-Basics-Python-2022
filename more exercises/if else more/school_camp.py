season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())
price = 0
sport_type = ''

if season == 'Winter':
    if group_type == 'boys' or group_type == 'girls':
        price = students_count * 9.60 * nights_count
        
        if group_type == 'boys':
            sport_type = 'Judo'
        elif group_type == 'girls':
            sport_type = 'Gymnastics'
            
        if students_count >= 50:
            price -= price * 0.50
        elif students_count >= 20 and students_count < 50:
            price -= price * 0.15
        elif students_count >= 10 and students_count < 20:
            price -= price * 0.05
        
    elif group_type == 'mixed':
        price = students_count * 10 * nights_count
        sport_type = 'Ski'
        if students_count >= 50:
            price -= price * 0.50
        elif students_count >= 20 and students_count < 50:
            price -= price * 0.15
        elif students_count >= 10 and students_count < 20:
             price -= price * 0.05
        
elif season == 'Spring':
    if group_type == 'boys' or group_type == 'girls':
        price = students_count * 7.20 * nights_count
        
        if group_type == 'boys':
            sport_type = 'Tennis'
        elif group_type == 'girls':
            sport_type = 'Athletics'
        
        if students_count >= 50:
            price -= price * 0.50
        elif students_count >= 20 and students_count < 50:
            price -= price * 0.15
        elif students_count >= 10 and students_count < 20:
            price -= price * 0.05
            
    elif group_type == 'mixed':
        price = students_count * 9.50 * nights_count
        sport_type = 'Cycling'
        
        if students_count >= 50:
            price -= price * 0.50
        elif students_count >= 20 and students_count < 50:
            price -= price * 0.15
        elif students_count >= 10 and students_count < 20:
             price -= price * 0.05
            
if season == 'Summer':
    if group_type == 'boys' or group_type == 'girls':
        price = students_count * 15 * nights_count
        
        if group_type == 'boys':
            sport_type = 'Football'
        elif group_type == 'girls':
            sport_type = 'Volleyball'
            
        if students_count >= 50:
            price -= price * 0.50
        elif students_count >= 20 and students_count < 50:
            price -= price * 0.15
        elif students_count >= 10 and students_count < 20:
            price -= price * 0.05
            
    elif group_type == 'mixed':
        price = students_count * 20 * nights_count
        sport_type = 'Swimming'
        
        if students_count >= 50:
            price -= price * 0.50
        elif students_count >= 20 and students_count < 50:
            price -= price * 0.15
        elif students_count >= 10 and students_count < 20:
             price -= price * 0.05
    
   
    
print(f'{sport_type} {price:.2f} lv.')