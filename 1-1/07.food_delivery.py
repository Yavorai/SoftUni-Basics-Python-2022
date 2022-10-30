price_chicken = 10.35
price_fish = 12.40
price_veggie = 8.15
factor_desert = .2
cost_delivery = 2.5
qty_chicken = int(input())
qty_fish = int(input())
qty_veggie = int(input())
cost_chicken = qty_chicken * price_chicken
cost_fish = qty_fish * price_fish
cost_veggie = qty_veggie * price_veggie
cost_food = (cost_chicken + cost_fish + cost_veggie) * (1 + factor_desert)
print(round(cost_food + cost_delivery, 2))