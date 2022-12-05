destination = input()
budget = float(input())
input_data = input()
total_sum = 0
while input_data != 'End':
    money = float(input_data)
    total_sum += money
    if total_sum >= budget:
        print(f'Going to {destination}!')
    input_data = input()
    #============================================
destination = input()  # това ти е еквивалент на command, който се презаписва накрая на цикъла
while destination != 'End':  # трябва ти цикъл, който проверява дали command/destination e 'End'
    min_budget = float(input())  # трябва да е float иначе ще получиш Runtime error на скрити тестове
    needed_money = 0
    while min_budget > needed_money:  # не трябва да влиза в цикъла когато са равни
        tips = float(input())  # същата работа като min_budget - ще се чудиш защо гърми
        needed_money += tips
    print(f'Going to {destination}!')  # достига се и печата, когато вложеният цикъл приключи
    destination = input() # презаписва се и ако е 'End' програмата приключва, иначе започва от начало
    #============================================
destination = input()
savedMoney = 0
while destination != "End":
    neededMoney = float(input())
    while savedMoney <= neededMoney:
        money = float(input())
        savedMoney += money
        if savedMoney >= neededMoney:
            print(f"Going to {destination}!")
            break
    savedMoney = 0
    destination = input()
    #============================================
location = input()
budget = savings = 0
while location != "End":
    budget = float(input())
    if budget > 0:
        while budget > savings:
            money = float(input())
            if money > 0:
                savings += money
                if savings >= budget:
                    print(f"Going to {location}!")
                    savings = 0
            if savings == 0:
                break
    location = input()