from math import ceil,floor
magnolii_number = int(input()) * 3.25
ziombiuli_number = int(input()) * 4
rozi_number = int(input()) * 3.50
kaktusi_number = int(input()) * 8

gift_price = float(input())

total = magnolii_number + ziombiuli_number + rozi_number + kaktusi_number
total -= (5 / 100) * total 


if total >= gift_price:
    print(f'She is left with {floor(total - gift_price)} leva.')
elif total < gift_price:
    print(f'She will have to borrow {ceil(gift_price - total)} leva.')

