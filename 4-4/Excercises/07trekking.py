groups_count = int(input())
pMusala = 0
pMonblan = 0
pKilimandjaro = 0
pK2 = 0
pEverest = 0
pAll = 0
for i in range(groups_count):
    x = int(input())  # people in each group
    pAll += x
    if x > 40:
        pEverest += x
    elif x > 25:
        pK2 += x
    elif x > 12:
        pKilimandjaro += x
    elif x > 5:
        pMonblan += x
    else:
        pMusala += x
print(f'{(pMusala / pAll * 100):.2f}%')
print(f'{(pMonblan / pAll * 100):.2f}%')
print(f'{(pKilimandjaro / pAll * 100):.2f}%')
print(f'{(pK2 / pAll * 100):.2f}%')
print(f'{(pEverest / pAll * 100):.2f}%')
