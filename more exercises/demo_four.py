#from math import floor
one_euro = float(1.94)

price_kg_vegetables = float(input())
price_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

price_vege = price_kg_vegetables * total_kg_vegetables
price_fruits = price_kg_fruits * total_kg_fruits
sum_all = (price_vege + price_fruits) / one_euro
print(format(sum_all,".2f"))
