bonus_money = float(input())
year = int(input())
ivan_age = 18

for i in range(1800, year + 1):
    if i % 2 == 0:
        bonus_money -= 12000.0
    else:    
        bonus_money -= 12000.0 + 50 * ivan_age
    ivan_age += 1

if bonus_money >= 0:
    print(f'Yes! He will live a carefree life and will have {bonus_money:.2f} dollars left.')
else:
    print(f"He will need {abs(bonus_money):.2f} dollars to survive.")