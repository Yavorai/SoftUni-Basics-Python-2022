min_number = ''
number = input()

while number != 'Stop':
    x = int(number)
    if min_number == '':
        min_number = x
    if x < min_number:
        min_number = x
    number = input()

if min_number != '':
    print(min_number)
