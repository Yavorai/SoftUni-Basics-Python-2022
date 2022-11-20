seats_capacity = int(input())
fans_number = int(input())
secA = 0
secB = 0
secV = 0
secG = 0
for i in range(fans_number):
    sector = input()
    secA += int(sector == 'A')
    secB += int(sector == 'B')
    secV += int(sector == 'V')
    secG += int(sector == 'G')

print(f'{(secA / fans_number * 100):.2f}%')
print(f'{(secB / fans_number * 100):.2f}%')
print(f'{(secV / fans_number * 100):.2f}%')
print(f'{(secG / fans_number * 100):.2f}%')
print(f'{(fans_number / seats_capacity * 100):.2f}%')
