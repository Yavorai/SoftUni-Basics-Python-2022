n_numbers = int(input())
sum_odd_positions = 0
sum_even_positions = 0
for i in range(1, n_numbers + 1):
    x = int(input())
    if i % 2 == 0:
        sum_even_positions += x
    else:
        sum_odd_positions += x
diff = abs(sum_odd_positions - sum_even_positions)
if diff == 0:
    print(f'Yes')
    print(f'Sum = {sum_odd_positions}')
else:
    print(f'No')
    print(f'Diff = {diff}')
