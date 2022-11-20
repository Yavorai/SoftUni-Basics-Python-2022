open_tabs_count = int(input())
init_salary = float(input())
salary = init_salary
for i in range(open_tabs_count):
    tab_name = input()

    if tab_name == 'Facebook':
        salary -= 150
    elif tab_name == 'Instagram':
        salary -= 100
    elif tab_name == 'Reddit':
        salary -= 50
    if salary <= 0:
        break
salary = int(salary)
if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
