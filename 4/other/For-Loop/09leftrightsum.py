n_numbers = int(input())
left_sum = 0
right_sum = 0
for i in range(0, n_numbers):
    x = int(input())
    left_sum += x
for i in range(0, n_numbers):
    x = int(input())
    right_sum += x
diff = abs(right_sum - left_sum)
if diff == 0:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {diff}')
