inherited_money = float(input())
last_year = int(input())
start_year = 1800
start_age = 18
year = 0
# age = 0
money_left = inherited_money
# i = 0
yearly_expenses = 0
for year in range(start_year, last_year + 1):
    # age = start_age + i
    # age = start_age + (year - start_year)
    if year % 2 == 0:
        # yearly_expenses = 12000
        money_left -= 12000
    else:
        # yearly_expenses = 12000 + 50 * age
        money_left -= 12000 + 50 * (start_age + (year - start_year))
    # money_left -= yearly_expenses
    # i += 1

if money_left < 0:
    print(f'He will need {abs(money_left):.2f} dollars to survive.')
else:
    print(f'Yes! He will live a carefree life and will have {money_left:.2f} dollars left.')
