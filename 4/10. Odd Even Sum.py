number = int(input())
odd_sum = 0
even_sum = 0
for i in range(1, number + 1):
    curr = int(input())
    if i % 2 == 0:
        even_sum += curr
    else:
        odd_sum += curr
if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')        
else:
    print('No')    
    print(f'Diff = {abs(even_sum - odd_sum)}')    