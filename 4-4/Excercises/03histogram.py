numbers_count = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(numbers_count):
    x = int(input())
    if x >= 800:
        p5 += 1
    elif x >= 600:
        p4 += 1
    elif x >= 400:
        p3 += 1
    elif x >= 200:
        p2 += 1
    elif x < 200:
        p1 += 1

print(f'{(p1 / numbers_count * 100):.2f}%')
print(f'{(p2 / numbers_count * 100):.2f}%')
print(f'{(p3 / numbers_count * 100):.2f}%')
print(f'{(p4 / numbers_count * 100):.2f}%')
print(f'{(p5 / numbers_count * 100):.2f}%')
