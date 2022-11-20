# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,
# и проверява дали сред тях съществува число, което е равно на сумата на всички останали.
# •	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# •	Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност)

numbers_count = int(input())
max_number = 0
sum_numbers = 0
diff = 0

for i in range(numbers_count):
    x = int(input())
    if (i == 0) or (x > max_number):
        max_number = x
    sum_numbers += x
diff = abs(sum_numbers - 2 * max_number)

if diff == 0:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {diff}')
