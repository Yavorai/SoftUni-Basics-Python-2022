chrysanthemum_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()

holiday_y_or_n = input()

sum_bouquet = 0
price_arranging_bouquet = 2
total_amount_all_flowers = chrysanthemum_number + roses_number + tulips_number

if season == 'Spring' or season == 'Summer':

    if holiday_y_or_n == 'Y':
       sum_bouquet += (chrysanthemum_number * 2.00) + (roses_number * 4.10) + (tulips_number * 2.50)
       sum_bouquet += sum_bouquet * 0.15
    elif holiday_y_or_n == 'N':
       sum_bouquet += (chrysanthemum_number * 2.00) + (roses_number * 4.10) + (tulips_number * 2.50)


    if tulips_number > 7 and season == 'Spring':
        sum_bouquet -= sum_bouquet * 0.05

    if total_amount_all_flowers > 20: 
        sum_bouquet -= sum_bouquet * 0.20

    sum_bouquet += price_arranging_bouquet

elif season == 'Autumn' or season == 'Winter':

    if holiday_y_or_n == 'Y':
        sum_bouquet += (chrysanthemum_number * 3.75) + (roses_number * 4.50) + (tulips_number * 4.15)
        sum_bouquet += sum_bouquet * 0.15
    elif holiday_y_or_n == 'N':
        sum_bouquet += (chrysanthemum_number * 3.75) + (roses_number * 4.50) + (tulips_number * 4.15)


    if roses_number >= 10 and season == 'Winter':
         sum_bouquet -= sum_bouquet * 0.10

    if total_amount_all_flowers > 20: 
        sum_bouquet -= sum_bouquet * 0.20

    sum_bouquet += price_arranging_bouquet


print(f'{sum_bouquet:.2f}')