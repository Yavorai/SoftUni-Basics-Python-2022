days = int(input())
type_room = input()
assessment = input()
 
nights = days - 1
expenses = 0
if type_room == "room for one person":
    expenses = 18 * nights
elif type_room == "apartment":
    expenses = 25 * nights
    if days < 10:
        expenses = expenses * 0.70
    elif 10 <= days <= 15:
        expenses = expenses * 0.65
    else:
        expenses = expenses * 0.50
elif type_room == "president apartment":
    expenses = 35 * nights
    if days < 10:
        expenses = expenses * 0.90
    elif 10 <= days <= 15:
        expenses = expenses * 0.85
    else:
        expenses = expenses * 0.80
 
if assessment == "positive":
    expenses = expenses * 1.25
else:
    expenses = expenses * 0.90
 
print(f"{expenses:.2f}")