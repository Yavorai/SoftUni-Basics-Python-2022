from math import ceil, floor
number_of_days = int(input())
left_food_kg = int(input())
dog_food_day_kg = float(input())
cat_food_day_kg = float(input())
turtle_food_grams = float(input())

actual_food = (dog_food_day_kg * number_of_days) + (cat_food_day_kg * number_of_days) + ((turtle_food_grams * number_of_days) / 1000)


if left_food_kg >= actual_food:
    print(f'{floor(left_food_kg - actual_food)} kilos of food left.')
else:   
    print(f'{ceil(actual_food - left_food_kg)} more kilos of food are needed.')