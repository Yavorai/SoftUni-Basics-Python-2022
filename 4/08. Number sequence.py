import sys
number = int(input())
max = -sys.maxsize
min = sys.maxsize

for num in range(number):
    current_number = int(input())
    if current_number > max:
        max = current_number
    if current_number < min:
        min = current_number
        
print(f'Max number: {max}')    
print(f'Min number: {min}')    