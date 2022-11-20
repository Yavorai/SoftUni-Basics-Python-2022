numbers_count = int(input())
odd_sum = 0
even_sum = 0
odd_min = 'No'
odd_max = odd_min
even_min = odd_min
even_max = odd_min


for i in range(1, numbers_count + 1):
    x = float(input())
    if i % 2 == 1:
        odd_sum += x
        if odd_min == 'No':
            odd_min = x
            odd_max = x
        elif x < odd_min:
            odd_min = x
        elif x > odd_max:
            odd_max = x
    else:
        even_sum += x
        if even_min == 'No':
            even_min = x
            even_max = x
        elif x < even_min:
            even_min = x
        elif x > even_max:
            even_max = x
if odd_min != 'No':
    odd_min = f'{odd_min:.2f}'
    odd_max = f'{odd_max:.2f}'
if even_min != 'No':
    even_min = f'{even_min:.2f}'
    even_max = f'{even_max:.2f}'

print(f'OddSum={odd_sum:.2f},')
print(f'OddMin={odd_min},')
print(f'OddMax={odd_max},')
print(f'EvenSum={even_sum:.2f},')
print(f'EvenMin={even_min},')
print(f'EvenMax={even_max}')
