budget = float(input())
season = input()

location = ''
accommodation = ''

if budget <= 1000:

    accommodation = 'Camp'

    if season == 'Summer':
        location = 'Alaska'
        budget -= budget * 0.35
    elif season == 'Winter':
        location = 'Morocco'
        budget -= budget * 0.55

elif budget > 1000 and budget <= 3000:

    accommodation = 'Hut'

    if season == 'Summer':
        location = 'Alaska'
        budget -= budget * 0.20
    elif season == 'Winter':
        location = 'Morocco'
        budget -= budget * 0.40


elif budget > 3000:

    accommodation = 'Hotel'

    if season == "Summer":
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'
    budget -= budget * 0.10

print(f'{location} - {accommodation} - {budget:.2f}')
