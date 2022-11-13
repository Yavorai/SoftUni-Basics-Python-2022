number = int(input())

if 100 <= number <= 200 or number == 0:
    print()
else:
    print('invalid')
    

# or

is_valid = 100 <= number <= 200 or number == 0
if is_valid == False:
    print('invalid')
    
# or

is_valid = 100 <= number <= 200 or number == 0
if not is_valid:  # само ако is_false е със стойност false проверката ще се изпълни 
    print('invalid')
