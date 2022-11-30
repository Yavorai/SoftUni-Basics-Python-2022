numbers_count = int(input())
sum_numbers = 0
for i in range(numbers_count):
    x = int(input())
    sum_numbers += x

avg_number = sum_numbers / numbers_count
print('{:.2f}'.format(avg_number))
