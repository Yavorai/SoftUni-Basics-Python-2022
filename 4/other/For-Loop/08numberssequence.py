import sys

n_numbers = int(input())
# min_number = 0
# min_number = sys.maxsize
# max_number = 0
# max_number = -sys.maxsize
for i in range(0, n_numbers):
    x = int(input())
    if i > 0:
        if x < min_number:
            min_number = x
        elif x > max_number:
            max_number = x
    elif i == 0:
        min_number = x
        max_number = x
if n_numbers > 0:
    print(f'Max number: {max_number}')
    print(f'Min number: {min_number}')
