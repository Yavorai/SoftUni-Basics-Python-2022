max_number = ''
number = input()

while number != 'Stop':
    x = int(number)
    if max_number == '':
        max_number = x
    if x > max_number:
        max_number = x
    number = input()

if max_number != '':
    print(max_number)
