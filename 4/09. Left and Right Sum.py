n_numbers = int(input())

first_sum = 0
second_sum = 0

for _ in range(0, n_numbers):
    curr = int(input())
    first_sum += curr
for _ in range(0, n_numbers):
    curr = int(input())
    second_sum += curr   
    
diff = abs(first_sum - second_sum)
if diff == 0:
    print(f'Yes, sum = {first_sum}')
else:
    print(f'No, diff = {diff}')
    