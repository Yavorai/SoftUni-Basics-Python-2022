movie_budget = float(input())
extras = int(input())
price_clothe_per_extras = float(input())

price_for_clothes = extras * price_clothe_per_extras

if extras > 150:
    price_for_clothes *= 0.90

decor = movie_budget * 0.10

money = decor + price_for_clothes

if money > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {money - movie_budget:.2f} leva more.")
else :
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - money:.2f} leva left.")